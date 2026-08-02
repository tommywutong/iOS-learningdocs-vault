---
title: Memory Allocation Recommendations on Mac OS X
apple_id: DTS10003484
resource_type: Technical Note
platform: macOS
topic: null
technology: null
published: '2005-07-12'
source_url: https://developer.apple.com/library/archive/technotes/tn2130/_index.html
archived_at: '2026-07-26T19:53:51.029675Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2130

# Memory Allocation Recommendations on Mac OS X

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

This Technical Note is aimed at Carbon Application Developers to help them decide which, out of the multiple memory allocation APIs, is the one the most appropriate for the situation.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwugsbrfvjukq2ujfhu4mi)[Legacy and Deprecated APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwugsbrfvjukq2ujfhu4mq)[Current APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwugsbrfvjukq2ujfhu4my)[Core Foundation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwugsbrfvjvkqstivbviskpjyzq)[Macintosh Memory Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwugsbrfvjvkqstivbviskpjy2a)[Standard C Library](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwugsbrfvjvkqstivbviskpjy2q)[Moving and Setting bytes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwugsbrfvjukq2ujfhu4ny)[Summary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwugsbrfvjukq2ujfhu4oa)[Reference Section](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwugsbrfvjukq2ujfhu4oi)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbygqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

A lot of Carbon APIs allocate memory to create specific items, for example, `HIObjectCreate`, `CreateNewWindow`, `NewGWorld`. Since there is usually only one API to create/allocate a specific item, there is little choice, thus little doubt as to which API is the best to use in each case.

But when it comes to allocating blocks of memory for general use, for example, pixel data for image processing, arrays of numeric values for number crunching, or character buffers for text processing, there are many Carbon APIs which could be used for that purpose.

With choice comes confusion and the possibility of choosing a sub-optimal API for a particular job.

Furthermore, the optimal APIs for Mac OS X are not the same as those which were optimal in Mac OS 9 and earlier releases. Thus, developers who have a lot of legacy code should check this code for possible improvements.

