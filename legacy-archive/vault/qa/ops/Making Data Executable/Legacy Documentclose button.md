---
title: Making Data Executable
apple_id: DTS10001500
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-04-12'
source_url: https://developer.apple.com/library/archive/qa/ops/ops19.html
archived_at: '2026-07-18T02:29:50.007927Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS19Making Data Executable |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: I'm writing a program that constructs machine code on the fly. How do I correctly flush the processor cache so that I can execute the newly constructed instructions?  A: This answer depends on the instruction set architecture (ISA) of the code you are constructing:   - __If you are constructing 68K code, you must call   `FlushCodeCacheRange` and, if that returns an error,   call `FlushCodeCache`.__ - __If you are constructing PowerPC code, you must call   `MakeDataExecutable`.__  |  | | --- | | __IMPORTANT:__The answer is independent of the ISA of the code you are running. For example, if you're writing PowerPC code that constructs 68K code, you must call `FlushCodeCacheRange` and not `MakeDataExecutable`. Similarly, if you are writing 68K code that constructs PowerPC code, you must call `MakeDataExecutable`. |  |  | | --- | | __WARNING:__  You can not make 68K data executable using either `FlushInstructionCache` or `FlushDataCache`. To correctly make 68K data executable, you must flush both caches in the right order. `FlushCodeCacheRange` and `FlushCodeCache` do this for you, which is why we strongly recommend you use them exclusively.    For a detailed description of how the Macintosh cache architecture affects software, see DTS Technote [HW 06 Cache as Cache Can](https://developer.apple.com/library/archive/technotes/hw/hw_06.html). |   The DTS sample code library "MoreIsBetter" contains a module ("MoreOSUtils") that shows how to make data executable as 68K or PowerPC code. This module handles all of the complexities described below.  There are a number of important things to remember when calling the above routines:   - `FlushCodeCacheRange` is not exported by   InterfaceLib on Mac OS 8.1 and below. If you want to use   `FlushCodeCacheRange` from CFM code prior to Mac OS   8.5, you must write your own Mixed Mode glue. Technote 1127   [In   Search of Missing Links](https://developer.apple.com/library/archive/technotes/tn/tn1127.html) describes the general technique for   doing this. - `FlushCodeCacheRange` is exported by InterfaceLib   on Mac OS 8.5 and above. To access it, you must link with the   InterfaceLib stub library from Universal Interfaces 3.2 or above. - Various versions of Universal Interfaces have one or two of   the following bugs:   1. Wrong prototype for `FlushCodeCacheRange` --    Older versions of Universal Interfaces define    `FlushCodeCacheRange` to have a `void`    result rather than an `OSErr`. This is a problem    because the correct cache flushing algorithm requires you to    test the result from `FlushCodeCacheRange`. 2. Wrong Conditional -- Older versions of Universal Interfaces    conditionally define `FlushCodeCacheRange` so that    it's not available to CFM code. But, as explained above, it's    important to call `FlushCodeCacheRange` if you    generate 68K code, even if you generate the 68K instructions    using PowerPC code.  The following table shows which versions of Universal Interfaces have which of these problems:   |  |  |  | | --- | --- | --- | | __Universal Interfaces Version__ | __Bogus Prototype__ | __Bogus Conditional__ | | 2.1.4 and below | Yes | Yes | | 3.0, 3.0.1, 3.1 | No | Yes | | 3.2 | No | No |  - PowerPC-based computers always implement   `FlushCodeCacheRange`, so you never need to call   `FlushCodeCache` if you're executing PowerPC code. - Some older 68K-based computers may not implement   `_HWPriv`, the trap underlying   `FlushCodeCacheRange`. If your software might be run on   68K-based computers, you should test for the availability of the   `_HWPriv` trap before calling   `FlushCodeCacheRange`. - `MakeDataExecutable` has no trap. If you're running   classic 68K code on a PowerPC-based computer, you must make   explicit CFM and Mixed Mode calls to execute this routine.   Technote 1077 [Calling   CFM Code From Classic 68K Code](https://developer.apple.com/library/archive/technotes/tn/tn1077.html) describes a general technique   for doing this. - `BlockMove` is possibly the easiest way to flush   the 68K instruction cache, especially when you're moving large   chunks of 68K code.   [Inside   Macintosh: Memory](https://developer.apple.com/documentation/mac/Memory/Memory-2.html) documents that `BlockMove` will   do whatever flushing is appropriate when any   [block   12 bytes and bigger](https://developer.apple.com/documentation/mac/Memory/Memory-180.html#HEADING180-31) is moved.   For more information about instruction caches on the Macintosh, see:   - DTS Technote   [HW 06   Cache as Cache Can](https://developer.apple.com/library/archive/technotes/hw/hw_06.html) - Technote PT 39   [The   DR Emulator](https://developer.apple.com/library/archive/technotes/pt/pt_39.html)  Updated: 12-April-1999 |

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
