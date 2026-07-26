---
title: 'Friday Q&A 2014-05-09: When an Autorelease Isn''t'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:66f8dcdbd3b8420e'
translated: false
---

> 原文：[Friday Q&A 2014-05-09: When an Autorelease Isn't](https://www.mikeash.com/pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html)　·　mikeash.com Friday Q&A

Posted at 2014-05-09 13:59 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-05-23: A Heartbleed-Inspired Paranoid Memory Allocator](https://www.mikeash.com/pyblog/friday-qa-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.html)  
Previous article: [Friday Q&A 2014-03-14: Introduction to the Sockets API](https://www.mikeash.com/pyblog/friday-qa-2014-03-14-introduction-to-the-sockets-api.html)  
Tags: [arc](https://www.mikeash.com/pyblog/?tag=arc) [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory)

Friday Q&A 2014-05-09: When an Autorelease Isn't

by [Mike Ash](https://www.mikeash.com/)

**The Setup**  
[ARC](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html) is a lovely technology but it doesn't cover everything. Sometimes you need to use CoreFoundation objects and you're back in the world of manual memory management.

Normally, that's no problem. I did manual memory management for many years, and while I enjoy _not_ doing it with ARC, I still remember how. However, ARC makes some things a bit more difficult than they used to be. In particular, sometimes you want to `autorelease` a CoreFoundation object. Without ARC, you might write something like this:

```
    CFDictionaryRef MakeDictionary(void) {
        CFMutableDictionaryRef dict = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
        // Put some stuff in the dictionary here perhaps

        [(id)dict autorelease];
        return dict;
    }
```

This gives you nice memory management semantics, where the caller is not responsible for releasing the return value, just like we're used to with most Cocoa methods. It takes advantage of the fact that all CoreFoundation objects are also Objective-C objects, and an `autorelease` is a way to balance a CoreFoundation `Create` call.

This code no longer works with ARC, because the call to `autorelease` is not permitted. To solve this, Apple helpfully provided us with a `CFAutorelease` function which does the same thing and can be used with ARC. Unfortunately, it's only available as of iOS 7 and Mac OS X 10.9. For those of us who need to support older OS releases, we have to improvise.

My solution was to get the selector for `autorelease` using the `sel_getUid` runtime call, which sneaks past ARC's rules. Then I'd send that selector to the CoreFoundation object, thus accomplishing the same thing as `[(id)dict autorelease]`. My code looked like this:

```
    CFDictionaryRef MakeDictionary(void) {
        CFMutableDictionaryRef dict = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
        // Put some stuff in the dictionary here perhaps

        SEL autorelease = sel_getUid("autorelease");
        IMP imp = class_getMethodImplementation(object_getClass((__bridge id)dict), autorelease);
        ((id (*)(CFTypeRef, SEL))imp)(dict, autorelease);

        return dict;
    }
```

Note: if you ended up here because you need code to accomplish this, _do not use this code_. As we will see shortly, it's broken. If you want working code for this, check the end of the article.

I tested this code and everything worked fine. A little later, another programmer on the project reported that it was consistently crashing for him. Fortunately, I was able to replicate his crash without too much difficulty. However, it took a while to figure out just what was going on.

**The Crash**  
This code does not crash itself. However, it can _cause_ a crash in subsequent code. For example:

```
    CFDictionaryRef dict = MakeDictionary();
    NSLog(@"Testing.");
    NSLog(@"%@", dict);
```

This crashes on the second `NSLog` line. The stack trace looks like a typical memory management crash:

```
    frame #0: 0x00007fff917980a3 libobjc.A.dylib`objc_msgSend + 35
    frame #1: 0x00007fff97175184 Foundation`_NSDescriptionWithLocaleFunc + 41
    frame #2: 0x00007fff9077bd94 CoreFoundation`__CFStringAppendFormatCore + 7332
    frame #3: 0x00007fff907aa313 CoreFoundation`_CFStringCreateWithFormatAndArgumentsAux + 115
    frame #4: 0x00007fff907e1b9b CoreFoundation`_CFLogvEx + 123
    frame #5: 0x00007fff9719ed0c Foundation`NSLogv + 79
    frame #6: 0x00007fff9719ec98 Foundation`NSLog + 148
```

It seems that the dictionary is being destroyed before the `NSLog` call. But how can that be? We called `autorelease` in the function, and the autorelease pool has not yet been drained. The `release` that will balance the CoreFoundation `Create` call hasn't happened yet, so the object should still exist.

**The Assembly**  
After poking at the code in various ways, I decided to read the assembly code generated by the compiler. There wasn't much to the code I wrote, so whatever problem there was must have been deeper.

Here's the x86-64 assembly output for the broken `MakeDictionary` function:

```
    _MakeDictionary:                        ## @MakeDictionary
        .cfi_startproc
    Lfunc_begin0:
        .loc    1 11 0                  ## test.m:11:0
    ## BB#0:
        pushq   %rbp
    Ltmp2:
        .cfi_def_cfa_offset 16
    Ltmp3:
        .cfi_offset %rbp, -16
        movq    %rsp, %rbp
    Ltmp4:
        .cfi_def_cfa_register %rbp
        subq    $32, %rsp
        movabsq $0, %rax
        .loc    1 12 0 prologue_end     ## test.m:12:0
    Ltmp5:
        movq    %rax, %rdi
        movq    %rax, %rsi
        movq    %rax, %rdx
        movq    %rax, %rcx
        callq   _CFDictionaryCreateMutable
        leaq    L_.str(%rip), %rdi
        movq    %rax, -8(%rbp)
        .loc    1 15 0                  ## test.m:15:0
        callq   _sel_getUid
        movq    %rax, -16(%rbp)
        .loc    1 16 0                  ## test.m:16:0
        movq    -8(%rbp), %rax
        movq    %rax, %rdi
        callq   _object_getClass
        movq    -16(%rbp), %rsi
        movq    %rax, %rdi
        callq   _class_getMethodImplementation
        movq    %rax, -24(%rbp)
        .loc    1 17 0                  ## test.m:17:0
        movq    -24(%rbp), %rax
        movq    -8(%rbp), %rcx
        movq    -16(%rbp), %rsi
        movq    %rcx, %rdi
        callq   *%rax
        movq    %rax, %rdi
        callq   _objc_retainAutoreleasedReturnValue
        movq    %rax, %rdi
        callq   _objc_release
        .loc    1 19 0                  ## test.m:19:0
        movq    -8(%rbp), %rax
        addq    $32, %rsp
        popq    %rbp
        ret
```

Pretty straightforward here. Since no real calculations are done, we can just look at the sequence of `callq` instructions to see what functions are called. It calls `CFDictionaryCreateMutable`, `sel_getUid`, `object_getClass`, `class_getMethodImplementation`, and then there's an indirect call through the function pointer which is where it actually makes the `autorelease` call. ARC then hops in and does some pointless but harmless work on the return value from the call by retaining it and then immediately releasing it. The function then returns the dictionary to the caller.

**Mostly Harmless**  
It took me a little while to realize what was going on, but then it was obvious. I said that the ARC calls inserted are "pointless but harmless." In fact, they are anything but!

One of the interesting features that came with ARC is fast handling of autoreleased return values. This sort of pattern is extremely common with ARC:

```
    // callee
    obj = [[SomeClass alloc] init];
    [obj setup];
    return [obj autorelease];

    // caller
    obj = [[self method] retain];
    [obj doStuff];
    [obj release];
```

A human programmer would typically omit the `retain` and `release` calls in the caller, but ARC is more paranoid. This would make things a bit slower when using ARC, which is where the fast autorelease handling comes in.

There is some extremely fancy and mind-bending code in the Objective-C runtime's implementation of `autorelease`. Before actually sending an `autorelease` message, it first inspects the caller's code. If it sees that the caller is going to immediately call `objc_retainAutoreleasedReturnValue`, it _completely skips the message send_. It doesn't actually do an `autorelease` at all. Instead, it just stashes the object in a known location, which signals that it hasn't sent `autorelease` at all.

`objc_retainAutoreleasedReturnValue` cooperates in this scheme. Before calling `retain`, it first checks that known location. If it contains the right object, it skips the retain. The net result is that the above code is effectively transformed into this:

```
    // callee
    obj = [[SomeClass alloc] init];
    [obj setup];
    return obj;

    // caller
    obj = [self method];
    [obj doStuff];
    [obj release];
```

This is faster because it skips the autorelease pool entirely, saving three message sends and the accompanying work: `autorelease`, the caller's `retain`, and the eventual `release` sent by the autorelease pool. It also allows the object to be destroyed earlier, reducing memory and cache pressure.

The beautiful thing about this technique is that because the runtime checks the caller's code before making this optimization, everything is perfectly compatible with code that doesn't participate in the scheme. If the caller does something else with the return value, then the runtime simply calls `autorelease` and everything works normally.

I said that this code is _not_ pointless. What, then, is the point of the `retain` immediately followed by `release` in the assembly above? It allows the caller to participate in this scheme even though it's not using the return value. It would be correct to simply omit them, but in that case, the fast `autorelease` path is lost. It ends up being faster to make these two extra calls, at least in the common case.

I also said that this code is not harmless. The harm here is exactly that fast autorelease path. To ARC, an `autorelease` in a function or method followed by a `retain` in the caller is just a way to pass ownership around. However, that's not what's going on in this code. This code is attempting to _actually_ put the object into the autorelease pool no matter what. ARC's clever optimization ends up bypassing that attempt and as a result, the dictionary is immediately destroyed instead of being placed in the autorelease pool for later destruction.

**Root Cause**  
It all comes down to the function pointer cast used when making the `autorelease` call:

```
    ((id (*)(CFTypeRef, SEL))imp)(dict, autorelease);
```

I wrote it like this because that's what the type is. The `autorelease` method returns `id` and takes two (normally implicit) parameters: `self` and the selector being sent. I changed the `self` parameter to `CFTypeRef` instead of `id` for convenience, but left the return type as `id` since that's what it really is in the underlying `autorelease` method. It shouldn't matter, since the return value is ignored anyway.

That return type is this code's downfall. I was careful to avoid ARC's meddling for the most part, but that `id` makes ARC come in and start inserting calls, and that causes the dictionary to be immediately destroyed.

**The Fix**  
Once all of this is known, the fix is easy. Get ARC out of the picture by having the call return `CFTypeRef` instead of `id`. Here's the complete function with the fix:

```
    CFDictionaryRef MakeDictionary(void) {
        CFMutableDictionaryRef dict = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
        // Put some stuff in the dictionary here perhaps

        SEL autorelease = sel_getUid("autorelease");
        IMP imp = class_getMethodImplementation(object_getClass((__bridge id)dict), autorelease);
        ((CFTypeRef (*)(CFTypeRef, SEL))imp)(dict, autorelease);

        return dict;
    }
```

Dumping the assembly shows that ARC is now out of the picture:

```
    _MakeDictionary:                        ## @MakeDictionary
        .cfi_startproc
    Lfunc_begin0:
        .loc    1 11 0                  ## test.m:11:0
    ## BB#0:
        pushq   %rbp
    Ltmp2:
        .cfi_def_cfa_offset 16
    Ltmp3:
        .cfi_offset %rbp, -16
        movq    %rsp, %rbp
    Ltmp4:
        .cfi_def_cfa_register %rbp
        subq    $32, %rsp
        movabsq $0, %rax
        .loc    1 12 0 prologue_end     ## test.m:12:0
    Ltmp5:
        movq    %rax, %rdi
        movq    %rax, %rsi
        movq    %rax, %rdx
        movq    %rax, %rcx
        callq   _CFDictionaryCreateMutable
        leaq    L_.str(%rip), %rdi
        movq    %rax, -8(%rbp)
        .loc    1 15 0                  ## test.m:15:0
        callq   _sel_getUid
        movq    %rax, -16(%rbp)
        .loc    1 16 0                  ## test.m:16:0
        movq    -8(%rbp), %rax
        movq    %rax, %rdi
        callq   _object_getClass
        movq    -16(%rbp), %rsi
        movq    %rax, %rdi
        callq   _class_getMethodImplementation
        movq    %rax, -24(%rbp)
        .loc    1 17 0                  ## test.m:17:0
        movq    -24(%rbp), %rax
        movq    -8(%rbp), %rcx
        movq    -16(%rbp), %rsi
        movq    %rcx, %rdi
        callq   *%rax
        .loc    1 19 0                  ## test.m:19:0
        movq    -8(%rbp), %rcx
        movq    %rax, -32(%rbp)         ## 8-byte Spill
        movq    %rcx, %rax
        addq    $32, %rsp
        popq    %rbp
        ret
```

**Architectures**  
One question remains: why did this code work for me initially, and my colleage only uncovered the crash later?

The answer is actually pretty simple, once everything else is known. This is an iOS project. I tested the code in the simulator, while he tried it on a real iPhone. The runtime function that performs the fast autorelease check is called `callerAcceptsFastAutorelease`. It's architecture-specific since it's inspecting machine code. If you look at the version used in the 32-bit iOS simulator, the problem becomes apparent:

```
    # elif __i386__  &&  TARGET_IPHONE_SIMULATOR

    static bool callerAcceptsFastAutorelease(const void *ra)
    {
        return false;
    }
```

In short, the fast autorelease handling is not implemented for the 32-bit iOS simulator. It makes sense that it wouldn't be. It's going to be some non-trivial amount of effort to implement and fix. Meanwhile, ARC is not supported on `i386` for Mac programs, so the only way to hit this path on `i386` is to run in the simulator. There's no real point in putting effort into extreme optimizations that will only apply to simulator apps.

**Aside**  
Before writing this article, I first wrote a small test case so I could easily experiment and examine the problem in isolation. However, there was a big problem: the test case didn't work! Or rather, it _did_ work just fine, and refused to crash. The code was really simple, roughly:

```
    int main(int argc, char **argv)
    {
        @autoreleasepool {
            CFDictionaryRef dict = MakeDictionary();
            NSLog(@"Testing.");
            NSLog(@"%@", dict);
        } 
        return 0;
    }
```

There isn't much room for error there, so it was baffling why it wouldn't crash.

After many single-steps through assembly in the debugger, I realized that it had to do with `dyld` lazy binding. References to external functions aren't fully bound when a program is initially loaded. Instead, a stub is generated which has enough information to complete the binding the first time the call is made. On the first call to an external function, the address for that function is looked up, the stub is rewritten to point to it, and then the function call is made. Subsequent calls go directly to the function. By binding lazily, program startup time is improved and time isn't wasted looking up functions that are never called.

That means that on the very first run of this code, the call to `objc_retainAutoreleasedReturnValue` isn't fully bound. Because it's not fully bound, `callerAcceptsFastAutorelease` doesn't realize that the call is to `objc_retainAutoreleasedReturnValue`. Because it doesn't see the call to `objc_retainAutoreleasedReturnValue`, the fast autorelease path isn't used. The dictionary goes into the autorelease pool as was originally intended, and the code works... once.

Once I figured _that_ out, it was trivial to force the crash by inserting a loop:

```
    int main(int argc, char **argv)
    {
        while(1) @autoreleasepool {
            CFDictionaryRef dict = MakeDictionary();
            NSLog(@"Testing.");
            NSLog(@"%@", dict);
        } 
        return 0;
    }
```

The loop reliably crashes on the second iteration. The first time through triggers lazy binding of `objc_retainAutoreleasedReturnValue`, which then allows the next call to take the fast autorelease path and trigger the bug.

This has little consequence for normal programs, which will perform the lazy binding for functions like these early on. It ended up being a severe complicating factor for a small test program, though.

**Conclusion**  
ARC is great technology, but sometimes it's necessary to work around it. When working around it, you have to be sure you _really_ work around it, and not give it any opportunity to jump in. If you do, it might decide to eliminate what looks like a useless autorelease call, causing your objects to be instantaneously destroyed instead of being peacefully returned to the caller.

People sometimes ask me if I actually use the crazy and esoteric stuff I discuss on this blog. This is a good example: it took basic assembly language reading, Objective-C runtime internals, and understanding of specific ARC calls to track down this bug. Building the example crasher further required understanding how `dyld` binds external function references at runtime. This is all great stuff to know, and even if you never use it, it's just plain fun.

That's it for today. I hope to be back on track, so check back soon for another article. In the meantime, as always, Friday Q&A is driven by reader suggestions, so if you have a topic that you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
