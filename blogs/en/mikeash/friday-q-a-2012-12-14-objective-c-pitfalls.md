---
title: 'Friday Q&A 2012-12-14: Objective-C Pitfalls'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-12-14-objective-c-pitfalls.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5e1e81c873ce1da2'
translated: false
---

> 原文：[Friday Q&A 2012-12-14: Objective-C Pitfalls](https://www.mikeash.com/pyblog/friday-qa-2012-12-14-objective-c-pitfalls.html)　·　mikeash.com Friday Q&A

Posted at 2012-12-14 14:38 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-12-28: What Happens When You Load a Byte of Memory](https://www.mikeash.com/pyblog/friday-qa-2012-12-28-what-happens-when-you-load-a-byte-of-memory.html)  
Previous article: [Friday Q&A 2012-11-30: Let's Build A Mach-O Executable](https://www.mikeash.com/pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-12-14: Objective-C Pitfalls

by [Mike Ash](https://www.mikeash.com/)

**Introduction**  
I'll use the same definition as Horstmann: a pitfall is code that compiles, links, runs, but doesn't do what you might expect it to. He provides this example, which is just as problematic in Objective-C as it is in C++:

```
    if (-0.5 <= x <= 0.5) return 0;
```

A naive reading of this code would be that it checks to see whether `x` is in the range [-0.5, 0.5]. However, that's not the case. Instead, the comparison gets evaluated like this:

```
    if ((-0.5 <= x) <= 0.5)
```

In C, the value of a comparison expression is an `int`, either `0` or `1`, a legacy from when C had no built-in boolean type. It is that `0` or `1`, not the value of `x`, that is compared with 0.5. In effect, the second comparison works as an extremely weirdly phrased negation operator, such that the if statement's body will execute if and only if `x` is less than -0.5.

**Nil Comparison**  
Objective-C is highly unusual in that sending messages to `nil` does nothing and simply returns `0`. In nearly every other language you're likely to encounter, the equivalent is either prohibited by the type system or produces a runtime error. This can be both good and bad. Given the subject of the article, we'll concentrate on the bad.

First, let's look at equality testing:

```
    [nil isEqual: @"string"]
```

Messaging `nil` returns `0`, which in this case is equivalent to `NO`. That happens to be the correct answer here, so we're off to a good start! However, consider this:

```
    [nil isEqual: nil]
```

This _also_ returns `NO`. It doesn't matter that the argument is the exact same value. The argument's value doesn't matter _at all_, because messages to `nil` always return `0` no matter what. So going by `isEqual:`, `nil` never equals anything, including itself. Mostly right, but not always.

Finally, consider one more permutation with `nil`:

```
    [@"string" isEqual: nil]
```

What does this do? Well, we can't be sure. It may return `NO`. It may throw an exception. It may simply crash. Passing `nil` to a method that doesn't explicitly say it's allowed is a bad idea, and `isEqual:` doesn't say that it accepts `nil`.

Many Cocoa classes also include a `compare:` method. This takes another object of the same class and returns either `NSOrderedAscending`, `NSOrderedSame`, or `NSOrderedDescending`, to indicate less than, equal, or greater than.

What happens if we compare with `nil`?

```
    [nil compare: nil]
```

This returns `0`, which happens to be equal to `NSOrderedSame`. Unlike `isEqual:`, `compare:` thinks `nil` equals `nil`. Handy! However:

```
    [nil compare: @"string"]
```

This _also_ returns `NSOrderedSame`, which is definitely the wrong answer. `compare:` will consider `nil` to be equal to anything and everything.

Finally, just like `isEqual:`, passing `nil` as the parameter is a bad idea:

```
    [@"string" compare: nil]
```

In short, be careful with `nil` and comparisons. It really just doesn't work right. If there's any chance your code will encounter `nil`, you _must_ check for and handle it separately before you start doing `isEqual:` or `compare:`.

**Hashing**  
You write a little class to contain some data. You have multiple equivalent instances of this class, so you implement `isEqual:` so that those instances will be treated as equal. Then you start adding your objects to an `NSSet` and things start behaving strangely. The set claims to hold multiple objects after you just added one. It can't find stuff you just added. It may even crash or corrupt memory.

This can happen if you implement `isEqual:` but don't implement `hash`. A lot of Cocoa code requires that if two objects compare as equal, they will also have the same hash. If you only override `isEqual:`, you violate that requirement. Any time you override `isEqual:`, _always_ override `hash` at the same time. For more information, see my article on [Implementing Equality and Hashing](https://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html).

**Macros**  
Imagine you're writing some unit tests. You have a method that's supposed to return an array containing a single object, so you write a test to verify that:

```
    STAssertEqualObjects([obj method], @[ @"expected" ], @"Didn't get the expected array");
```

This uses the new literals syntax to keep things short. Nice, right?

Now we have another method that returns _two_ objects, so we write a test for that:

```
    STAssertEqualObjects([obj methodTwo], @[ @"expected1", @"expected2" ], @"Didn't get the expected array");
```

Suddenly, the code fails to compile and produces completely bizarre errors. What's going on?

What's going on is that `STAssertEqualObjects` is a macro. Macros are expanded by the preprocessor, and the preprocessor is an ancient and fairly dumb program that doesn't know anything about modern Objective-C syntax, or for that matter modern C syntax. The preprocessor splits macro arguments on commas. It's smart enough to know that parentheses can nest, so this is seen as three arguments:

```
    Macro(a, (b, c), d)
```

Where the first argument is `a`, the second is `(b, c)`, and the third is `d`. However, the preprocessor has no idea that it should do the same thing for `[]` and `{}`. With the above macro, the preprocessor sees _four_ arguments:

- `[obj methodTwo]`
- `@[ @"expected1"`
- `@"expected2 ]`
- `@"Didn't get the expected array"`

This results in completely mangled code that not only doesn't compile, but confuses the compiler beyond the ability to provide understandable diagnostics. The solution is easy, once you know what the problem is. Just parenthesize the literal so the preprocessor treats it as one argument:

```
    STAssertEqualObjects([obj methodTwo], (@[ @"expected1", @"expected2" ]), @"Didn't get the expected array");
```

Unit tests are where I've run into this most frequently, but it can pop up any time there's a macro. Objective-C literals will fall victim, as will C compound literals. Blocks can also be problematic if you use the comma operator within them, which is rare but legal. You can see that Apple thought about this problem with their `Block_copy` and `Block_release` macros in `/usr/include/Block.h`:

```
    #define Block_copy(...) ((__typeof(__VA_ARGS__))_Block_copy((const void *)(__VA_ARGS__)))
    #define Block_release(...) _Block_release((const void *)(__VA_ARGS__))
```

These macros conceptually take a single argument, but they're declared to take variable arguments to avoid this problem. By taking `...` and using `__VA_ARGS__` to refer to "the argument", multiple "arguments" with commas are reproduced in the macro's output. You can take the same approach to make your own macros safe from this problem, although it only works on the last argument of a multi-argument macro.

**Property Synthesis**  
Take the following class:

```
    @interface MyClass : NSObject {
        NSString *_myIvar;
    }

    @property (copy) NSString *myIvar;

    @end

    @implementation MyClass

    @synthesize myIvar;

    @end
```

Nothing wrong with this, right? The ivar declaration and `@synthesize` are a little redundant in this modern age, but do no harm.

Unfortunately, this code will _silently_ ignore `_myIvar` and synthesize a _new_ variable called `myIvar`, without the leading underscore. If you have code that uses the ivar directly, it will see a different value from code that uses the property. Confusion!

The rules for `@synthesize` variable names are a little weird. If you specify a variable name with `@synthesize myIvar = _myIvar;`, then of course it uses whatever you specify. If you leave out the variable name, then it synthesizes a variable with the same name as the property. If you leave out `@synthesize` altogether, then it synthesizes a variable with the same name as the property, _but with a leading underscore_.

Unless you need to support 32-bit Mac, your best bet these days is to just avoid explicitly declaring backing ivars for properties. Let `@synthesize` create the variable, and if you get the name wrong, you'll get a nice compiler error instead of mysterious behavior.

**Interrupted System Calls**  
Cocoa code usually sticks to higher level constructs, but sometimes it's useful to drop down a bit and do some `POSIX`. For example, this code will write some data to a file descriptor:

```
    int fd;
    NSData *data = ...;

    const char *cursor = [data bytes];
    NSUInteger remaining = [data length];

    while(remaining > 0) {
        ssize_t result = write(fd, cursor, remaining);
        if(result < 0)
        {
            NSLog(@"Failed to write data: %s (%d)", strerror(errno), errno);
            return;
        }
        remaining -= result;
        cursor += result;
    }
```

However, this can fail, and it will fail strangely and intermittently. POSIX calls like this can be interrupted by signals. Even harmless signals handled elsewhere in the app like `SIGCHLD` or `SIGINFO` can cause this. `SIGCHLD` can occur if you're using `NSTask` or are otherwise working with subprocesses. When `write` is interrupted by a signal, it returns `-1` and sets `errno` to `EINTR` to indicate that the call was interrupted. The above code treats all errors as fatal and will bail out, even though the call just needs to be tried again. The correct code checks for that separately and just retries the call:

```
    while(remaining > 0) {
        ssize_t result = write(fd, cursor, remaining);
        if(result < 0 && errno == EINTR)
        {
            continue;
        }
        else if(result < 0)
        {
            NSLog(@"Failed to write data: %s (%d)", strerror(errno), errno);
            return;
        }
        remaining -= result;
        cursor += result;
    }
```

**String Lengths**  
The same string, represented differently, can have different lengths. This is a relatively common but incorrect pattern:

```
    write(fd, [string UTF8String], [string length]);
```

The problem is that `NSString` computes length in terms of UTF-16 code units, while `write` wants a count of bytes. While the two numbers are equal when the string only contains ASCII (which is why people so frequently get away with writing this incorrect code), they're no longer equal once the string contains non-ASCII characters such as accented characters. Always compute the length of the same representation you're manipulating:

```
    const char *cStr = [string UTF8String];
    write(fd, cStr, strlen(cStr));
```

**Casting to BOOL**  
Take this bit of code that just checks to see whether an object pointer is `nil`:

```
    - (BOOL)hasObject
    {
        return (BOOL)_object;
    }
```

This works... usually. However, roughly 6% of the time, it will return `NO` even though `_object` is not `nil`. What gives?

The `BOOL` type is, unfortunately, not a boolean. Here's how it's defined:

```
    typedef signed char BOOL;
```

This is another bit of unfortunate legacy from the days when C had no boolean type. Cocoa predates C99's `_Bool`, so it defines its "boolean" type as a `signed char`, which is just an 8-bit integer. When you cast a pointer to an integer, you just get the numeric value of that pointer. When you cast a pointer to a small integer, you just get the numeric value of the lower bits of that pointer. When the pointer looks like this:

```
    ....110011001110000
```

The `BOOL` gets this:

```
               01110000
```

This is not `0`, meaning that it evaluates as true, so what's the problem? The problem is when the pointer looks like this:

```
    ....110011000000000
```

Then the `BOOL` gets this:

```
               00000000
```

This is `0`, also known as `NO`, even though the pointer wasn't `nil`. Oops!

How often does this happen? There are `256` possible values in the `BOOL`, only one of which is `NO`, so we'd naively expect it to happen about 1/256 of the time. However, Objective-C objects are allocated aligned, normally to `16` bytes. This means that the bottom four bits of the pointer are always zero (something that [tagged pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html) takes advantage of) and there are only four bits of freedom in the resulting `BOOL`. The odds of getting all zeroes there are about 1/16, or about 6%.

To safely implement this method, perform an explicit comparison against `nil`:

```
    - (BOOL)hasObject
    {
        return _object != nil;
    }
```

If you want to get clever and unreadable, you can also use the `!` operator twice. This `!!` construct is sometimes referred to as C's "convert to boolean" operator, although it's just built from parts:

```
    - (BOOL)hasObject
    {
        return !!_object;
    }
```

The first `!` produces `1` or `0` depending on whether `_object` is `nil`, but backwards. The second `!` then puts it right, resulting in `1` if `_object` is not `nil`, and `0` if it is.

You should probably stick to the `!= nil` version.

**Missing Method Argument**  
Let's say you're implementing a table view data source. You add this to your class's methods:

```
    - (id)tableView:(NSTableView *) objectValueForTableColumn:(NSTableColumn *)aTableColumn row:(NSInteger)rowIndex
    {
        return [dataArray objectAtIndex: rowIndex];
    }
```

Then you run your app and `NSTableView` complains that you haven't implemented this method. But it's right there!

As usual, the computer is correct. The computer is your friend.

Look closer. The first parameter is _missing_. Why does this even _compile?_

It turns out that Objective-C allows empty selector segments. The above does not declare a method named `tableView:objectValueForTableColumn:row:` with a missing argument name. It declares a method named `tableView::row:`, and the first argument is named `objectValueForTableColumn`. This is a particularly nasty way to typo the name of a method, and if you do it in a context where the compiler can't warn you about the missing method, you may be trying to debug it for a long time.

**Conclusion**  
Objective-C and Cocoa have plenty of pitfalls ready to trap the unwary programmer. The above is just a sampling. However, it's a good list of things to be careful of.

That's it for today! Check back next time for more wacky advice. Friday Q&A is driven by user ideas, in case you didn't already know, so until next time, please [send in your ideas for articles](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-12-14-objective-c-pitfalls.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
