---
title: 'Friday Q&A 2013-08-02: Type-Safe Scalars with Single-Field Structs'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-08-02-type-safe-scalars-with-single-field-structs.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6246464e00cd239c'
translated: false
---

> 原文：[Friday Q&A 2013-08-02: Type-Safe Scalars with Single-Field Structs](https://www.mikeash.com/pyblog/friday-qa-2013-08-02-type-safe-scalars-with-single-field-structs.html)　·　mikeash.com Friday Q&A

Posted at 2013-08-02 15:01 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-08-16: Let's Build Dispatch Groups](https://www.mikeash.com/pyblog/friday-qa-2013-08-16-lets-build-dispatch-groups.html)  
Previous article: [Friday Q&A 2013-06-28: Anatomy of a Compiler Bug](https://www.mikeash.com/pyblog/friday-qa-2013-06-28-anatomy-of-a-compiler-bug.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2013-08-02: Type-Safe Scalars with Single-Field Structs

by [Mike Ash](https://www.mikeash.com/)

**`typedef`**  
C's `typedef` facility is tremendously useful for turning primitives into more semantic types, and a typical C program will be full of them. Even if you never write them yourself, you typically inherit a ton of them from system frameworks and the like. For example, Cocoa gives you types like `NSTimeInterval`, `NSInteger`, and `CGFloat`.

However, the `typedef` facility is weak. It doesn't produce a new type, but rather it just creates a new name for the existing type. For example, `NSTimeInterval` is declared as:

```
    typedef double NSTimeInterval;
```

This means that an `NSTimeInterval` _is_ just a `double`. They're two names for the same thing.

Sometimes that's exactly what we want. The whole point of `NSInteger` is just to be either an `int` or a `long` depending on architecture. Likewise, `CGFloat` just exists to give you either a `float` or a `double` depending on architecture.

`NSTimeInterval` is a different beast. Conceptually, it's not just a `double`, but a `double` _representing a number of seconds_. You might write this:

```
    NSTimeInterval interval = 5.0; // five seconds
```

But you probably wouldn't write this:

```
    NSTimeInterval interval = [view frame].size.width;
```

It's _possible_ that you just happen to want an interval that's equal to the width of a view, interpreted as seconds. However, it's not very likely. It would be nice if the type system could notice that you're trying to assign a `float` or `double` to a `NSTimeInterval` and call this out as being wrong. Unfortunately, `typedef` can't do this, because `NSTimeInterval` _is_ a `double` in the end.

**`struct`**  
An interesting feature of C `struct`s is that structurally-identical `struct`s are still different types. For example, given this:

```
    struct Foo { int x, y; };
    struct Bar { int x, y; };
```

This will not compile:

```
    struct Foo foo;
    struct Bar bar = foo;
```

Despite the fact that `foo` and `bar` have identical contents, they have different types, the compiler won't convert between the two.

This fact gives us the tool we need to create new types rather than simply creating new names for existing types.

**Single-Field `struct`s**  
The idea is simple. Rather than define a time interval using `typedef`, define it with a `struct` that contains a single element:

```
    typedef struct MATimeInterval {
        double seconds;
    } MATimeInterval;
```

This still uses `typedef`, of course, but just as a convenience, so that we can write the type as `MATimeInterval` instead of `struct MATimeInterval`.

The fact that it's a struct has some syntactic consequences which makes the code more verbose. While this is a minor disadvantage over a plain `typedef`, it's also an advantage in that it makes code more explicit. For example, you can no longer write something like this:

```
    MATimeInterval interval = 5;
```

Instead, you need some braces:

```
    MATimeInterval interval = { 5 };
```

Using field initializers, you can make it more explicit:

```
    MATimeInterval interval = { .seconds = 5 };
```

This way there's no doubt what unit of time is being used.

When passing a value to a function or method that takes a `MATimeInterval` as a parameter, you can no longer just pass a number. Instead, you can use C's [compound literals syntax](https://www.mikeash.com/pyblog/friday-qa-2011-02-18-compound-literals.html):

```
    [obj methodThatTakesATimeInterval: (MATimeInterval){ 5 }];
```

It can also be nice to make a helper function:

```
    MATimeInterval MATimeIntervalMakeSeconds(double seconds)
    {
        return (MATimeInterval){ seconds };
    }

    [obj methodThatTakesATimeInterval: MATimeIntervalMakeSeconds(5)];
```

One advantage of this, aside from slightly better syntax, is that you can make functions that take other units of time as well:

```
    MATimeInterval MATimeIntervalMakeMinutes(double minutes)
    {
        return MATimeIntervalMakeSeconds(minutes * 60);
    }

    [obj methodThatTakesATimeInterval: MATimeIntervalMakeMinutes(5)];
```

A major disadvantage of the `struct` approach is that it makes arithmetic much messier. For example, instead of this:

```
    NSTimeInterval delta = a - b;
```

You get something like this:

```
    MATimeInterval delta = MATimeIntervalMakeSeconds(a.seconds - b.seconds);
```

I think the benefits are well worth it even so. If this sort of thing is a common operation, you can make a helper function:

```
    MATimeInterval MATimeIntervalDelta(MATimeInterval a, MATimeInterval b)
    {
        return MATimeIntervalMakeSeconds(a.seconds - b.seconds);
    }
```

This hides the details of the calculation and makes the calling code a bit nicer:

```
    MATimeInterval delta = MATimeIntervalDelta(a, b);
```

**Unit Interplay**  
Once you start doing this, you can come up with interesting helper functions that manipulate multiple types. For example, let's also create distance and velocity types:

```
    typedef struct MADistance {
        double meters;
    } MADistance;

    typedef struct MAVelocity {
        double metersPerSecond;
    } MAVelocity;
```

You can then write a nice function that takes a distance and a time and produces a velocity:

```
    MAVelocity MAVelocityFromDistanceAndTime(MADistance dist, MATimeInterval time)
    {
        return (MAVelocity){ .metersPerSecond = dist.meters / time.seconds };
    }

    MATimeInterval t = ...;
    MADistance d = ...;
    MAVelocity v = MAVelocityFromDistanceAndTime(d, t);
```

The function implementation is explicit and clear, with all the units spelled out, and the calling code is direct and to the point.

**Runtime Costs**  
When replacing a bunch of simple primitives with `struct`s, it's natural to be worried about the runtime costs. An `int` or a `double` can fit into a register and be directly manipulated with machine instructions, but a `struct` must require more work to load and unload the values within.

The good news is that this is not the case. It would be true if we were using, say, full-fledged Objective-C objects, but `struct`s are sufficiently low-level that they can be completely optimized away. The compiler is able to treat each element of a `struct` as a separate value:

```
    struct Foo {
        int a;
        long b;
        double c;
    };

    struct Foo foo;
    foo.a = 42;
    foo.b = 99;
    foo.c = 3.14;
```

As long as you don't take the address of `foo`, the compiler is free to rearrange the storage at will. It can put `a`, `b`, and `c` into individual registers. It can even eliminate or short-circuit the assignments altogether if circumstances allow. Take this function for example:

```
    CGFloat f(void)
    {
        CGSize s = { 12, 34 };
        return sqrt(s.width * s.width + s.height * s.height);
    }
```

You might expect this to allocate 16 bytes on the stack (two `double` components in the `CGSize`, when targeting `x86-64`), then perform two multiplies, a subtraction, and finally a call to `sqrt()`. Here is the code that `clang` produces when compiling this function with optimizations:

```
    _f:
        movq  %rsp, %rbp
        movsd LCPI0_0(%rip), %xmm0
        popq  %rbp
        ret

    LCPI1_0:
        .quad 4630271179615950904     ## double 3.605551e+01
```

It's able to peel away the `struct` and precalculate the entire expression, so that the executed code does nothing but returning that precalculated value.

There's never a case where a single-field `struct` _can't_ be treated as being the same as the field it contains at runtime. Manipulating the `struct` to get or set the value inside becomes free. Even passing them as parameters to methods or returning them from methods imposes no additional overhead compared to using the underlying type directly, at least on any architecture we're likely to encounter. The field access ends up as nothing more than compile-time syntax.

**Conclusion**  
The C type system is fairly weak, and the common technique of using `typedef` to produce new type names makes it easy to mix up values of different conceptual types in code. The `struct` keyword creates an entirely new type which can be used to avoid this, allowing the compiler to enforce the difference between your types. The resulting code becomes more verbose, which can be good or bad, depending on your perspective and situation. While constantly packing and unpacking structs can be a pain, wisely chosen field names can help make it more obvious just what kind of values the code is working with.

That wraps it up for today! Come back next time for more craziness. Friday Q&A is driven by reader suggestions, so if you have a topic you'd like to see covered that next time, or some time after that, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-08-02-type-safe-scalars-with-single-field-structs.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
