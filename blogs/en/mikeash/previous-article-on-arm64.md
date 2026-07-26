---
title: previous article on ARM64
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-09-27-arm64-and-you.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dfce404dfd8cd5db'
translated: false
---

> 原文：[previous article on ARM64](https://www.mikeash.com/pyblog/friday-qa-2013-09-27-arm64-and-you.html)　·　mikeash.com Friday Q&A

Posted at 2013-09-27 13:31 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-10-11: Why Registers Are Fast and RAM Is Slow](https://www.mikeash.com/pyblog/friday-qa-2013-10-11-why-registers-are-fast-and-ram-is-slow.html)  
Previous article: [Friday Q&A 2013-09-13: A Library for Easier Property List Type Checking and Error Reporting](https://www.mikeash.com/pyblog/friday-qa-2013-09-13-a-library-for-easier-property-list-type-checking-and-error-reporting.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hardware](https://www.mikeash.com/pyblog/?tag=hardware) [iphone](https://www.mikeash.com/pyblog/?tag=iphone)

Friday Q&A 2013-09-27: ARM64 and You

by [Mike Ash](https://www.mikeash.com/)

**"64-bit"**  
Let's start by talking about the general term "64-bit" and what it means. There's a lot of confusion around this term, and a lot of that is because there's no single agreed-upon definition of it. However, there is _generally_ some consensus about it, even if it's not universal.

There are two parts of the CPU that "X-bit" usually refers to: the width of the integer registers, and the width of pointers. Thankfully, in most modern CPUs, these widths are the same. "64-bit" then typically means that the CPU has 64-bit integer registers and 64-bit pointers.

It's also important to point out the things that "64-bit" does _not_ refer to, as there's a lot of confusion in this area as well. In particular, "64-bit" does not include:

1. Physical RAM address size. The number of bits used to actually talk to RAM (and therefore the amount of RAM the hardware can support) is decoupled from the question of CPU bitness. ARM CPUs have ranged from 26 bits to 40 bits, and this can be changed independently from the rest.
2. Data bus size. The amount of data fetched from RAM or cache is likewise decoupled. Individual CPU instructions may request a certain amount of data, but the amount of data actually fetched can be independent, either by splitting the fetch into smaller parts, or fetching more than is necessary. The iPhone 5 already fetches data from memory in 64-bit chunks, and chunk sizes of up to 192 bits exist in the PC world.
3. Anything related to floating-point. FPU register size and internal design is independent, and ARM CPUs have had 64-bit FPU registers since well before ARM64.

**Generic Advantages and Disadvantages**  
If we compare otherwise-identical 32-bit and 64-bit CPUs, there isn't a whole lot of difference, which is a big part of the confusion around the significance of Apple's move to 64-bit ARM. The move is important, but largely because of specifics of the ARM processor and Apple's use of it.

Still, there are some differences. Perhaps the most obvious is that 64-bit integer registers make it more efficient to work with 64-bit integers. You can still work with 64-bit integers on a 32-bit processor, but it typically entails working with it in two 32-bit pieces, which means that arithmetic can take substantially longer. 64-bit CPUs can typically perform arithmetic on 64-bit quantities just as fast as on 32-bit quantities, so code that does heavy manipulation of 64-bit integers will run much faster.

Although 64-bit has no bearing on the amount of RAM that can be used by the CPU itself, it can make it much easier to use large amounts of RAM within a single program. A single program running on a 32-bit CPU only has 4GB of address space. Chunks of that address space are taken up by the operating system and standard libraries and such, typically leaving anywhere from 1-3GB available for use. If a 32-bit system has more than 4GB of RAM, taking advantage of all of it from a single program is tough. You have to resort to shenanigans like asking the operating system to map chunks of memory in and out of your process as you need them, or splitting your program into multiple processes.

This takes a lot of extra programming effort and can slow things down, so few programs actually do it. In practice, a 32-bit CPU limits individual programs to using 1-3GB of RAM each, and the advantage of having more RAM is the ability to run multiple such programs simultaneously, and the ability to cache more data from disk. This is still useful, but there are cases where the ability of a single program to use more RAM is needed.

The increased address space is also useful even on a system without that much RAM. Memory-mapped files are a handy construct, where the contents of a file are logically mapped into a process's memory space, even though physical RAM is not necessarily allocated for the entire file. On a 32-bit system, a program can't memory map large files (over, say, a few hundred megabytes) reliably. On a 64-bit system, the available address space is much larger, so there's no concern with running out.

The increased pointer size comes with a substantial downside: otherwise-identical programs will use more memory, perhaps a lot more, when running on a 64-bit CPU. Pointers have to be stored in memory as well, and each pointer takes twice the amount of memory. Pointers are really common in most programs, so that can make a substantial difference. Increased memory usage can put more pressure on caches, causing reduced performance.

In short: 64-bit can increase performance for certain types of code, and makes certain programming techniques, like memory mapped files, more viable. However, it can also decrease performance due to increased memory usage.

**ARM64**  
The iPhone 5S's 64-bit CPU is not merely a regular ARM processor with wider registers. The 64-bit ARM architecture includes substantial changes from the 32-bit version.

First, a note on the name: the official name from ARM is "AArch64", but this is a silly name that pains me to type. Apple calls it ARM64, and that's what I will call it too.

ARM64 doubles the number of integer registers over 32-bit ARM. 32-bit ARM provides 16 integer registers, of which one is a dedicated program counter, two more are given over to a stack pointer and link register, and the other 13 are available for general use. With ARM64, there are 32 integer registers, with a dedicated zero register, link register, and frame pointer register. One further register is reserved for the platform, leaving 28 general purpose integer registers.

ARM64 also increases the number of floating-point registers available. The floating point registers on 32-bit ARM are a bit odd, so it's tough to compare. It has 32 32-bit floating point registers which can also be viewed as 16 overlapped 64-bit registers, and there are 16 additional independent 64-bit registers. The 32 total 64-bit registers registers can also be viewed as 16 overlapped 128-bit registers. ARM64 simplifies this to 32 128-bit registers, which can also be used for smaller data types, and there's no overlapping.

The register count can strongly influence performance. Memory is extremely slow compared to CPUs, and reading from and writing to memory takes a long time compared to how long it takes the CPU to process an instruction. CPUs try to hide this with layers of caches, but even the fastest layer of cache is slow compared to internal CPU registers. More registers means more data can be kept purely CPU-internal, reducing memory accesses and increasing performance.

Just how much of a difference this makes will depend on the specific code in question, as well as how good the compiler is at optimizing it to make the best use of available registers. When the Intel architecture moved from 32-bit to 64-bit, the number of registers was doubled from 8 to 16, and this made for a substantial performance improvement. ARM already had substantially more registers than the 32-bit Intel architecture, so the impact of additional registers is smaller, but it's a still helpful change.

ARM64 also brings some significant changes to the instruction set beyond the increased number of registers.

Most 32-bit ARM can be executed conditionally based on the state of a condition register at the time of execution. This allows compiling `if` statements and similar without requiring branching. Intended to increase performance, it must have been causing more trouble than it was worth, as ARM64 eliminates conditional execution.

ARM64's NEON SIMD unit provides full double-precision IEEE754 compliance, whereas the 32-bit version of NEON only supports single-precision, and leaves out some of the harder, more obscure bits of IEEE754.

ARM64 adds specialized instructions for AES encryption and SHA-1 and SHA-256 cryptographic hashes. Not important in general, but potentially a big win if you happen to be doing those things.

Overall, by far the most important changes are the greatly increased number of general-purpose registers, and support for full IEEE754-compliant double-precision arithmetic in NEON. These changes could allow for considerable performance increases in a lot of code.

**32-bit Compatibility**  
It's important to note that the A7 includes a full 32-bit compatibility mode that allows running normal 32-bit ARM code without any changes and without emulation. This means that the iPhone 5S runs old iPhone apps with no problem and no performance impact compared to other hardware. 32-bit code does potentially run with somewhat reduced performance since it gets none of the advantages of ARM64.

**Apple Runtime Changes**  
Apple takes advantage of architecture changes like this to make changes in their own libraries. Since they don't need to worry about maintaining binary compatibility across such a change, it's a good time to make changes that would otherwise break existing apps.

In Mac OS X 10.7, Apple introduced [tagged pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html). Tagged pointers allow certain classes with small amounts of per-instance data to be stored entirely within the pointer. This can eliminate the need for memory allocations for many uses of classes like `NSNumber`, and can make for a good performance boost. Tagged pointers were only supported on 64-bit, partly due to binary compatibility concerns, but partly because 32-bit pointers don't leave a lot of room left over for actual data once the tag bits are accounted for. Presumably because of that, iOS never got tagged pointers. However, on ARM64, the Objective-C runtime includes tagged pointers, with all of the same benefits they've brought to the Mac.

Although pointers are 64 bits, not all of those bits are really used. Mac OS X on x86-64, for example, only uses 47 bits of a pointer. iOS on ARM64 uses even less, with only 33 bits of a pointer currently being used. As long as the extra bits are masked off before the pointer is used, they can be used to store other data. This leads to one of the most significant internal changes in the Objective-C runtime in the language's history.

**Repurposed `isa` Pointer**  
Much of the information for this section comes from [Greg Parker's article on the relevant changes](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html). Check that out for information straight from the source.

First, a quick refresher: Objective-C objects are contiguous chunks of memory. The first pointer-sized piece of that memory is the `isa`. Traditionally, the `isa` is a pointer to the object`s class. For more information on how objects are laid out in memory, see [my article on the Objective-C runtime](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html).

Using an entire pointer-sized piece of memory for the `isa` pointer is a bit wasteful, especially on 64-bit CPUs which don't use all 64 bits of a pointer. ARM64 running iOS currently uses only 33 bits of a pointer, leaving 31 bits for other purposes. Class pointers are also aligned, meaning that a class pointer is guaranteed to be divisible by `8`, which frees up another three bits, leaving 34 bits of the `isa` available for other uses. Apple's ARM64 runtime takes advantage of this for some great performance improvements.

Probably the most important performance improvement is an inline reference count. Nearly all Objective-C objects are reference counted (the exceptions being constant objects like `NSString` literals) and `retain`/`release` operations to modify the reference count happen extremely frequently. This is especially true with ARC, which emits even more `retain`/`release` calls than a typical human programmer. As such, high performance for `retain` and `release` is critical.

Traditionally, the reference count is not stored in the object itself. If the `isa` is the only field every object shares, then there's simply no room for any additional data. It would be possible to make it so that every object also contains a reference count field, but this would use up a great deal more memory. This is less important today, but it was a pretty big deal in the earlier days of Objective-C. Because of this, the retain count is stored in an external table.

Any time an object is retained, the runtime goes through this procedure:

1. Fetch a global retain count hash table.
2. Lock the table to make the operation thread safe.
3. Look up the retain count of the object in the table.
4. Increment the count and store the new value back in the table.
5. Release the table lock.

This is a bit slow! The hash table implementation used for tracking retain counts is fast, for a hash table, but even the best hash tables are slow compared to direct memory access.

On ARM64, 19 bits of the `isa` field go to holding the object's reference count inline. That means that the procedure for retaining an object simplifies to:

1. Perform an atomic increment of the correct portion of the `isa` field.

And that's it! This should be much, much faster.

There is a bit more to it than just that, because of some corner cases that need to be handled. The real code looks more like this:

1. The bottom bit of the `isa` indicates whether all this extra data is active for this class. If it's not active, then fall back to the old hash table approach. This allows for a compatibility mode for classes that fall outside the representable range, or programs that incorrectly assume the `isa` is a pure class pointer.
2. If the object is currently deallocating, do nothing.
3. Increment the retain count, but don't store it back into the `isa` just yet.
4. If it overflowed (an unusual but real possibility with only 19 bits available) then fall back to a hash table.
5. Perform an atomic store of the new `isa` value.

Most of this was necessary with the old approach as well, and it doesn't add too much overhead. The new approach should still be much, much faster.

There are several other performance improvements stuffed into the remaining free bits that make deallocating objects faster. There's potentially a lot of cleanup that needs to be done when an Objective-C object deallocates, and being able to skip unnecessary cleanup can increase performance. These are:

1. Whether the object ever had any associated objects, set with `objc_setAssociatedObject`. If not, then associated objects don't need to be cleaned up.
2. Whether the object has a C++ destructor method, which is also used as the ARC automatic `dealloc` method. If not, then it doesn't need to be called.
3. Whether the object has ever been referenced by a `__weak` variable. If it has, then any remaining `__weak` references need to be zeroed. If not, then this step can be skipped.

Previously, all of these flags were tracked per-class. If any instance of a class ever had an associated object set on it, for example, then _every_ instance of that class would perform associated object cleanup when deallocating from that point on. Tracking them for each instance independently helps ensure that only the instances that really need it take the performance hit.

Adding it all together, it's a pretty big win. My casual benchmarking indicates that basic object creation and destruction takes about 380ns on a 5S running in 32-bit mode, while it's only about 200ns when running in 64-bit mode. If any instance of the class has ever had a weak reference and an associated object set, the 32-bit time rises to about 480ns, while the 64-bit time remains around 200ns for any instances that were not themselves the target.

In short, the improvements to Apple's runtime make it so that object allocation in 64-bit mode costs only 40-50% of what it does in 32-bit mode. If your app creates and destroys a lot of objects, that's a big deal.

**Conclusion**  
The "64-bit" A7 is not just a marketing gimmic, but neither is it an amazing breakthrough that enables a new class of applications. The truth, as happens often, lies in between.

The simple fact of moving to 64-bit does little. It makes for slightly faster computations in some cases, somewhat higher memory usage for most programs, and makes certain programming techniques more viable. Overall, it's not hugely significant.

The ARM architecture changed a bunch of other things in its transition to 64-bit. An increased number of registers and a revised, streamlined instruction set make for a nice performance gain over 32-bit ARM.

Apple took advantage of the transition to make some changes of their own. The biggest change is an inline retain count, which eliminates the need to perform a costly hash table lookup for `retain` and `release` operations in the common case. Since those operations are so common in most Objective-C code, this is a big win. Per-object resource cleanup flags make object deallocation quite a bit faster in certain cases. All in all, the cost of creating and destroying an object is roughly cut in half. Tagged pointers also make for a nice performance win as well as reduced memory use.

ARM64 is a welcome addition to Apple's hardware. We all knew it would happen eventually, but few expected it this soon. It's here now, and it's great.

That's it for today. Check back next time for more adventures in the land of hardware and software. Friday Q&A is driven by reader suggestions, so if an idea pops into your head between now and then for a topic you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-09-27-arm64-and-you.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
