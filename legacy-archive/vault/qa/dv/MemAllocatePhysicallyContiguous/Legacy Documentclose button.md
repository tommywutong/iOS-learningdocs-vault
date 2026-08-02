---
title: MemAllocatePhysicallyContiguous
apple_id: DTS10001177
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-08-23'
source_url: https://developer.apple.com/library/archive/qa/dv/dv36.html
archived_at: '2026-07-18T02:29:27.800741Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV36MemAllocatePhysicallyContiguous |

|  |  |  |
| --- | --- | --- |
| ---   Q: My driver needs to allocate physically contiguous memory. I'm calling `MemAllocatePhysicallyContiguous` but it returns `nil`, even though the system has plenty of free memory. What can I do?  A: `MemAllocatePhysicallyContiguous` uses a very naive algorithm to find physically contiguous memory. The gist of the algorithm is shown below.   |  | | --- | | ``` on MemAllocatePhysicallyContiguous size     result = NewPtrSys(size)     if result != nil then         if LockMemoryContiguous(result, size) != noErr then             previousResult = result;             result = NewPtrSys(size)             if result != nil then                 if LockMemoryContiguous(result, size) != noErr then                     DisposePtr(result)                     result = nil;                 end-if             end-if             DisposePtr(previousResult)         end-if     end-if     return result end MemAllocatePhysicallyContiguous ``` |  |  | | --- | | __Note:__  The above pseudo-code is a rough description of the `MemAllocatePhysicallyContiguous` algorithm. The actual code is more complex, partly because the buffer returned by `MemAllocatePhysicallyContiguous` is always page-aligned. |    This algorithm is not particularly smart about finding physically contiguous memory. Specifically, the algorithm only makes two attempts to find a physically contiguous block. If both attempts fail, `MemAllocatePhysicallyContiguous` gives up and returns an error. There may be plenty of memory, there may even be plenty of physically contiguous memory, but `MemAllocatePhysicallyContiguous` won't find it.  There are a number factors that determine whether the [LockMemoryContiguous](https://developer.apple.com/documentation/mac/Memory/Memory-164.html) call used by `MemAllocatePhysicallyContiguous` succeeds.   - Before VM loads, the relationship between logical and   physical addresses is relatively simple. Typically there   is a direct map between logical and physical addresses.   However, this is not always true.    - [ROM-in-RAM](https://developer.apple.com/library/archive/technotes/tn/tn1167.html)     computers have a number of discontinuities in the     logical-to-physical mapping because of the way the     system transitions from Open Firmware to Mac OS, and     how the system loads the Mac OS ROM file into memory.     For more background on this issue, see DTS Q&A DV     33 [`PrepareMemoryForIO` in the NewWorld](dv33.md).   - These discontinuities are not a new thing.     Historically, computers such as the Mac IIci used the     Memory Management Unit to “stitch” together     banks of RAM that are discontiguous in the physical     address space. Your driver may encounter these discontinuities at   boot time, depending on the hardware platform, the RAM   configuration, the time your driver loads, and the amount   of memory consumed by other drivers that loaded before   you. - After VM loads, the relationship between logical and   physical addresses quickly becomes scrambled. - The ROM contains a primitive version of   `LockMemoryContiguous` that simply checks   whether the memory is physically contiguous and returns   `cannotMakeContiguousErr` if it isn't. If you   try to get physically contiguous memory before VM loads   (or at any time on a system with VM disabled), you will   use this version of `LockMemoryContiguous`. - The Virtual Memory Manager re-implements   `LockMemoryContiguous` with a somewhat smarter   algorithm. If VM is enabled and you try to get physically   contiguous memory after VM loads, this new algorithm will   work harder to find a physically contiguous range of   memory. However, a request for a large block of   physically contiguous memory is still likely to fail.   In summary, the ability of the system to provide physically contiguous memory is extremely limited, and extremely sensitive to environmental factors.  That’s the bad news. The good news is that you can do things to work around this limitation:   - Smaller Memory Allocations—The smaller the   memory allocation, the greater chance that it will be   physically contiguous. [In the limiting case, it is   always possible to allocate one page of physically   contiguous memory.] Allocating one huge physically   contiguous block is the worst case scenario. You may be   able to restructure your driver to use a number of   smaller blocks. - Early Memory Allocation—The earlier you load,   the more likely that you can allocate physically   contiguous memory. Some drivers defer memory allocation   until they are opened, and then fail to get physically   contiguous memory at that time. To prevent this, you can   allocate your memory early in the startup process by   marking your driver with the   `kDriverIsLoadedUponDiscovery` flag. You can   then use the pre-allocated memory when your driver is   opened. - Deferred Memory Allocation—When you can't   allocate memory at startup time, you can try again later,   either when your driver is opened, or when it is tickled   by some other service that loads later in the startup   process. This deferred allocation may succeed because of   VM’s improved `LockMemoryContiguous`   algorithm. - Scatter/Gather—Most DMA hardware supports a   scatter/gather mechanism. [Scatter/gather hardware is a   requirement on OS’s which provide no way to allocate   physically contiguous memory.] Many developers are   reticent to enable scatter/gather because it is less   efficient (it typically consumes PCI bus cycles fetching   the descriptors) and harder to program. However,   scatter/gather is the ultimate solution to   `MemAllocatePhysicallyContiguous` returning   `nil`.   You will get best results by using a combination of these techniques. If your card gains significant performance benefits from using physically contiguous memory, you should try to allocate that memory using the techniques described above. If all your attempts to allocate physically contiguous memory fail, you should ultimately be prepared to enable the scatter/gather mode on your hardware. |

#### [Aug 23 1999]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
