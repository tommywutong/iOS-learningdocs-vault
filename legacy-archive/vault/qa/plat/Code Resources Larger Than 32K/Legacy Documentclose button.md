---
title: Code Resources Larger Than 32K
apple_id: DTS10001511
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat01.html
archived_at: '2026-07-18T02:29:50.713792Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A PLAT01Code Resources Larger Than 32K |

|  |  |
| --- | --- |
| ---   Q: I'm trying to write a 4D external (stand-alone code) which will be larger than 32K. When I compile my C code with model -far, the linker tells me:   |  | | --- | | ``` ### Link: Error: Linker does not edit 32-bit instructions. (Error 29) ``` |   Q: Is there an example showing a MPW generated >32K standalone code resource?  A: Model far works by patching parts of the segment loading mechanism, changing the structure of jump table entries, and storing segment relocation information for the generation of absolute addresses. This only applies to applications, however, which is why the Linker is generating an error.  The restriction in creating >32K CODE resources is only because of limitations with intra-segment branching. Depending on the compiler options you use, this can be worked around. For example, the MPW C compiler has the `-bigseg` option, which creates one big CODE resource with all function calls within the same segment to be BSR.L instruction. Since BSR.L is a PC-relative instruction with a 32-bit offset, the 32K restriction is eliminated. (However, these code resources will only work on Macintoshes with 68020s or later).  Another option you can use with the MPW Linker is `-br` on. This creates branch islands that are less than 32K apart for overall jumps within a CODE resource that are greater than 32K. This method has the advantage of being able to work on 68000 Macintoshes, but it can make your code larger and slower.  To find out more about both options, we suggest looking through the MPW Command Reference under C and Linker. In addition, check out the Runtime Architecture chapter in "Building Programs with MPW," available with MPW.  Unfortunately, there aren't any samples showing how these samples are used, but it should be just a matter of adding options to your MakeFile. |

#### [May 01 1995]

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
