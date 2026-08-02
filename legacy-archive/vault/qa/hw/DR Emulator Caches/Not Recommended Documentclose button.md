---
title: DR Emulator Caches
apple_id: DTS10001300
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/hw/hw28.html
archived_at: '2026-07-18T02:29:36.531300Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [Apple Hardware](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxAppleHardware-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Apple Hardware](https://developer.apple.com/referencelibrary/HardwareDrivers/idxAppleHardware-date.html)

|  |
| --- |
| Technical Q&A HW28DR Emulator Caches |

|  |
| --- |
| ---   Q: Our 68K application is crashing on Macs that have the new Dynamic Recompiling (DR) emulator. If we call `FlushCodeCache()` and `FlushDataCache()`, the crashes stop. Is this a bug in the DR emulator?  A: This is not a bug in the DR emulator. The DR emulator now has an instruction cache that need to be flushed, just like the 68020, 030, and 040.  DR emulator reports itself as being a 68020 processor, just like the old emulator, but it now has an instruction cache that is variable in size (instead of the fixed sized caches on the real processors). Some applications fail to flush the instruction cache either because they did not realize it had one, or their testing on real 680x0 processors showed that flushing the cache was not needed because the cache was naturally flushed by the amount of code going through it.  The fix to the crashing is to flush the cache. If you have code that conditionally flushes the cache, or you do anything that might leave the cache in an inconsistent state, unconditionally flush the cache.  When running on a PowerPC-based Macintosh in PPC or 68K mode, the best way to flush the instruction cache is to call `FlushCodeCacheRange()` since this will remove only the minimum necessary amount of code from the processor's or DR emulator's cache and will result in the most minimal speed loss. For flushing the data cache, simply call `FlushDataCache()`. The DR emulator does not have a data cache so you may not need to flush it, see if just using `FlushCodeCacheRange()` fixes the crashing.  However, you may need to flush both caches in PPC code if you are modifying code since the code is often treated as data and is therefore in the data cache so flushing only the instruction cache does no good (the instruction is stuck in the data cache). For this reason `FlushInstructionCache()` and `FlushCodeCache()` will flush the data cache on an 040 or PPC.  Before calling any of these calls (except `FlushCodeCache()`) make sure that you use `TrapAvailable()` to check for `_HwPriv(0xA198)`. `FlushCodeCache()` does not depend on the `_HwPriv` trap, it depends on `_CacheFlush`, which must be implemented on any Mac that has a cache.  You should call `FlushCodeCacheRange()` if the `_HwPriv` trap is available. If it returns a hwParamErr (-502), or `_HwPriv` is not available, you will have to flush the entire cache by calling `FlushCodeCache()`. See Also:  - _develop_ 23, "Balance of Power; Power Macintosh: The Next Generation" - Technote HW06-Cache As Cache Can |

#### [Apr 08 1996]

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
