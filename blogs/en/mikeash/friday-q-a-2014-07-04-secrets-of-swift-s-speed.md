---
title: 'Friday Q&A 2014-07-04: Secrets of Swift''s Speed'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-07-04-secrets-of-swifts-speed.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:665def1a5f30f1e3'
translated: false
---

> 原文：[Friday Q&A 2014-07-04: Secrets of Swift's Speed](https://www.mikeash.com/pyblog/friday-qa-2014-07-04-secrets-of-swifts-speed.html)　·　mikeash.com Friday Q&A

Posted at 2014-07-04 13:40 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-07-18: Exploring Swift Memory Layout](https://www.mikeash.com/pyblog/friday-qa-2014-07-18-exploring-swift-memory-layout.html)  
Previous article: [Friday Q&A 2014-06-20: Interesting Swift Features](https://www.mikeash.com/pyblog/friday-qa-2014-06-20-interesting-swift-features.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [optimization](https://www.mikeash.com/pyblog/?tag=optimization) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2014-07-04: Secrets of Swift's Speed

by [Mike Ash](https://www.mikeash.com/)

**Speculation**  
While the language should allow for great performance, the current compiler is still a bit rough, and I've had a hard time getting Swift to come out ahead in any performance tests. Most of the slowness looks to come down to a lot of redundant retain/release activity being emitted by the compiler. I expect this to be fixed before too long, but in the meantime, it means that this article is going to be more about how Swift could potentially be faster than Objective-C than about how it's actually faster right now.

**Faster Method Dispatch**  
As we all know by now, every time we write an Objective-C method call, it gets translated into a call to `objc_msgSend` which then handles the work of looking up the target method at runtime and invoking it. `objc_msgSend` is responsible for taking the selector you're sending and the object you're sending it to, and looking that up in the class method tables to figure out exactly which piece of code is supposed to handle it. It's extremely fast for what it does, but it does a lot more than is usually necessary.

Message sending is nifty because it makes no assumption about the runtime type of the target object. It could be an instance of the expression's static type; if you're sending a message to a variable declared `NSView *`, the object could very well be a straight `NSView` instance. It could also be a subclass. It could even be an instance of a completely unrelated class. You can lie to the compiler about an object's type and everything still works fine.

However, in 99.999% of Objective-C code, you don't lie to the compiler. When an object is declared `NSView *`, it really is either an `NSView` or a subclass. We need some dynamic dispatch, but the vast majority of code doesn't need the full message send dispatch. However, the nature of Objective-C is such that every call has to pay the full cost.

Consider this Swift code:

```
    class Class {
        func testmethod1() { print("testmethod1") }
        @final func testmethod2() { print("testmethod2") }
    }

    class Subclass: Class {
        override func testmethod1() { print("overridden testmethod1") }
    }

    func TestFunc(obj: Class) {
        obj.testmethod1()
        obj.testmethod2()
    }
```

In the equivalent Objective-C code, both method calls would be compiled to `objc_msgSend` calls and that would be the end of the story.

In Swift, the compiler is able to take advantage of the tighter guarantees provided by the language. In Objective-C, we can lie to the compiler, and the object may not be anything like the type we say it is. In Swift, we can't lie to the compiler. If we say that `obj` is an instance of `Class`, then it's either an instance of that class or of a subclass.

Instead of `objc_msgSend`, the Swift compiler emits code that makes a call using a vtable. A vtable is just an array of function pointers, accessed by index. That array exists as part of the class. The code emitted by the compiler for the first method call is roughly equivalent to:

```
    methodImplementation = object->class.vtable[indexOfMethod1]
    methodImplementation()
```

A simple array index is quite a bit faster than `objc_msgSend`, even with its fancy caching and finely tuned assembly code, so this is a nice performance win.

The call to `testmethod2` is even nicer. Because it's declared `@final`, the compiler knows that nothing can override it. No matter what happens, the call will always go to the implementation in `Class`. Thus the compiler doesn't even need to emit a vtable lookup. It can just make a normal function call that goes straight to `__TFC9speedtest5Class11testmethod2fS0_FT_T_`, which is the mangled name of the testmethod2 implementation in my test case.

This isn't a _huge_ win. `objc_msgSend` really is remarkably fast, and most programs don't spend that much time in it. In addition, Swift will still use `objc_msgSend` to send messages to Objective-C objects. Still, it should be good for a few percentage points.

**More Intelligent Method Calls**  
The different method call semantics allow speed improvements beyond simply using faster dispatch techniques. Because the compiler can better understand where control goes, it can optimize the code better. It can potentially inline method calls or even eliminate them entirely.

In the above exmple, I deleted the body of `testmethod2`:

```
    @final func testmethod2() {}
```

The compiler is smart enough to see that the call to this method now does nothing. With optimizations turned on, it doesn't even emit the call. It calls `testmethod1` and then it's done.

It can do this even with methods that aren't marked `@final` if it has enough information locally. For example, consider a slight variation on the above code:

```
    let obj = Class()
    obj.testmethod1()
    obj.testmethod2()
```

Since the compiler can see the creation of `obj`, it knows that it's an instance of `Class` and not a subclass. This allows it to completely eliminate the dynamic dispatch even for `testmethod1`, making a direct function call to the implementation.

To take an extreme case, consider code like this:

```
    for i in 0..1000000 {
        obj.testmethod2()
    }
```

In Objective-C, this code will send a million messages and take a noticeable amount of time to run. In Swift, if the compiler can see that `testmethod2` does nothing, it could potentially eliminate the entire loop, meaning that this code runs in zero time.

**Less Memory Allocation**  
If enough information is available to the compiler, it could potentially eliminate some memory allocations altogether. In code like the above, if the compiler can see the object creation and all uses and determine that the object never lives beyond the local scope, the compiler could skip heap allocation for the object and allocate it on the stack instead, which is much faster. In an extreme case, where the methods invoked on the object never actually use the object, it could skip the allocation altogether. Consider some ridiculous Objective-C code like this:

```
    for(int i = 0; i < 1000000; i++)
        [[[NSObject alloc] init] self];
```

This will send three million messages and allocate and destroy one million objects. The equivalent Swift code could, with a smart compiler, compile to nothing at all if it's able to determine that the `self` method doesn't do anything useful and doesn't cause anything to refer to the object beyond its local lifetime.

**More Efficient Register Usage**  
Every Objective-C method takes two implicit parameters: `self` and `_cmd`, with the explicit parameters passed after those two. On most architectures (including x86-64, ARM, and ARM64), the first few parameters to a function are passed in registers, with the rest passed on the stack. Registers are much faster than stack, so passing parameters in registers can be a big performance win.

The implicit `_cmd` parameter is rarely needed. It's really only useful when taking advantage of fully dynamic message sending, which 99.999% of Objective-C code doesn't do. Yet it occupies a scarce parameter register in all calls, leaving one fewer for real parameters. There aren't many available: ARM only uses four registers for passing parameters, x86-64 uses six, and ARM64 uses eight.

Swift omits the `_cmd` parameter, freeing up an additional argument register for more useful purposes. For methods that take several explicit parameters (three or more for ARM, five or more for x86-64, and seven or more for ARM64), this means a small performance win on every call due to better use of argument registers.

**Aliasing**  
These are all reasons why Swift can be faster than Objective-C, but how about plain C? Aliasing is something that could allow Swift to surpass C.

Aliasing is when you have more than one pointer to the same chunk of memory. For example:

```
    int *ptrA = malloc(100 * sizeof(*ptrA));
    int *ptrB = ptrA;
```

This is a tricky situation, because writing to `ptrA` will affect reads from `ptrB`, and vice versa. This can hurt the compiler's ability to optimize.

Consider a simple implementation of the standard library `memcpy` function:

```
    void *mikememcpy(void *dst, const void *src, size_t n) {
        char *dstBytes = dst;
        const char *srcBytes = src;

        for(size_t i = 0; i < n; i++)
            dstBytes[i] = srcBytes[i];

        return dst;
    }
```

Copying one byte at a time is pretty inefficient. We'd generally want to copy larger chunks. SIMD instructions may allow copying 16 or even 32 bytes at a time, which would make this go much faster. In theory, the compiler should be able to analyze this loop and do that for us. However, aliasing stops that from happening. To understand why, consider this code:

```
    char *src = strdup("hello, world");
    char *dst = src + 1;
    mikememcpy(dst, src, strlen(dst));
```

With `memcpy`, this wouldn't be legal. It's not allowed to pass overlapping pointers like this. However, this is `mikememcpy`, which accepts overlapping pointers, but it behaves strangely.

In the first iteration of the copy loop, `srcBytes[i]` refers to the `'h'` and `dstBytes[i]` refers to the `'e'`. After copying this byte, the full string then contains `"hhllo, world"`. In the second iteration, `srcBytes[i]` refers to the second `'h'`, and `dstBytes[i]` refers to the first `'l'`. The full string after this iteration is `"hhhlo, world"`. It continues like this, with the `'h'` being copied forward byte by byte, until the full string is simply `"hhhhhhhhhhhh"`. Not really what we wanted.

This sort of thing is why `memcpy` doesn't allow overlapping pointers. The `memmove` function is smart enough to handle overlapping copies like this, at the cost of some performance. By ignoring potential overlap, `memcpy` can go faster.

However, the compiler doesn't understand all of this context. It doesn't know that `mikememcpy` is supposed to assume that the arguments don't overlap. We'd be happy with any optimization that changed the semantics of the case where the arguments overlap, as long as it kept the non-overlapping case intact. For all the compiler knows, we _want_ `"hhhhhhhhhhhh"`. We _need_ it. The code we wrote _demands_ it. Any optimization has to keep these semantics intact, even though we don't care. This makes it tough to make this function more efficient by copying larger chunks of memory.

`clang` actually does an impressive job with this function. It generates code which checks for overlap and performs optimized copies when the two pointers don't overlap. The performance penalty from the compiler's lack of context ends up being small, but not zero. Those extra checks aren't entirely free.

This is a pervasive problem in C, because the language allows any two pointers of the same type (and sometimes of different types!) to alias. Most code is written with the assumption that pointers don't alias, but the compiler generally has to assume that they might. This makes C much harder to optimize, and can make C programs slower than they need to be.

It's such a common problem that the C99 standard introduced a new keyword just to deal with it. The `restrict` keyword tells the compiler that a given pointer won't alias, allowing for better optimizations. Adding it to `mikememcpy`'s parameters produces better code:

```
    void *mikememcpy(void * restrict dst, const void * restrict src, size_t n) {
        char *dstBytes = dst;
        const char *srcBytes = src;

        for(size_t i = 0; i < n; i++)
            dstBytes[i] = srcBytes[i];

        return dst;
    }
```

Problem solved, right? Well, how often have you actually added the `restrict` keyword to your code? I'm going to guess "never" for most of you. In my case, the first time I ever actually used `restrict` was when I wrote the modified `mikememcpy` above. It gets used for extremely performance sensivite code, but otherwise we just take the minor hit and move on.

It can show up in a lot of places you might not expect, too. For example:

```
    - (int)zero {
        _count++;
        memset(_ptr, 0, _size);
        return _count;
    }
```

As far as the compiler knows, `_ptr` could point to `_count`. Thus, it generates code which loads `_count`, increments it, stores it, calls `memset`, then loads `count` _again_ to return it. If we know that `_ptr` doesn't point to `_count` then this is wasted effort, but the compiler has to do it just in case. Compare with:

```
    - (int)zero {
        memset(_ptr, 0, _size);
        _count++;
        return _count;
    }
```

Putting the `memset` first eliminates the redundant load of `_count`. It's a small win, but it's there.

Even something as innocent as an `NSError **` parameter can hit this case. Imagine a counting method that never returns an error, but the API is designed to take one just in case the underlying implementation gets more complex:

```
    - (int)increment: (NSError **)outError {
        _count++;
        *outError = nil;
        return _count;
    }
```

Once again, the compiler generates a redundant load of `_count` just in case `outError` points to it. This is an odd case, because C's aliasing rules don't allow aliasing pointers of different types, and so it should actually be safe to omit the redundant load. I assume that something about how the Objective-C type rules are implemented on top of C is defeating that. We could add `restrict`:

```
    - (int)increment: (NSError ** restrict)outError {
        _count++;
        *outError = nil;
        return _count;
    }
```

This generates better code. But how often do you really do that? For me, this is now the second time I have ever used this keyword.

Swift code encounters these situations much less frequently. In general, you don't take references to arbitrary instance variables, and array semantics make it impossible for them to overlap. This should allow the Swift compiler to generate better code in general, with fewer redundant loads and stores to handle the case where you _might_ alias something.

**Conclusion**  
Swift has a couple of tricks that can potentially make for faster programs than Objective-C. Less dynamic dispatch allows for faster method calls. It also allows for better optimization of the code that makes those calls, such as inlining or removing calls altogether. The way method dispatch works also frees up an extra argument register, making it faster to pass parameters into methods that take a large number of parameters. Finally, the rarity of pointers in Swift means that aliasing is much less of a problem, allowing the compiler to perform better optimizations and fewer redundant loads and stores. It remains to be seen exactly how much of a difference all of this will make in practice, but it looks promising for modest speed gains.

That's all for today. Come back next time for more Swifty goodness. In the meantime, if there's a topic you'd like to see covered (Swift or not), please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-07-04-secrets-of-swifts-speed.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
