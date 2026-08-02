---
title: Stubs.o vs. fgets
apple_id: DTS10001523
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat13.html
archived_at: '2026-07-18T02:29:51.875422Z'
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
| Technical Q&A PLAT13Stubs.o vs. fgets |

|  |  |
| --- | --- |
| ---   Q: We have a problem with the MPW SIOW and Stubs.o libraries. A program ("Show_bug") linked without either of these libraries works properly (the test sequence is basically an `fopen` followed by an `fgets`), but if the Stubs.o or the SIOW.o library is linked into the program, either nothing is returned by the `fgets`, or a `ZcbFree` error occurs during a call to `fprintf`.  The following list shows the target, the library that is linked, and the bug shown:   |  | | --- | | ``` Target			Library	Bug Show_bug		Stubs.o	the 'fgets' problem Show_bug_NAKED	---		works as expected Show_bug_SIOW		SIOW.o	ZcbFree error during fprintf ``` |   A: The Stubs.o library is intended for use in building MPW Tools, but the make file that you are using is building an application. Changing that to an MPW Tool should solve your problem. For a brief discussion of Stubs.o, see page 9-4 of _Building and Managing Programs in MPW_.  The SIOW library is intended for use in applications that perform simple I/O to a console. SIOW _cannot_ be used with an application that opens windows. There is a warning to this effect on page 6-3 of _Building and Managing Programs in MPW_.  With regard to your Naked build, you should not be making calls to `fgets` or `fprintf` using stdout and stderr from within a "Mac-like" application, as indicated by the warning given in two of the dialogs put up by your Naked application. |

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
