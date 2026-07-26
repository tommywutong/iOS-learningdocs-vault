---
title: 'A look at how malloc works on the Mac | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/05/look-at-how-malloc-works-on-mac.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:3c889a4af525db24'
translated: false
---

> 原文：[A look at how malloc works on the Mac | Cocoa with Love](https://www.cocoawithlove.com/2010/05/look-at-how-malloc-works-on-mac.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I'll take a high-level look at how malloc is implemented on the Mac. I'll look at how memory is allocated for "tiny", "small" and "large" allocation scales, the multi-core performance improvements introduced in Snow Leopard and some inbuilt debugging features you can trigger for finding memory problems including buffer overruns.

## Introduction

All memory in Mac OS X is allocated to applications by the kernel. The kernel allocates memory to applications by mapping virtual memory pages (which are 4 kilobytes in size) into the application's memory space.

You can allocate memory in your application this way (using the `mmap` function) to get your memory 4 kilobytes at a time. Alternately, you can simply use memory on the stack (which is 64 kilobytes big by default) and is mapped automatically for every thread.

But most of the time when people talk about allocating memory, they are referring to allocations using `malloc`.

Compared to requesting pages of virtual memory directly, `malloc` is finer grained (you can request much smaller sizes than 4 kilobytes) and considerably faster (since it doesn't require an `mmap` every time).

Of course, internally, `malloc` does receive its memory from the kernel by mapping virtual memory pages. Malloc gains its advantage by dividing those pages (or clusters of pages) into smaller regions and returning pointers to addresses within those regions when smaller allocations are requested.

> I'm using the term "`malloc`" but this article applies to Objective-C's `alloc` and `allocWithZone:`, all CoreFoundation allocations and all related C functions like `calloc`, `realloc`, `valloc`, `malloc_zone_malloc`, `malloc_zone_calloc`, `malloc_zone_valloc`, `malloc_zone_realloc` and `malloc_zone_batch_malloc` since all these functions go through the same internal implementation on the Mac.

## A generic malloc implementation

Malloc implementations work by requesting a handful of virtual memory pages from the kernel and returning pointers to free areas within those pages when memory is requested. To know which areas within the pages are free at any given time, a malloc implementation must maintain metadata about the size and location of each allocated block in use and any free space between blocks.

> The pages of memory managed by malloc are collectively called "the heap" but it should be noted that malloc generally does not use a [heap data structure](http://en.wikipedia.org/wiki/Heap_(data_structure)) (which is a form of sorted tree) to track blocks; the two uses of the term "heap" are unrelated.

As the program requires more memory, the malloc implementation requests more virtual memory pages, increasing the application's memory footprint. Every reasonable effort should to be made to allocate new blocks in the spaces left by previously free blocks to keep the memory footprint low.

The main difficulty for a memory allocator is to keep the amount of metadata and the amount of processing time low. This can be very difficult to do when memory becomes a mottled pattern of allocated blocks and freed space.

If the memory allocator kept an array of every single allocation, its location and size, the metadata could easily take as much memory as the allocations themselves. To increase efficiency, most allocators do not track every single byte in memory. Most use a resolution of 16 bytes or more. This allows reduced metadata to track allocated and freed runs.

Further, most allocators use free lists; instead of traversing memory on each allocation looking for an empty space of the appropriate size, the allocator keeps lists of freed areas categorized by their approximate sizes. As a further optimization, these free lists do not always track all free areas in a block (the free lists normally track a finite number of free areas).

## The Mac's implementation of malloc

Despite the fact that all C standard library implementations offer a function named `malloc`, they all have very different internal implementations.

The Mac's implementation of malloc is open source and is composed of two key implementation files:

- [malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/malloc.c)
- [magazine_malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/magazine_malloc.c)

The _malloc.c_ file is mostly a wrapper around the internal implementation in _magazine_malloc.c_. This external wrapper routes regular `malloc` invocations through the `malloc_zone_malloc` function using the default malloc zone — so all malloc allocations on the Mac are actually zoned allocations sharing the same implementation that's used by Objective-C's `+[NSObject allocWithZone:]`.

Up until Snow Leopard, the internal implementation was named [scalable_malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/scalable_malloc.c). It is scalable because it contains different code paths for allocations based on their size. The newer version magazine_malloc.c retains much of the code from scalable_malloc.c but adds multithreaded improvements for smaller allocations and removes the old "huge" scale (instead using the same allocation approach for "large" and "huge" scale allocations).

## The Mac's malloc regions

The malloc allocation on the Mac has different code paths for the following allocation sizes:

| Allocation Size | Code path name | Quantum size (Allocation resolution) | Region size |
|---|---|---|---|
| 32-bit: 1 byte to 496 bytes 64-bit: 1 byte to 992 bytes | Tiny | 16 bytes | 32-bit: 1MB 64-bit: 2MB |
| 32-bit: 497 bytes to "Large" threshold 64-bit: 993 bytes to "Large" threshold | Small | 512 bytes | 32-bit: 8MB 64-bit: 16MB |
| \< 1GB RAM: 15kB or greater \>= 1GB RAM: 127kB or greater | Large | 4kB | N/A |

The key point to note about the Mac's scalable malloc implementation is that it doesn't just divide up virtual memory pages to return smaller blocks but it allocates "tiny" and "small" allocations from their own separate regions ("large" allocations are simply allocated as virtual memory pages).

Allocating a "tiny" amount results in memory being returned from within a 2MB block (1MB in 32-bit programs). Allocations are always rounded up to the nearest 16 byte boundary since the tiny regions only track allocations at a resolution of 16 bytes. This has the additional advantage that it ensures all memory allocations are 16-byte aligned (helpful for SSE/Altivec instructions).

Of course, the 1 or 2 MB regions used for tiny allocations are only big enough to hold around 64,000 allocations at the smallest size — less for larger allocations. More regions are created as needed.

Beyond 15kB (127kB on systems with more than 1GB RAM) the Mac's malloc allocates memory purely as virtual memory pages — no additional tracking or metadata is maintained (although the kernel does maintain tracking for these pages).

To summarize the levels of hierarchy then:

- Malloc zones allocate "tiny" and "small" regions or "large" blocks directly
- Regions return blocks from their contents as results for "tiny" and "small" malloc operations

## The importance of regions

The reason for separate regions for tiny and small allocations is that it allows the region's metadata to be more efficiently tuned to tracking the size of object it contains. For "tiny" allocations, tracking memory down to 16 byte units is worthwhile (it allows freed space to be reclaimed better and doesn't waste large amounts of memory around allocated objects). For "small" sized objects though, tracking at this resolution would be a poor tradeoff between CPU time (traversing through lists of freed or allocated blocks) and memory efficiency — the coarser 512 byte resolution is more efficient.

The tiny regions also have the advantage of reducing the impact of memory fragmentation. By keeping small and large allocations separate, the pattern of small allocations in the midst of otherwise large, free areas that is a cause of memory fragmentation is avoided. Of course, it doesn't eliminate fragmentation but helps.

The existence of the "tiny" region is of great important to Objective-C. Since Objective-C allocates all objects within malloc zones and almost all Objective-C objects fall within the "tiny" size bounds, it is of great benefit to have an optimized code path for such allocations.

## Threading improvements in Mac OS X 10.6

In Snow Leopard, Apple replaced the old [scalable_malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/scalable_malloc.c) with the newer [magazine_malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/magazine_malloc.c). This new implementation introduces a new approach of creating special "tiny" memory allocation regions for each thread.

This approach is "inspired" by the [Hoard memory allocator](http://www.cs.umass.edu/~emery/pubs/berger-asplos2000.pdf) with the thread-specific clusters and "superblocks" of that approach implemented as the magazine and regions in the Mac malloc implementation. Most of the allocation metadata that was previously kept in the "zone" structures moves into the new "magazine" level of the hierarchy so that it can be kept thread-specific. This includes all data that needs to be updated per allocation, like the number of allocated regions, the free lists and available memory counts.

Each "tiny" region is itself allocated by the top level allocator but is then assigned to a specific thread. Since the region is then thread-specific, the top-level, shared, allocator does not need to be locked and the chance of any thread contention is very low.

To summarize the levels of hierarchy for "tiny" allocations with these additions:

- Malloc zones allocate magazines for "tiny" regions (1 per thread) and allocated the regions themselves when requested by the magazines.
- Magazines manage the regions for a thread
- Regions return blocks from their contents

Of course, locks are still used internally when allocating or freeing from a region (since a malloc from one thread can still be freed in a different thread) but the chance of two threads contesting a lock is significantly reduced. The likelihood of cache lines shared unnecessarily between CPUs is also reduced since threads don't allocate memory in the same regions.

Then end result is that the majority of memory allocations in Objective-C (which are typically allocated in a thread and released by the autorelease pool on that thread) will have near perfect thread independence.

## A pair of minor notes

When you free memory, your application footprint will not immediately go down. Freeing region allocated memory adds the space to the free list for the region but will not cause the region to be released unless it was the last block in the region. Your application's footprint will only go down if an entire region is freed and the zone can unmap the virtual memory pages.

`calloc` takes two parameters: a size and a number of elements. `malloc` only takes a size but is often calculated by multiplying a `sizeof(SomeType)` by a number of elements. The end result is identical: internally, calloc just multiplies its two parameters together — other than some overflow checking on the multiplication, the size of the returned block from `calloc(a, b)` is identical to the block returned by `malloc(a * b)`.

## Debugging information

One important point to note from reading the malloc.c file is that the Mac memory allocator can be configured at runtime to generate logging information. The following environment variables can be set to have the memory allocator perform debug behaviors:

- **MallocLogFile** \<f\> to create/append messages to file \<f\> instead of stderr
- **MallocGuardEdges** to add 2 guard pages for each large block
- **MallocDoNotProtectPrelude** to disable protection (when previous flag set)
- **MallocDoNotProtectPostlude** to disable protection (when previous flag set)
- **MallocStackLogging** to record all stacks. Tools like leaks can then be applied
- **MallocStackLoggingNoCompact** to record all stacks. Needed for malloc_history
- **MallocStackLoggingDirectory** to set location of stack logs, which can grow large; default is /tmp
- **MallocScribble** to detect writing on free blocks and missing initializers: 0x55 is written upon free and 0xaa is written on allocation
- **MallocCheckHeapStart** \<n\> to start checking the heap after \<n\> operations
- **MallocCheckHeapEach** \<s\> to repeat the checking of the heap after \<s\> operations
- **MallocCheckHeapSleep** \<t\> to sleep \<t\> seconds on heap corruption
- **MallocCheckHeapAbort** \<b\> to abort on heap corruption if \<b\> is non-zero
- **MallocCorruptionAbort** to abort on malloc errors, but not on out of memory for 32-bit processes MallocCorruptionAbort is always set on 64-bit processes
- **MallocErrorAbort** to abort on any malloc error, including out of memory
- **MallocHelp** - this help!

Unfortunately, the normal build of magazine_malloc.c in Mac OS X has the limitation that it won't apply guard pages to "small" or "tiny" allocations. To apply guard pages to all data, you'll need to use the libgmalloc library. Do this by setting the following environment variable:

```objc
export DYLD_INSERT_LIBRARIES=/usr/lib/libgmalloc.dylib
```

For more information, see the [libgmalloc Manual Page](http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man3/libgmalloc.3.html).

You can also set environment variables in Xcode by right-clicking on the executable in the Tree view, selecting "Get Info" and going to the "Arguments" tab.

## Conclusion

I'm not sure there are a huge number of lessons to be directly taken from this article and immediately used in a program. The debug options are useful to know should the need arise but this article is mostly an exercise in investigating one of more heavily used library functions on the Mac.

The memory allocator on the Mac has lots of different OS-specific behaviors related to alignment, granularity and thread performance. Depending on the size of the allocation, and even the amount of installed memory, some of these behaviors will change from allocation to allocation.

One reassuring point to take from this is to know that the many thousands of tiny Objective-C object allocations in a typical Cocoa program do have a heavily optimized path on the Mac.
