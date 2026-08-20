---
title: NewRoutineDescriptor & Porting 68K code to PPC
apple_id: DTS10001549
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-06-01'
source_url: https://developer.apple.com/library/archive/qa/ppcsys/ppcsys08.html
archived_at: '2026-07-18T02:29:54.501921Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Runtime Architecture](https://developer.apple.com/referencelibrary/Carbon/idxRuntimeArchitecture-date.html)

|  |
| --- |
| Technical Q&A PPCSYS08NewRoutineDescriptor & Porting 68K code to PPC |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: I'm trying to port my 68K code to PPC. I have custom functions defined for calling `ModalDialog`. Here's what my code looked like:   |  | | --- | | ``` ModalDialog((ModalFilterProcPtr) MyFilter, &itemNum); ``` |   The compiler complained that it cannot covert my custom function to type RoutineDescriptor\*, so I changed it by casting it to `RoutineDescriptor`:   |  | | --- | | ``` ModalDialog((RoutineDescriptor*) MyFilter, &itemNum); ``` |   There were no compile or link errors, but now, when I run the program, it crashes with a type 3 error.  What's the correct way to implement this?  A: Create a UPP using `NewRoutineDescriptor` instead of casting to a UPP. In Dialogs.h there is a macro for `NewRoutineDescriptor` called `NewModalFilterProc`. Your code should look like this:   |  | | --- | | ``` ModalFilterUPP myFilterUPP; myFilterUPP = NewModalFilterProc(MyFilter); ModalDialog(myFilterUPP,  &itemNum); ``` |  See Also  - See Using Universal Procedure Pointers in _Inside Macintosh: PPC System   Software_, page 2-21, for more information. |

#### [Jun 01 1996]

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
