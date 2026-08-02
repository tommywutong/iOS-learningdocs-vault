---
title: Creating Native MPW Tools
apple_id: DTS10001519
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat09.html
archived_at: '2026-07-18T02:29:51.648153Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Tools](https://developer.apple.com/referencelibrary/Java/idxTools-date.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A PLAT09Creating Native MPW Tools |

|  |
| --- |
| ---   Q: Are there any examples or tech notes available that deal with creating native Tools for MPW using Power Mac libraries? I want to see how this is done in C, and I want to use this information to create native Tools for MPW using our Language Systems FORTRAN compiler.  A: Examples and documentation for building 68K and native MPW Tools are available. The __code examples are in the CExamples folder on the current ETO in the Prerelease MPW folder__. You need to know the name of a Tool to locate it's .c and Make files. For example, the Count Tool is in this folder along with the other files needed to build it.  __"Writing and Building MPW Tools," which is Chapter 9 of _Building Programs in MPW___, contains the documentation you need. This chapter is for 68K only, but this is where the examples are. After reading that chapter, see __"Building for PowerPC"__ to read about the changes made to MPW for the Power PC, including the new `CreateMake` dialog box. You might want to port the Count Tool to the Power PC as an exercise while you learn. |

#### [Jun 01 1995]

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
