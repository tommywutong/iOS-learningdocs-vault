---
title: 'Friday Q&A 2015-07-03: Address Sanitizer'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-07-03-address-sanitizer.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:434172c49135fee8'
translated: false
---

> 原文：[Friday Q&A 2015-07-03: Address Sanitizer](https://www.mikeash.com/pyblog/friday-qa-2015-07-03-address-sanitizer.html)　·　mikeash.com Friday Q&A

Posted at 2015-07-03 13:52 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-07-17: When to Use Swift Structs and Classes](https://www.mikeash.com/pyblog/friday-qa-2015-07-17-when-to-use-swift-structs-and-classes.html)  
Previous article: [Friday Q&A 2015-06-19: The Best of What's New in Swift](https://www.mikeash.com/pyblog/friday-qa-2015-06-19-the-best-of-whats-new-in-swift.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [valgrind](https://www.mikeash.com/pyblog/?tag=valgrind)

Friday Q&A 2015-07-03: Address Sanitizer

by [Mike Ash](https://www.mikeash.com/)

**A Most Precarious Situation**  
C is a great programming language in many ways. The fact that it's still going strong after more than four decades is a testament to that. It's not the first (or second) programming language I learned, but it is the one that first made me truly understand what was going on in these mysterious computer machines, and it's the first language I learned that I still use.

C is also a frighteningly dangerous programming language that's responsible for many woes in the world, and allows for the casual creation of bugs so ridiculous that most other languages can't even express them.

A major problem is memory safety. C has none. Code like this will compile _and likely run_ without a problem:

```
    char *ptr = malloc(5);
    ptr[12] = 0;
```

This just allocates an array of five bytes, then writes into the 13th byte of that array, silently corrupting whatever happens to be in memory at that location. Probably nothing. (On Apple platforms, `malloc` always allocates at least 16 bytes even if you asked for less, so this should always work there. Do not write code that relies on this fact.) Maybe something unimportant. Maybe something important.

More sane languages keep track of array sizes and validate indexes before allowing an operation to go through. The equivalent Java code, for example, will reliably throw an exception. When you can count on this, it makes debugging mysterious problems a lot easier. For example, if a variable should contain the value 4, but actually contains the value 5, you know that some piece of code that modifies that variable is to blame. (At least until you reach that stage of debugging where you start looking carefully at the compiler.) In C, you can't assume this. It could be a piece of code that deliberately modifies that variable, or it could be a piece of code that _accidentally_ modifies that variable by using a bad pointer or a bad index.

A whole cottage industry has sprung up to produce solutions to this problem. Clang's static analyzer, for example, can detect certain types of memory safety problems in source code. Programs like Valgrind detect unsafe memory accesses at runtime.

Address Sanitizer is another one of these solutions. It uses a new approach which has some advantages and disadvantages, but it can be a valuable tool for discovering problems in your code.

**Memory Access Validation**  
Many of these tools work by validating memory access at runtime. The theory is that if you can validate accesses as they happen by comparing them against the memory actually allocated by the program, these bugs can be discovered as they happen, rather than being discovered through their side effects long after.

Ideally, every pointer would include data about the size and location of the overall memory region it belongs to, and each access could be validated against that. There's no particular reason a C compiler couldn't be built that does that, but the extra metadata attached to each pointer would make its programs incompatible with code compiled by normal C compilers. That means system libraries couldn't easily be used, and that would severely limit the code that could be tested with such a system.

Valgrind approaches this problem by running the entire program in an emulator. This allows it to work with binaries produced by a normal C compiler without any changes. It then analyzes the program as it runs and keeps track of the state of each chunk of memory as the program manipulates it. This allows it to work with essentially any program without modifications, and system libraries too. This comes with a huge speed penalty, which can make it impractical to run on performance-sensitive code. This approach also requires deep understanding of the semantics of each system call on the platform so that their changes to memory can be appropriately tracked, which requires tight integration with the hosting OS. As a result of that, Valgrind support on the Mac has been hit-or-miss over the years, and as of this writing it does not support 10.10.

Guard Malloc takes advantage of the CPU's built-in memory checking facilities. It replaces the standard `malloc` function with one that marks the memory off the end of each allocation as unreadable and unwriteable. When the program attempts to access memory off the end, the program traps predictably.

The problem with this is that hardware memory protection is relatively coarse. Memory can only be marked as readable or unreadable with page-level granularity, and a memory page on any modern system is at least 4kB in size. That means that each allocation uses at least 8kB of memory: one page for the allocation itself, and one forbidden page off the end, even if the allocation is just a few bytes. It also means that small overruns may not be detected. Memory needs to be allocated on a 16-byte boundary in order to preserve the guarantees of standard `malloc`, so any allocation which isn't a multiple of 16 bytes will have a few bytes off the end which aren't marked as forbidden.

Address Sanitizer attempts to make this concept of forbidden memory more granular. It's essentially a slower but more practical approach to how Guard Malloc works.

**Tracking Forbidden Memory**  
If hardware memory protection can't be used, then it must be tracked in software. Since extra data can't be passed around with a pointer, it must be tracked in some sort of global table. This table needs to be fast to read and fast to modify.

Address Sanitizer uses a simple but brilliant approach. It reserves a fixed section within the process's address space called the shadow memory. In Address Sanitizer terms, a byte that is marked as forbidden is "poisoned," and the shadow memory tracks which bytes are poisoned. A simple formula translates each address within the process's address space into a spot in the shadow memory. Each eight-byte chunk of regular memory maps to a byte of shadow memory, which tracks the poison state of those eight bytes.

Since eight bytes of memory maps to eight bits of shadow memory, it would be natural to think that each byte's poison state is tracked by one bit in the shadow memory. However, Address Sanitizer actually keeps a single integer in the shadow memory byte. It's assumed that all poisoned memory within an eight byte chunk is contiguous and at the end, so the shadow byte describes the number of unpoisoned bytes within the chuck. A value of `1` through 7 indicates that the corresponding number of bytes at the beginning of the region are unpoisoned. A value of `0` indicates that the entire region is unpoisoned. A negative value indicates that the entire region is poisoned. This slightly odd scheme allows for simpler computations when checking accesses against the shadow memory. Allocations are never that close together to begin with, so the assumption that poisoned bytes are contiguous and at the end doesn't cause any trouble.

With this table structure in place, Address Sanitizer generates extra code in the program to check every read and write through a pointer, and throw an error if the memory in question is poisoned. This is the advantage of being integrated into the compiler and not merely existing as an external library or runtime environment: every pointer access can be reliably identified and the appropriate checks added into the machine code.

Compiler integration also allows neat tricks like the ability to poison and guard local and global variables, not just heap allocations. Locals and globals are allocated with a bit of extra padding in between them, and the padding is poisoned to catch any overflows. This is something that Guard Malloc can't do, and that Valgrind has difficulty with.

Compiler integration has downsides as well. In particular, Address Sanitizer can't catch bad memory accesses in system libraries. It is _compatible_ with system libraries, in that you can turn on Address Sanitizer, build a program that links against Cocoa (for example) and have it work, but it won't catch bad memory accesses performed by Cocoa, or performed by your code on memory allocated by Cocoa.

Address Sanitizer also helps to catch use-after-free errors. When memory is freed, it's all marked as poisoned, so subsequent accesses will be trapped. Use-after-free errors are particularly nasty when the memory is reused for a new allocation first, because then you corrupt unrelated bits of data. Address Sanitizer defends against this by placing newly freed memory into a recycling queue that keeps it unallocated for a while before it can be reused.

Adding a check for every single pointer access carries substantial overhead, of course. It depends heavily on just what your code is doing, since different types of code may access pointer contents much more or less frequently. On average, expect a roughly 2-5x slowdown. This is significant, but usually not enough to make a program unusable.

**How to Use**  
With Xcode 7, using Address Sanitizer is simple. When compiling from the command line, add `-fsanitize=address` to the `clang` invocation. Here's a program that exercises it:

```
    #include <stdlib.h>

    void Write(char *ptr, size_t index, char value) {
        ptr[index] = value;
    }

    int main(int argc, char **argv) {
        char *ptr = malloc(12);
        Write(ptr, 12, 42);
    }
```

Compiling and running with Address Sanitizer:

```
    $ clang -fsanitize=address test.c
    $ ./a.out
```

It quickly crashes and produces a bunch of output:

```
    ==18186==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000df9c at pc 0x000101025efc bp 0x7fff5ebda8a0 sp 0x7fff5ebda898
    WRITE of size 1 at 0x60200000df9c thread T0
        #0 0x101025efb in Write (/Users/mikeash/Dropbox/shell/asan/./a.out+0x100000efb)
        #1 0x101025f46 in main (/Users/mikeash/Dropbox/shell/asan/./a.out+0x100000f46)
        #2 0x7fff940025c8 in start (/usr/lib/system/libdyld.dylib+0x35c8)
        #3 0x0  (<unknown module>)

    0x60200000df9c is located 0 bytes to the right of 12-byte region [0x60200000df90,0x60200000df9c)
    allocated by thread T0 here:
        #0 0x101070960 in wrap_malloc (/Applications/Xcode-beta.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/7.0.0/lib/darwin/libclang_rt.asan_osx_dynamic.dylib+0x42960)
        #1 0x101025f2d in main (/Users/mikeash/Dropbox/shell/asan/./a.out+0x100000f2d)
        #2 0x7fff940025c8 in start (/usr/lib/system/libdyld.dylib+0x35c8)
        #3 0x0  (<unknown module>)

    SUMMARY: AddressSanitizer: heap-buffer-overflow ??:0 Write
    0x1c0400001ba0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    0x1c0400001bb0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    0x1c0400001bc0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    0x1c0400001bd0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    0x1c0400001be0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    =>0x1c0400001bf0: fa fa 00[04]fa fa 00 06 fa fa 00 00 fa fa 00 04
    0x1c0400001c00: fa fa 00 06 fa fa 00 07 fa fa 00 fa fa fa 00 00
    0x1c0400001c10: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
    0x1c0400001c20: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
    0x1c0400001c30: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
    0x1c0400001c40: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
    Shadow byte legend (one shadow byte represents 8 application bytes):
    Addressable:           00
    Partially addressable: 01 02 03 04 05 06 07 
    Heap left redzone:       fa
    Heap right redzone:      fb
    Freed heap region:       fd
    Stack left redzone:      f1
    Stack mid redzone:       f2
    Stack right redzone:     f3
    Stack partial redzone:   f4
    Stack after return:      f5
    Stack use after scope:   f8
    Global redzone:          f9
    Global init order:       f6
    Poisoned by user:        f7
    Container overflow:      fc
    Array cookie:            ac
    Intra object redzone:    bb
    ASan internal:           fe
    Left alloca redzone:     ca
    Right alloca redzone:    cb
    ==18186==ABORTING
    Abort trap: 6
```

This is a wealth of information, and in a real-world scenario it would be enormously helpful in tracking down the problem. It not only shows where the bad write occurred, but where the memory was originally allocated, and a bunch of extra data besides.

Using Address Sanitizer from within Xcode is just as easy: edit your scheme, click the Diagnostics tab, and check the box labeled "Enable Address Sanitizer." Then just build and run as usual, and watch the diagnostics roll in.

**Bonus Feature: Undefined Behavior Sanitizer**  
Bad memory accesses are just one of the many entertaining undefined behaviors offered by C. Clang offers another sanitizer which catches many instances of undefined behavior. Here's an example program:

```
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char **argv) {
        int value = 1;
        for(int x = 0; x < atoi(argv[1]); x++) {
            value *= 10;
            printf("%d\n", value);
        }
    }
```

Let's run it:

```
    $ clang undefined.c 
    $ ./a.out 15
    10
    100
    1000
    10000
    100000
    1000000
    10000000
    100000000
    1000000000
    1215752192
    -727379968
    1316134912
    276447232
    -1530494976
```

That got a little weird at the end. No surprise: signed integer overflow is undefined behavior in C. It would be great to catch that instead of just producing bad data. Undefined behavior sanitizer to the rescue! This is enabled by passing `-fsanitize=undefined-trap -fsanitize-undefined-trap-on-error`:

```
    $ clang -fsanitize=undefined-trap -fsanitize-undefined-trap-on-error undefined.c
    $ ./a.out 15
    10
    100
    1000
    10000
    100000
    1000000
    10000000
    100000000
    1000000000
    Illegal instruction: 4
```

This doesn't give any additional information like Address Sanitizer does, but it does stop execution right at the point where the undefined behavior occurred and the problem can easily be inspected in the debugger.

The undefined behavior sanitizer is not integrated with Xcode at the moment. You can enable it for your app by adding the above compiler flags to your project's build settings directly.

**Conclusion**  
Address Sanitizer is a great piece of technology that can catch a lot of problematic errors in C code. It's not perfect and it won't find all errors, but even so it provides some extremely useful diagnostics. I highly recommend that you try it on your code base and see what it finds. The results might surprise you.

That's it for today. Come back next time for more gooey goodness. Friday Q&A is driven by reader suggestions, as always, so if you have a topic you'd like to see me discuss here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
