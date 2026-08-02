---
title: Test What You Ship
apple_id: DTS10001508
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-11-02'
source_url: https://developer.apple.com/library/archive/qa/ov/ov01.html
archived_at: '2026-07-18T02:29:50.537968Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OV01Test What You Ship |

|  |  |  |
| --- | --- | --- |
| ---   Q: I went to the trouble of building a fat (68K and PowerPC code) custom window definition function (WDEF) in anticipation of the day when the Window Manager would be implemented in PowerPC-native code. In Mac OS 8.5, the Window Manager __is__ implemented in PowerPC-native code, but only the 68K code in my WDEF gets called. Why?  A: During the development and testing of Mac OS 8.5, we discovered that some applications with custom WDEFs would crash when attempting to open windows which used those WDEFs. On investigating these crashes, we determined that the common factor was fat WDEFs that request that callers use the current instruction set architecture (ISA -- in other words, PowerPC, 68K, or CFM-68K).    |  | | --- | | For more information regarding ISA's, see the [first paragraph](https://developer.apple.com/documentation/mac/PPCSoftware/PPCSoftware-14.html) of the Mixed Mode section of Chapter 1 of _Inside Macintosh: PowerPC System Software_. |      |  | | --- | | For more information on requesting the current ISA, see [the Routine Flags section](https://developer.apple.com/documentation/mac/PPCSoftware/PPCSoftware-24.html) of the constants section of the Mixed Mode Manager Reference section of Chapter 2 of _Inside Macintosh: PowerPC System Software_. |    If a fat WDEF requests the current ISA on a system whose Window Manager is 68K code, the WDEF's 68K code is called. Until Mac OS 8.5, requesting the current ISA would never result in the WDEF's PowerPC code being called, because Window Manager was 68K code. However, since the Window Manager is PowerPC code in Mac OS 8.5, the PowerPC half of a fat WDEF requesting the current ISA is always called.  The PowerPC half of the WDEFs in the crashing applications proved to be catastrophically faulty in some small way or other. Generally, this turned out to be incorrect `procInfo` in the routine descriptor, which results in all sorts of entertaining misbehavior.  We theorize that some developers built fat WDEFs without testing them fully. This is somewhat understandable, because it was impossible to test a fat WDEF which requested the current ISA when that ISA was PowerPC until Mac OS 8.5.  Given a fat WDEF which requests the current ISA, Window Manager now goes out of its way to call the 68K code, which is more likely to have been tested.  There is a larger lesson to be learned here: be careful not to ship code you haven't tested. In other words, code only what you can test now. |

#### [Nov 02 1998]

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
