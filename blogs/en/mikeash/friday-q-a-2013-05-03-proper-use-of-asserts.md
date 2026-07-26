---
title: 'Friday Q&A 2013-05-03: Proper Use of Asserts'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-05-03-proper-use-of-asserts.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:555b93d519f0ce66'
translated: false
---

> 原文：[Friday Q&A 2013-05-03: Proper Use of Asserts](https://www.mikeash.com/pyblog/friday-qa-2013-05-03-proper-use-of-asserts.html)　·　mikeash.com Friday Q&A

Posted at 2013-05-03 13:03 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-05-17: Let's Build stringWithFormat:](https://www.mikeash.com/pyblog/friday-qa-2013-05-17-lets-build-stringwithformat.html)  
Previous article: [Friday Q&A Is On Vacation](https://www.mikeash.com/pyblog/friday-qa-is-on-vacation.html)  
Tags: [assert](https://www.mikeash.com/pyblog/?tag=assert) [c](https://www.mikeash.com/pyblog/?tag=c) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-05-03: Proper Use of Asserts

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Romanian (translation by Science Blog)](http://someblogscience.com/pyblog.html) and [Georgian (translation by Irakli Nishnianidze)](http://i-love-png.com/friday-qa-2013-05-03-proper-use-of-asserts.html).

**APIs**  
Fundamentally, an assert is just a call that takes an expression and indicates failure in some way if the expression isn't true. The basic idea is to check for conditions that should always be true so that you fail early and obviously, rather than failing later and confusingly. For example, an array dereference will fail in various weird ways if you give it a bad index:

```
    x = array[index]; // sure hope index is in range
```

Using an assert can help make it obvious what went wrong:

```
    assert(index >= 0 && index < arrayLength);
    x = array[index];
```

This actually demonstrates an API for asserts. C provides the `assert` function if you `#include <assert.h>`. It takes a single expression. If the expression is true, it does nothing. If it's false, it prints the expression, the file name and line number where the assert is located, and then calls `abort`, terminating the program.

Cocoa provides several assert functions as well. The most basic is `NSAssert`. It takes an expression and a string description, which can be a format string:

```
    NSAssert(x != y, @"x and y were equal, this shouldn't happen");
    NSAssert(z > 3, @"z should be greater than 3, but was actually %d", z);
    NSAssert(str != nil, @"nil string while processing %@ of type %@", name, type);
```

Like the `assert` function, this logs the assertion failure if the expression is false. It then throws an `NSInternalInconsistencyException`, and what happens then depends on what exception handlers are present. In a typical Cocoa app, it will either be caught and logged by the runloop, or it will terminate the application.

Unfortunately, the logging from `NSAssert` is weak. It logs the fact that the assertion failed, as well as the method it was in and the filename and line number, but it doesn't actually log the expression that failed, nor does it log the reason string provided to the macro. The exception it throws does include the reason string, at least, so as long as the exception gets printed at some point, that will show up.

There are a few variants of this call available in Cocoa. The `NSAssert` call only works within an Objective-C method, so there's an equivalent `NSCAssert` call that works in a C function. There's also `NSParameterAssert`, which doesn't take a description string and is intended for quickly checking a parameter value, and an equivalent `NSCParameterAssert` for C functions.

**Build Your Own**  
The built-in options aren't great. The C `assert` is decent, but doesn't allow for a customizable message. The Cocoa calls have bad logging, and their behavior in the event of a failed assertion depends too much on runtime context, and may not actually terminate the app.

These things aren't hard to build, though, so let's build one that does things right! We'll want a call that takes an expression and optionally a description format string:

```
    MAAssert(x > 0);
    MAAssert(y > 3, @"Bad value for y");
    MAAssert(z > 12, @"Bad value for z: %d", z);
```

It should log the expression, the format string if it exists, and the filename, line number, and function name where the problem occurred. Additionally, it should only evaluate the format string parameters if the assertion fails, to make things more efficient. All of this calls for a macro.

[Like all good multi-line macros](https://www.mikeash.com/pyblog/friday-qa-2010-12-31-c-macro-tips-and-tricks.html), this macro is wrapped in a `do`/`while` construct:

```
    #define MAAssert(expression, ...) \
        do { \
```

The first thing it does is check whether the expression is actually false:

```
            if(!(expression)) { \
```

If it is, it uses `NSLog` to log the details of the failure:

```
                NSLog(@"Assertion failure: %s in %s on line %s:%d. %@", #expression, __func__, __FILE__, __LINE__, [NSString stringWithFormat: @"" __VA_ARGS__]); \
```

The `#expression` construct produces a string literal containing the text of the expression. For example, it will produce `"x > 0"` for the first assert call above. The `__func__` identifier produces the name of the current function. `__FILE__` and `__LINE__` should be self-explanatory. The dummy `@""` in the `stringWithFormat:` call ensures that the syntax is legal even when no reason string is provided.

After logging the assertion failure, it then terminates the app by calling `abort`, and the macro ends:

```
                abort(); \
            } \
        } while(0)
```

This works perfectly. It allows an additional explanatory string, but doesn't require it for cases where the expression is enough to make it clear what's going wrong. It always calls `abort` on failure, rather than throwing an exception that could potentially be caught. It logs all available details at the point of failure.

**Application Specific Information**  
It would be great if we could get the failure message to show up in crash logs as well. Turns out, we can! [Wil Shipley demonstrated](https://gist.github.com/ccgus/5020894) how to put custom data into the "Application Specific Information" section of a crash log. Put this somewhere in the source code:

```
    const char *__crashreporter_info__ = NULL;
    asm(".desc ___crashreporter_info__, 0x10");
```

Any string written into this magic global variable will show up in that section of the crash log. This doesn't work everywhere (word is that it doesn't work on iOS), but it can be handy, and does no harm when it doesn't work. If you want to take advantage of this, a small modification to the assert macro will put the message into this variable as well as logging it:

```
    #define MAAssert(expression, ...) \
        do { \
            if(!(expression)) { \
                NSString *__MAAssert_temp_string = [NSString stringWithFormat: @"Assertion failure: %s in %s on line %s:%d. %@", #expression, __func__, __FILE__, __LINE__, [NSString stringWithFormat: @"" __VA_ARGS__]]; \
                NSLog(@"%@", __MAAssert_temp_string); \
                __crashreporter_info__ = [__MAAssert_temp_string UTF8String]; \
                abort(); \
            } \
        } while(0)
```

And, as if by magic, the message appears in the crash log.

**Philosophy**  
Now that you know how to write an assert in many different ways, just _what kind_ of asserts should you write?

Asserts should be written for conditions that, according to your understanding of the program, should _never_ occur. Asserts should _not_ be used to check for errors that are actually expected to happen in some cases. For example, asserting that a filename is not `nil` is good technique:

```
    assert(filename != nil);
```

However, asserting that data could be read from that file is bad practice:

```
    NSData *data = [NSData dataWithContentsOfFile: filename];
    assert(data != nil);
```

That call can legitimately fail due to real-world conditions, such as the file not existing on disk, or not having permissions to read it. Because of that, this code needs some actual error handling, not just an assert. Failing to read the file should result in taking an alternate approach or alerting the user that something went wrong, not just logging and terminating the app.

Typically, the most useful place for asserts is at the top of a function or method, to check constraints on the parameters that can't be expressed in the language directly. These asserts correspond directly to constraints expressed in the documentation. For example:

```
    // Flange an array of sprockets. The sprockets array must contain
    // at least two entries, and the index must lie within the array.
    - (void)flangeSprockets: (NSArray *)array fromIndex: (NSUInteger)index
    {
        assert([array count] >= 2);
        assert(index < [array count]);

        ...method body...
```

The gap between a caller and a callee makes it easy to lose track of these constraints, making this an excellent place to double-check that everything is as it should be. Special attention should be paid to parameters that are easy to screw up, and to parameters where bad values will cause strange failures. For example, this assert checking for `NULL`, while still useful, doesn't add much, since the resulting crash without it would still be fairly clear:

```
    assert(ptr != NULL);
    x = *ptr;
```

It's not _bad_, but your time may be better spent elsewhere. This assert checking for `nil` is really handy, as a `nil` value here will just result in a strangely built string, which could show up far away and much later:

```
    assert(name != nil);
    str = [NSString stringWithFormat@"Hello, %@!", name];
```

It can also be handy to add asserts in the middle of complex code which has clear pre or post-conditions. For example, in the middle of modifying a data structure, you might check to make sure all of your variables have consistent values between themselves:

```
    assert(done + remaining == total);
```

This will let you catch logic errors quickly.

Avoid asserts for obvious conditions that have little room for error. For example, these are pointless:

```
    int x = 1;
    assert(x == 1);

    for(int i = 0; i < 10; i++)
    {
        assert(i >= 0);
        ...
```

There's no way these asserts will fire unless the computer is seriously malfunctioning, so they're basically a waste of time. Concentrate on things that "can't happen" if parts of your program work together as they should, but that you could conceivably miss.

Finally, make sure that the conditions you're asserting are reasonably fast to evaluate. You don't want them bogging down your program. Don't loop through your million-element array asserting a complex condition on every entry just out of paranoia.

In short, assert essential preconditions of your code, with an eye toward things that will cause you pain if not caught early. The goal is to get a leg up on debugging when things start to go wrong.

**Disabling Asserts**  
If you search the web for information about asserts, you'll invariably turn up discussions of how to disable asserts in your release builds. Most assert systems have a way to disable asserts program-wide. For the C `assert` call, setting the `NDEBUG` macro disables it. For the Cocoa assert calls, setting the `NS_BLOCK_ASSERTIONS` macro disables them. There are generally two reasons given for disabling asserts in release builds:

1. Asserts impose a runtime cost that you shouldn't make every user pay. In theory, if you've tested thoroughly, you shouldn't encounter any assertion failures in your release builds anyway.
2. An assertion failure immediately terminates the app, which users don't like. By removing asserts, you give the program a chance to continue functioning in the face of a bug.

However, I am firmly of the opinion that disabling asserts in release builds is a terrible idea. The runtime cost should be negligible, and if it's not, then you should redo your asserts to fix that. As for avoiding app termination, asserts should be written such that a failure always means that something has gone terribly wrong. It is _possible_ that the app will continue functioning in the face of that. It's more likely that it'll crash. It's also possible that it'll keep running, but corrupt your user's data. A clean crash is vastly preferable. No code is free of bugs, and crashing early and obviously when a bug is encountered is much better, even in a release build running on a user's machine. Generating a cleaner crash log will help you debug the failures more quickly.

The example `MAAssert` macro above doesn't have any built-in way to disable it for this reason. If you use a different assert facility, I strongly recommend that you avoid ever turning them off.

**Conclusion**  
Asserts are a valuable tool for producing better code and making bugs easier to find and fix. Asserts should be used anywhere there's a constraint on a value that isn't enforced by the language. My general guideline is that if you document a restriction for callers, you should also assert it in the code. If you ever find yourself writing some code that gets you thinking a lot, and has variables whose values should relate to each other in a certain way not enforced by the language, assert that in the code.

That's it for today. Friday Q&A is driven by reader suggestions as always, so if there's a topic that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com). Come back soon for another exciting article.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-05-03-proper-use-of-asserts.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