[Back to Top](#)

## Legacy and Deprecated APIs

Open Transport provided the memory allocation function `OTAllocMem` [`void * OTAllocMem(OTByteCount size)`] in the Universal Interfaces in Mac OS 9 and earlier. When Carbon was introduced, `OTAllocMem` was replaced by `OTAllocMemInContext` [`void * OTAllocMemInContext(OTByteCount size, OTClientContextPtr clientContext)`]. Since Open Transport, as a whole, has been deprecated, there is no reason to use `OTAllocMemInContext` other than if you still have to support Mac OS 8 or Mac OS 9. Use `OTFreeMem` to deallocate the allocated memory, you cannot resize the allocated memory.

Multiprocessing Services provided the memory allocation function `MPAllocate` [`LogicalAddress MPAllocate(ByteCount size)`], while this function is still available, it is marked as deprecated and not recommended. Since version 2.0, Multiprocessing Services provides `MPAllocateAligned` [`LogicalAddress MPAllocateAligned(ByteCount size, UInt8 alignment, OptionBits options)`] which has always been available in Carbon. Use `MPFree` to deallocate the allocate memory, you cannot resize the allocated memory.

Most of the specific alignments provided by `MPAllocateAligned` have ceased to be useful, except for the 16-byte boundary alignment required by Altivec code.

Since `malloc` aligns all its allocations on 16-byte boundaries more efficiently than `MPAllocateAligned` does, the memory-related APIs of the Multiprocessing Services have been deprecated, and so you should not use `MPAllocateAligned`.

The Macintosh Memory Manager provides six functions related to virtual memory management as it was handled on Mac OS 8 and 9. All those six functions are available but do strictly nothing when called on Mac OS X from version 10.0 to version 10.3. It is unlikely that they will ever be doing anything in a later release since the virtual memory management of Mac OS X is very different from its predecessor. Those six functions are `ReleaseMemoryData`, `MakeMemoryNonResident`, `MakeMemoryResident`, `FlushMemory`, `HoldMemory`, and `UnholdMemory`.

The Macintosh Memory Manager also provides seven functions which handle memory in the global address space instead of within the application heap on Mac OS 8 and 9. These seven functions are available on Mac OS X but function no differently than their application heap counterparts. Thus `TempNewHandle` is the same as `NewHandle`, `TempMaxMem` is the same as `MaxMem`, `TempFreeMem` is the same as `FreeMem`, `TempHLock` is the same as `HLock`, `TempHUnlock` is the same as `HUnlock`, `TempDisposeHandle` is the same as `DisposeHandle`, and `TempTopMem` is the same as `TopMem`. It is also noteworthy to mention that `FreeMem` always return a hard-coded value of, currently, 20 \* 1024 \* 1024, that `MaxMem` returns the same value, that `TopMem` always returns `NULL`, and that `CompactMem` does nothing else but return the value you passed as its parameter.

[Back to Top](#)

## Current APIs

### Core Foundation

Core Foundation provides in CFBase.h the memory allocation function `CFAllocatorAllocate` [`void *CFAllocatorAllocate(CFAllocatorRef allocator, CFIndex size, CFOptionFlags hint)`]. This function is thread safe.

The main reason for using `CFAllocatorAllocate` instead of another memory allocation API is that you can choose the `CFAllocatorRef` the most appropriate for the situation. It can be just the default `CFAllocatorRef` (`kCFAllocatorDefault`), but you can also use any of the other provided `CFAllocatorRef` (`kCFAllocatorSystemDefault`, `kCFAllocatorMalloc`, `kCFAllocatorNull`, `kCFAllocatorUseContext`) or create your own with `CFAllocatorCreate` (in very rare situations).

You can also, in a library, use `kCFAllocatorDefault` and then you will work with whatever `CFAllocatorRef` was set as a default by the main application.

Use `CFAllocatorDeallocate` to deallocate the allocate memory, you can use `CFAllocatorReallocate` to resize the allocated memory.

### Macintosh Memory Manager

The Macintosh Memory Manager provides in MacMemory.h the four memory allocation functions `NewPtr`, `NewPtrClear`, `NewHandle`, and `NewHandleClear`. All those functions are thread-safe starting with Mac OS X v10.3 but not in previous versions. On Mac OS X, those four functions eventually call the C library function `malloc` with a thin overhead.

Use `DisposePtr` to deallocate the memory allocated by `NewPtr` or `NewPtrClear` and you can use `SetPtrSize` to resize the allocated memory (beware, even on Mac OS X, `SetPtrSize` may fail).

Use `DisposeHandle` to deallocate the memory allocated by `NewHandle` or `NewHandleClear` and you can use `SetHandleSize` to resize the allocated memory.

There is no performance advantage to calling `NewPtr` instead of `malloc`, or `NewPtrClear` instead of `calloc`. This is the reverse of what was true on Mac OS 8 and 9 where `malloc` was eventually calling `NewPtr` in some C runtimes.

Carbon APIs use specific handles less and less, either because the technology has been or is being deprecated; a better, modern replacement has been introduced; or specific handles have been converted in opaque references. See the tables below for some examples; since Carbon APIs rely on handles less and less as new versions of Mac OS X are released, these table lists are not exhaustive and the best way to know whether you should or should not use a specific handle is to look at the comments of its declaration in its header file.

__Table 1__  Technologies which are or are being deprecated.

| Technology | Types (not exhaustive) |
| QuickDraw | PixMapHandle, CTabHandle, PicHandle, PaletteHandle |
| TextEdit | TEHandle, TextStyleHandle, CharsHandle, STHandle |

__Table 2__  Technologies which have a modern replacement.

| Technology | Types (not exhaustive) | Modern Technology |
| Sound Manager | SndHandle, SndListHandle, Snd2ListHandle | CoreAudio |
| File Translation | FileTranslationSpecArrayHandle, FileTranslationListHandle, ScrapTranslationListHandle | Translation Services |

__Table 3__  Specific Handles obsoleted by a modern replacement.

| Specific Handles | Modern Replacement |
| ListHandle (using the List control) | DataBrowser control |
| NavTypeListHandle (Navigation Services) | Use a filter function, use LSCanRefAcceptItem (Launch Services) |
| CIconHandle, IconFamilyHandle | IconRef |
| ControlHandle | ControlRef |
| MenuHandle | MenuRef |

__Table 4__  Specific Handles still in use.

| Specific Handles | Note |
| RgnHandle | HIShapeRef will replace RgnHandle as the HIShape technology evolves |
| AliasHandle | The Alias Manager is evolving to deal with the type AliasRecord \* |

It is still inadvisable to fake handles, that is to use a pointer on a pointer to a memory block, and use them as parameters in Carbon APIs. If the Carbon API attempts to call `GetHandleSize` or `SetHandleSize`, then unexpected consequences will follow.

### Standard C Library

The Standard C Library provides the memory allocation functions `malloc`, `calloc` (which clears the memory block), and `valloc` (which aligns the memory block on a virtual memory page boundary).

`malloc` and `calloc` align their allocations on 16-byte boundaries.

All these functions are thread-safe. Use `free` to deallocate the allocate memory, you can use `realloc` to safely resize the allocated memory.

Apple Engineers spent a long time making `malloc` the most efficient memory allocation function. Use `malloc` (or `calloc`) preferably to any other memory allocation function.

__Note:__ When debugging in Xcode, you may use GuardMalloc. That actually means that you are using libgmalloc which modifies the behavior of `malloc` and `calloc`. libgmalloc alignes the end of the allocated block with the end of a page. Thus, if you need 16-byte aligned allocations, you may need to pad your structures or arrays to a multiple of 16 when debugging with GuardMalloc.

[Back to Top](#)

## Moving and Setting bytes

After allocating memory, it is common to move bytes around. There are many functions which can do the job. Fortunately, it is easier to determine which API should be used almost exclusively.

Prefer `BlockMoveData` or `BlockMoveDataUncached` to `BlockMove`, but anyway, these functions eventually call `memmove`, so...

For copying bytes from one location to another, use `memmove` or `bcopy` which are thread-safe and check for overlaps.

On shipping releases of Mac OS X, `memcpy` also checks for overlaps, but the IEEE specification does not require that check, so behavior on other platforms is undefined, so use it with caution.

In some situations, rather than calling `memmove`, you can use a tight loop or let the compiler generate the code for moving bytes if the size of the transfer is known at compilation time. In most other situations, use `memmove`.

Rather than allocating a new block of memory, you may want to reuse instead previously allocated memory. In that case, it is common to zero that memory before using it. We recommend that you use `bzero` or `memset` rather than `BlockZero` to do so.

[Back to Top](#)

## Summary

Do not use `OTAllocMem` or `OTAllocMemInContext`.

Do not use `MPAllocate` or `MPAllocateAligned`.

Do not use `TempNewHandle`.

Use `NewPtr` or `NewHandle` only in legacy code that you didn't optimize yet. Do not use them in new code.

`CFAllocatorAllocate` should be rarely used.

__Important:__ Use `malloc` or `calloc` almost exclusively.

[Back to Top](#)

## Reference Section

[Optimizing Your Memory Allocations](https://developer.apple.com/documentation/Performance/Conceptual/ManagingMemory/Tasks/MemoryAlloc.html).

[Optimization Strategies for Mac OS](https://developer.apple.com/technotes/tn/tn1174.html).

[Memory Management Edge Cases](https://developer.apple.com/qa/qa2001/qa1259.html).

[Memory Management in Mac OS X](https://developer.apple.com/documentation/Performance/Conceptual/ManagingMemory/index.html).

[malloc(3) and calloc(3) man documentation](x-man-page://3/malloc)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-07-12 | Added a reference to malloc man documentation. |
| 2005-05-24 | GuardMalloc information added. |
| 2005-04-07 | New document that recommends the best ways to allocate memory on Mac OS X. |

