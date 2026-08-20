---
title: Determining if the Cursor is Hidden Or Not
apple_id: DTS10001494
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-09-27'
source_url: https://developer.apple.com/library/archive/qa/ops/ops13.html
archived_at: '2026-07-18T02:29:49.579869Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS13Determining if the Cursor is Hidden Or Not |

|  |
| --- |
| Q How do you determine whether the cursor is hidden or not?   A Currently the best way to determine that is to use a low memory global that has been removed from LowMem.h. The reason that it has been removed is that future OS may handle this differently. Using low-memory globals has never really been approved of but in older interface files, they were documented. However the Universal Interfaces were designed as a way ahead into future operating systems. Access to some low-mems were changed to accessor functions for safety and others were removed. Therefore this means the low-mems without functions were felt to be changeable and no longer safe to use.  The following definitions were taken from an older Interface file:   ``` enum {     CrsrRect = 0x83C,   /*[GLOBAL VAR]  Cursor hit rectangle [8 bytes]*/     TheCrsr  = 0x844,   /*[GLOBAL VAR]  Cursor data, mask & hotspot [68 bytes]*/     CrsrAddr = 0x888,   /*[GLOBAL VAR]  Address of data under cursor [long]*/     CrsrSave = 0x88C,   /*[GLOBAL VAR]  data under the cursor [64 bytes]*/     CrsrVis  = 0x8CC,   /*[GLOBAL VAR]  Cursor visible? [byte]*/     CrsrBusy = 0x8CD,   /*[GLOBAL VAR]  Cursor locked out? [byte]*/     CrsrNew  = 0x8CE,   /*[GLOBAL VAR]  Cursor changed? [byte]*/     CrsrState = 0x8D0,  /*[GLOBAL VAR]  Cursor nesting level [word]*/     CrsrObscure = 0x8D2 /*[GLOBAL VAR]  Cursor obscure semaphore [byte]*/   }; ```   As you can see, CrsrVis is a flag that tells whether the cursor is hidden or not.  The following routine uses this flag to determine the hidden state of the cursor.   ``` int IsCursorHidden() {     int retVal = 0;     unsigned char cursorVisible;       cursorVisible = *(unsigned char*)CrsrVis;     if (cursorVisible)         retVal = 0;     else         retVal = 1;     return (retVal); } ```  Updated: 27-September-96 |

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
