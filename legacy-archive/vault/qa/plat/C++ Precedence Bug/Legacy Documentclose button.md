---
title: C++ Precedence Bug
apple_id: DTS10001517
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat07.html
archived_at: '2026-07-18T02:29:51.429668Z'
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
| Technical Q&A PLAT07C++ Precedence Bug |

|  |  |
| --- | --- |
| ---   Q: We're running MPW 3.3.1 with C++ on a Centris 660AV running System 7.5. All the MPW files are from a clean ETO #15.  According to Stroustrup (the C++ programming language) and the K&R C, the precedence of "<" is _greater_ than the precedence of "!=", and all other references that we have agree with this. Since the two tests below return different results, MPW does not appear to be adhering to this rule. Both tests should succeed, but on MPW C++, test 1 fails. Under MPW 'C', this code works as it is supposed to.   |  | | --- | | ``` ------------------------------------------------------------------------- #include <stdio.h> main() {         puts("Starting Tests...");         if (1 != 900 < 0)                 puts("Test 1 Worked");         else                 puts("Test 1 Failed");         if (1 != (900 < 0))                 puts("Test 2 Worked");         else                 puts("Test 2 Failed"); } -------------------------------------------------------------------------  To compile:  CPlus -o tmp.o tmp.c  Link -o tmp tmp.o "{CLibraries}"StdClib.o "{CLibraries}"CSANElib.o 6                    "{CLibraries}"Math.o 6                 "{Libraries}"Runtime.o "{Libraries}"Interface.o 6                 "{Libraries}"ToolLibs.o ``` |   A: This is a bug, but since MPW is switching over to Mr C (Symantec C++ for MPW) as the main compiler, and this does not occur with SCpp, it is not likely to be fixed (maintenance on CFront has effectively stopped).  You have two choices: either explicitly specify precedence by using (), or switch to SCpp. |

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
