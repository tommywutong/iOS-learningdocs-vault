---
title: 'Friday Q&A 2009-06-26: Type Qualifiers in C, Part 1'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-06-26-type-qualifiers-in-c-part-1.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e86ecde52781b2e2'
translated: false
---

> 原文：[Friday Q&A 2009-06-26: Type Qualifiers in C, Part 1](https://www.mikeash.com/pyblog/friday-qa-2009-06-26-type-qualifiers-in-c-part-1.html)　·　mikeash.com Friday Q&A

Posted at 2009-06-26 16:11 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-07-03: Type Specifiers in C, Part 2](https://www.mikeash.com/pyblog/friday-qa-2009-07-03-type-specifiers-in-c-part-2.html)  
Previous article: [Friday Q&A 2009-06-19: Mac OS X Process Memory Statistics](https://www.mikeash.com/pyblog/friday-qa-2009-06-19-mac-os-x-process-memory-statistics.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-06-26: Type Qualifiers in C, Part 1

by [Mike Ash](https://www.mikeash.com/)

**What They Are**  
 The first thing is to talk about what type qualifiers actually are. In short, they're a keyword which can be used to modify the properties of an arbitrary type. The most common one is `const`. Type qualifiers should not be confused with keywords which modify the _storage_ of a particular variable. Those are called storage specifiers.

Let me illustrate with an example:

```
    static const int *x;
```

Here, `static` is a storage specifier. It modifies the variable `x` to change how `x` is actually stored. The `const` keyword is a type qualifier, which modifies the `int` type.

By way of illustration, it makes perfect sense to use `const` in a `typedef`, like so:

```
    typedef const int MyConstInt;
```

But it makes no sense to use

in this way, because

is not part of the type:

```
    typedef static int MyStaticInt; // will not compile, does not make sense!
```

The C99 language contains three type qualifiers:

- `const`
- `restrict`
- `volatile`

This week I will discuss `const` and `restrict`, and I'll finish up next week with a discussion of `volatile`.

**The `const` keyword**  
 The const qualifier is far and away the most common and the most useful of the three. Its meaning is very easy to understand: when applied to a type, `const` makes that type become read-only.

There are several places where `const` can be useful:

1. A

  function pointer parameter means that the function won't modify the value that the pointer points to. For example, look at the standard

  function. The first parameter is declared of type

  , because this function only reads the string, and doesn't modify it. This is a useful thing to do with your own code as well when taking pointer parameters that won't be modified.
2. Used here,

  indicates that the data being returned is read-only and the caller is not allowed to modify it. For example, the

  method in Cocoa returns a

  . This means you can use the data but you're not allowed to write to it. The data may be a pointer to some kind of internal storage or cache, and the

  is used to enforce access to make this useful.
3. When used here,

  indicates that this pointer can't be used to modify its contents. This can be useful to preserve correctness when you know that your use is read-only, but is most often useful to shut up the compiler when accessing

  return values from functions that return

  pointers as in #2.
4. This is handy to declare a compile-time constant. For example,

  declares a constant. The

  here will help prevent you from changing this value by accident, and may also allow the compiler to do some optimizations that otherwise would not be possible.

Note that this is not meant to be an exhaustive list, and there are probably other interesting places to use it as well.

Since this is a heavily Mac-centric blog, I also want to briefly discuss `const` as it applies to Objective-C. In particular, you should never declare an Objective-C object type as `const`. For example, this is _not_ a good way to enforce the immutability of an `NSString`:

```
const NSString *immutableNSStringPointer;
```

What

means here is that you can't use

to modify the memory at that location. But the immutability of an

is part of the API contract only. Nothing says that the memory of an

can't be modified, only that the

contents of the

can't be modified. For example,

might have some internal caches that get updated, but which don't affect the conceptual contents of the string. Changing those caches would violate the

requirement, but not the immutability of the

.

More concretely, if you declare a variable like this and then try to use it anywhere, you'll get a huge number of useless warnings about violating the `const`ness of your variable.

What if you want a constant NSString pointer? Not a pointer to a constant NSString, but a constant pointer, one which can't be changed. The NSString equivalent of the `const int kMeaning = 42;` example from above. This can easily be done, you just have to apply the `const` to the _variable_ directly, by altering its position:

```
    NSString * const kConstantStringPointer = @"hello, world";
```

The

keyword is new in C99. (The other two date from C89.) This one is purely for the purposes of optimization. That fact, combined with the fact that it's kind of hard to understand, means that this keyword is extremely rare to see and even more rare to actually use.

So what does `restrict` mean, exactly? It's actually pretty simple: when a pointer is declared with `restrict`, it tells the compiler that this is the only pointer which will be accessing a particular chunk of memory in that scope.

But what does that _mean_? Consider the following code:

```
    char *src, *dst;
    ...
    for(int i = 0; i < len; i++)
        dst[i] = src[i];
```

When compiling this code, the compiler will need to generate an individual memory load followed by an individual memory store for each iteration of this loop. There are techniques to make this loop run significantly faster by loading and storing larger chunks of memory at once, but the compiler can't use them. Imagine what would happen if

pointed to

. Each time the assignment is made, it also alters the value that will be used for the next iteration of the loop. Unless the compiler can rule out this possibility (which is extremely difficult to do automatically) it's forced to generate very slow code.

This is where the `restrict` keyword comes in. By declaring `src` and `dst` as `restrict`, you tell the compiler that you are personally guaranteeing that they won't point into the same block of memory, and thus that the compiler should feel free to generate nice, fast code for this loop.

It's unlikely that you'll have occasion to use `restrict` in your own code. However you may encounter it elsewhere. For example, here is the prototype for the `memcpy` function:

```
    void *memcpy(void *restrict s1, const void *restrict s2, size_t n);
```

When used on a function argument like this, it means that you must not provide overlapping pointers to this function. That's part of

API contract: it only works on blocks which don't overlap. (The

function is provided for blocks which potentially do overlap.) Previously this was only expressed in the documentation, but using

it can actually be expressed right in the code.

**Wrapping Up**  
 That brings us to the end of Part 1. Now you know what `const` and `restrict` mean and how to use them. The `const` can be very useful and every C programmer should know how to use it. The `restrict` keyword is mostly useless unless you're writing certain kinds of highly optimized code, but it's still good to know the basics.

Next week I'll discuss the `volatile` keyword. It sits in an interesting middle ground in between `const` and `restrict`: not nearly as useful or common as the former, but much more widely used and marginally more useful than the latter. It's also very frequently misunderstood and misused. For all the details on what it does, how to use it, and (most importantly) how _not_ to use it, check back next week.

And as always, Friday Q&A runs on your ideas, so send them in! If you have a subject that you would like to see discussed here, post it in the comments or [e-mail it to me directly](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
