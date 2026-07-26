---
title: 'Friday Q&A 2009-07-10: Type Specifiers in C, Part 3'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-07-10-type-specifiers-in-c-part-3.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bf2df0067155d9b8'
translated: false
---

> 原文：[Friday Q&A 2009-07-10: Type Specifiers in C, Part 3](https://www.mikeash.com/pyblog/friday-qa-2009-07-10-type-specifiers-in-c-part-3.html)　·　mikeash.com Friday Q&A

Posted at 2009-07-10 13:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-07-17: Format Strings Tips and Tricks](https://www.mikeash.com/pyblog/friday-qa-2009-07-17-format-strings-tips-and-tricks.html)  
Previous article: [Friday Q&A 2009-07-03: Type Specifiers in C, Part 2](https://www.mikeash.com/pyblog/friday-qa-2009-07-03-type-specifiers-in-c-part-2.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-07-10: Type Specifiers in C, Part 3

by [Mike Ash](https://www.mikeash.com/)

**Synchronization**  
 Shared data is a big part of what makes multithreaded code so difficult to write. In standard multithreaded code, you must synchronize access to any pieces of shared memory, usually by using a lock.

A key piece of advice: if you're using locks on all of your shared data, you do _not_ need to use `volatile` for anything.

This should give you a big clue as to when `volatile` _is_ useful.

**Lockless Shared Data**  
 What happens when you access shared data without a lock? Unless you're really careful, lots of bad things can happen. Unless your data access is carefully constructed, you can easily end up with inconsistent data. For example, imagine a simple shared counter built like so:

```
    int gCounter;
    void Increment(void) { gCounter++; }
    int GetCurrent(void) { return gCounter; }
```

If multiple threads use `Increment` then this code is not safe! On most systems, `gCounter++` will break down into multiple steps: `

load current value into register
    increment register
    store register into current value

` And those individual steps can be interleaved, so you can end up losing increments due to the overlap.

Note that making `gCounter` be `volatile` does not help in any way.

(If you want to learn more about lockless thread safe data structures, you may want to listen to [my podcast with the Mac Developer Network](http://www.mac-developer-network.com/shows/podcasts/lnc/lnc032/).)

The problems with shared data run deeper than simple interleaving of more basic steps. Let's say that you're allocating a data structure on a thread, and want to flag when it's ready:

```
    struct SharedDataStructure gSharedStructure;
    int gFlag;
```

Then you create it:

```
    gSharedStructure.foo = ...;
    gSharedStructure.bar = ...;
    gSharedStructure.baz = ...;
    gFlag = 1;
```

And then you periodically check for it in another thread:

```
    if(gFlag)
        UseSharedStructure(&gSharedStructure;);
```

This code is broken! Last week we discussed the "as-if" rule: the C compiler doesn't have to generate code that does exactly what you write in the exact order that you wrote it in, but rather it only has to generate code that does "as if" that happened. The standard knows nothing about multithreading, so the possibility that this shared data could be seen by other threads never enters into it: the "as if" rule applies only to threads individually.

Since `gFlag` shares no dependencies with `gSharedStructure`, the compiler is free to reorder all of those assignments. It could assign `gFlag` first, then fill out the structure. Your other thread will then see the flag as set before the structure is initialized, leading to chaos.

Easy to fix! We'll just make `gFlag` be `volatile`. This will force the compiler to make the store happen right on that line. Not so fast! This doesn't fix the problem at all. Yes, it forces the compiler to make the store happen right on that line, but it doesn't force the compiler to do anything about the struct. The C language requires that stores to `volatile` variables happen in order with respect to other `volatile` accesses, but it does _not_ require anything with respect to non-`volatile` variables. Thus the compiler is free to reorder the `gSharedStructure` stores as it wishes across the `volatile` boundary.

Still easy to fix! Just make both of them be `volatile`. This does indeed fix the problem with respect to the C compiler. The stores will be guaranteed to be generated in the proper order....

But no, this doesn't work, you're still doomed!

**CPU Memory Reordering**  
 It turns out that your CPU is playing its own version of the C "as if" game. Your CPU sees a list of instructions but is only required to execute them "as if" they occurred in the proper order. Internally, your CPU will aggressively re-order things to run faster. This could result in some loads or stores occurring in a different order from what the machine code indicates. Normally this is not a problem, because the CPU guarantees that the end result is still "as if" they all happened in the original order.

It becomes a problem when you have multiple CPUs sharing the same memory, as happens when you access shared data without locks on a multi-CPU system (which is most PC-class systems these days). Although everything happens "as if" it were in the original order on one CPU, another CPU will see the true out-of-order memory accesses. If your two threads are running on two different CPUs, then you still have the potential that the reader thread will see `gFlag` as set and not see `gSharedStructure` as initialized, even with `volatile` on both of them.

Easy to fix! I'm actually serious this time. You just insert a call to the `OSMemoryBarrier` function (from `libkern/OSAtomic.h`) in between the two sections to enforce ordering at the hardware level:

```
    gSharedStructure.foo = ...;
    gSharedStructure.bar = ...;
    gSharedStructure.baz = ...;
    OSMemoryBarrier();
    gFlag = 1;
```

And also in the reader:

```
    if(gFlag) {
        OSMemoryBarrier();
        UseSharedStructure(&gSharedStructure;);
    }
```

Now everything works correctly. Ordering is guaranteed at both the software and hardware level.

But there's a twist. At this point, you don't need the `volatile` qualifiers anymore! At least, you _probably_ don't....

**As If!**  
 Once again, the "as if" rule is key to understanding all of this. The compiler has to generate code that works "as if" everything happened as written. The trick is that the compiler can't see all of the code that's running in your process. Much of it is in system libraries. The moment that control jumps to code that the compiler can't see, it must make sure that all of its virtual ducks are in a row, and get all of those values to actually be in memory. For all the compiler knows, that external code may access your data, so it has to ensure that it's stored.

This means that `volatile` is definitely not needed on `gSharedStructure`. The call to `OSMemoryBarrier` in the writer forces the compiler to commit all of those stores to memory before making the call, to ensure that `OSMemoryBarrier` can see the correct values. (It won't look at them, but the compiler cannot know this.) Likewise, the call to `OSMemoryBarrier` in the reader forces the compiler to re-fetch everything from memory, because for all it knows `OSMemoryBarrier` could have modified the values.

What about `gFlag`? This is a bit more complex. Here's an example where it would definitely need to be `volatile`:

```
    while(1) {
        if(gFlag) {
            OSMemoryBarrier();
            UseSharedStructure(&gSharedStructure;);
        }
    }
```

As far as the compiler is concerned, nothing could possibly change `gFlag` as long as it's false, because you never hit any external code. If `gFlag` is not `volatile`, the compiler is free to read `gFlag` once, then use the cached value each time through the loop, so it would never see any change to it. Thus it must be made `volatile` for this code to be correct.

Now here's an example where it has no need to be `volatile`:

```
    - (void)method {
        if(gFlag) {
            OSMemoryBarrier();
            UseSharedStructure(&gSharedStructure;);
        }
    }
```

Here, the compiler must consider the caller to be foreign code, so it will re-read `gFlag` every time.

(Note: this is _largely_ true if this were a function instead of an Objective-C method, but can be false in the face of inlining and whole-program optimization such as is performed by gcc-llvm and clang. Be careful!)

Here is another example where `volatile` is useful:

```
    int gCount;
    ...
    while(!done) {
        work();
        gCount++;
    }
    ...
    while(gCount < total)
        ;
```

As before, the while loop is not guaranteed to work properly unless `gCount` is marked as volatile.

At this point it's important to note that even marking it as `volatile` won't be enough if `gCount` cannot be read or written atomically by your CPU. Whether this is true depends on your individual CPU. General guidelines are that the data must be aligned to a multiple of its size (true of a global, but not always true if you're doing skanky stuff) and that for integers it must be equal to or smaller than the CPU's native size. In other words, if you declared `volatile int64_t gCount` on a 32-bit CPU this code would not necessarily work. Your program could see half-written values, with the top and bottom mismatched, which would not be a good thing.

Finally, you need to be careful with `volatile` because it's a common place to find compiler bugs. The fact that `volatile` is used so rarely and is in conflict with things like the compiler's optimizer makes it a good place for bugs to flourish. A [survey of many popular compilers](http://www.cs.utah.edu/~regehr/papers/emsoft08-preprint.pdf) found that many of them miscompiled `volatile` code a large percentage of the time.

**Conclusion**  
 To break down what we've learned:

1. `volatile` is necessary when reading or writing a shared value in a loop whose body does not touch "foreign" code.
2. `volatile` is _not_ sufficient when doing this on multiple pieces of dependent data when ordering is important. In order for this to work, `OSMemoryBarrier` must be used. Since this is foreign code, this _may_ remove the requirement to use `volatile`, depending on the exact structure of your code.
3. `volatile` does not help in a multithreading context with variables that cannot be atomically written or read by your CPU.
4. `volatile` is neither necessary nor helpful when working with complex shared data protected by locks or using atomic operations.
5. Be wary of using `volatile` even where it's perfectly correct, as you stand a decent chance of encountering a compiler bug which defeats your correct code.

In short, `volatile` can be occasionally useful for certain types of shared data access in a lockless context. However, when in doubt, use locks! Lockless shared data is _extremely_ difficult to get right. I hope that this guide gives you some idea of how `volatile` can help you get it right, and more importantly how it can't help you get it right, but unless you absolutely must not use locks in any way, it's much better to protect your shared data with a lock instead. (And if you can, avoid shared data altogether! Message passing is usually a much nicer way to do multithreading.)

That wraps up this week's Friday Q&A, and also wraps up the three-part series on type qualifiers. Come back next week for another exciting edition. As always, Friday Q&A is powered by your ideas, so please [send them in](mailto:mike@mikeash.com) or post them in the comments below.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-07-10-type-specifiers-in-c-part-3.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
