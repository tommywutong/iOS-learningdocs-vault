---
title: 'Friday Q&A 2011-04-15: Compile-Time Tips and Tricks'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-04-15-compile-time-tips-and-tricks.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bb0cfead6c26e235'
translated: false
---

> 原文：[Friday Q&A 2011-04-15: Compile-Time Tips and Tricks](https://www.mikeash.com/pyblog/friday-qa-2011-04-15-compile-time-tips-and-tricks.html)　·　mikeash.com Friday Q&A

Posted at 2011-04-15 16:20 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A Falls Behind](https://www.mikeash.com/pyblog/friday-qa-falls-behind.html)  
Previous article: [Link: Implementing imp_implementationWithBlock](https://www.mikeash.com/pyblog/link-implementing-imp_implementationwithblock.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-04-15: Compile-Time Tips and Tricks

by [Mike Ash](https://www.mikeash.com/)

**`#if`, `#elif`, `#else`, `#endif`**  
 A common one which is already familiar to most people is the `#if` directive. This instructs the preprocessor to conditionally include or eliminate a block of code based on a condition. The `#elif` directive allows checking for an alternate, `#else` allows a fallback, and the whole thing is concluded with `#endif` For example:

```
    #if 2 + 2 == 4
        ThisCodeGetsIncluded();
    #elif 3 + 3 == 6
        NotIncludedBecauseTheFirstWasTrue();
    #else
        NotIncludedBecauseOneWasTrue();
    #endif
```

While limited expressions are allowed, like the above, `#if` is most commonly used with simple identifiers, defined by the user, by system headers, or by the compiler:

```
    #if __LITTLE_ENDIAN__
        // little endian code here
    #else
        // big endian code here
    #endif
    
    #define LOGGING_ENABLED 1
    #if LOGGING_ENABLED
        #define LOG NSLog
    #else
        #define LOG(...) (void)0
    #endif
```

These support common C-like expressions such as comparison operators and logical operators like `&&` and `||`.

In addition to testing the value of identifiers, it's also possible to simply test for whether an identifier is defined. This is done using the `defined` pseudo-function, like so:

```
    #if defined(MIGHT_NOT_BE_DEFINED)
        // it's defined!
    #endif
```

Note that, unlike most places in C, using an undefined identifier in `#if` is not illegal, it simply treats it as zero.

Since testing whether an identifier is defined or not is a pretty common operation, there are shortcuts for it. `#ifdef X` is equivalent to `#if defined(X)`, and `#ifndef X` is equivalent to `#if !defined(X)`. These shortcuts are handy, but can't be easily combined into more complicated logical expressions, so `defined` is often useful as well.

One major use of `#if` is to alter code based on the target platform. For example, you may have code which targets both Mac and iOS but needs some minor alterations between platforms. Apple offers a few conditionals that you can check for this. They are described in a handy table here: [Hamster Emporium: TargetConditionals.h](http://www.sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html).

When using these constructs, it's important to understand just when they run and what they work on. They are all evaluated by the preprocessor, before any real compilation begins. They only understand preprocessor identifiers, _not_ identifiers from C code. For example, it's common for people who are new to C to attempt something like this:

```
    #ifndef MyType
        typedef struct { ... } MyType;
    #endif
```

The intention is to define a type only if it's not already defined. This fails, because the `typedef` is evaluated long after the preprocessor runs. As far as the preprocessor is concerned, the `MyType` identifier is never defined, even after it evaluates this code. If you need to do something like this, then you need to add a preprocessor define as well:

```
    #if !MYTYPE_DEFINED
        typedef struct { ... } MyType;
        #define MYTYPE_DEFINED 1
    #endif
```

One last note: while you can use `#define` inside an `#if` to conditionally define macros, you cannot use an `#if` inside a `#define` to build macros which make clever decisions at the point of use.

**Built-in Defines**  
 The compiler defines a variety of identifiers for every program it compiles. Many of these are obscure and low level, but it can sometimes be handy to see what's made available. To do this, a handy shell command will print them all:

```
    gcc -E -dM -x c /dev/null
```

This also works with clang instead of gcc. Let's unpack this command a bit.

First, the `-E` tells gcc to only run the preprocessor and then print its output. No compilation or linking is performed.

Next, `-dM` instructs the compiler to perform a debugging dump after that stage is performed. This dump is what we're after.

After that, the `-x c` flag tells the compiler to ignore the file extension on the file and compile it as plain C. This flag can be changed to `c++`, `objective-c`, or `objective-c++` to see what gets defined in those modes. Finally, `/dev/null` is passed to the compiler so that it receives an empty file and dumps only what it defines internally.

**`#error` and `#warning`**  
 These two directives allow creating a custom error or warning in the code. This can be handy for marking things that really need your attention to ensure that you don't forget. For example, you might add a warning about a method that really needs to be implemented:

```
    - (NSString *)importantString
    {
        #warning this needs a real implementation
        return nil;
    }
```

This warning will show up in the list along with any others from your code. If things are really dire, you can cause a hard error instead:

```
    - (NSString *)reallyImportantstring
    {
        #error running the app without an implementation here causes disaster!
    }
```

These directives go especially well in combination with the `#if` directive. They allow you to create conditionally compiled code for certain conditions, and warn or error when a situation comes up that you haven't coded for. For example, if you haven't written a big-endian version of your code yet and don't anticipate needing one soon, you might just make it an error:

```
    #if __LITTLE_ENDIAN__
        // code here
    #else
        #error we don't support big endian yet
    #endif
```

Along those lines, you may have code for both, but not entirely trust the mechanism of detection. If neither one is positively identified, you can kill compilation with an error instead of potentially picking the wrong code path by mistake:

```
    #if __LITTLE_ENDIAN__
        // code here
    #elif __BIG_ENDIAN__
        // code here
    #else
        #error unknown endianness
    #endif
```

**Compile-Time Asserts**  
 The `#error` directive is invaluable for ensuring that code isn't inadvertently compiled in an environment that it's not prepared to handle. However, it can only check for things that the preprocessor is aware of. It can't be used to check things that aren't evaluated until the compiler runs. The big use case that I know of is checking the size of a type. The preprocessor knows nothing about types, so `#error` can't be used for that.

We can use a standard `assert` macro for this, but this only works at runtime. Often this is sufficient, but it's nice to get errors while compiling if possible, and that also eliminates the risk that the assert never gets executed because the code which has it never got tested.

With a bit of trickery, it's possible to build a check which happens at compile time, late enough so that types are known, but before your program actually runs. There are actually a few different ways to do this, but my preferred way is to declare an array whose size depends on the expression to test. If it passes, set the size to `1`, which compiles. If it fails, set the size to `-1`, which is illegal and causes an error. The error message cannot be fully customized, but by giving the array a descriptive name, the message can still be conveyed.

Here's an example of a compile-time assert. This would be used in code which depends on pointers being 64 bits:

```
    extern char this_code_requires_64_bit_pointers[sizeof(void *) == 8 ? 1 : -1];
```

When the size is `8`, this code compiles fine and doesn't affect anything. When the size is anything else, the array gets a negative size and compilation is halted with an error.

The expressions that this is useful for are fairly limited (they must be compile-time constants, but something the preprocessor couldn't deal with) but when they are useful they are very nice to have.

**Conclusion**  
 In many ways, C is a small and simple language. In other ways, it's a complex language with a great deal of depth. These tips are part of that depth. While relatively simple, they can also be extremely handy to have around.

That wraps things up for today. As always, return in two more weeks for the next edition. Like I say every week, Friday Q&A is driven by reader suggestions. If you have a topic that you would like to see covered, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-04-15-compile-time-tips-and-tricks.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
