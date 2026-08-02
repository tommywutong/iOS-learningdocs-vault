---
title: Including the Cursor in a Screen Capture when using CopyBits
apple_id: DTS10001898
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-09-27'
source_url: https://developer.apple.com/library/archive/qa/qd/qd45.html
archived_at: '2026-07-18T02:38:37.857275Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD45Including the Cursor in a Screen Capture when using CopyBits |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: When I used `CopyBits` to do a screen capture, the cursor is not included. What is going on?  A: `CopyBits` calls `ShieldCursor` to hide the cursor before it does its actual work. That is why you never see the cursor in your bitmap. The following bit of code hides the cursor and decrements the cursor count in the low memory global to fool `CopyBits` not to call `ShieldCursor`. Just as a warning, using low memory globals is dangerous and is subject to future OS changes. Anyway, the OS screen dump behaves similarly.   |  | | --- | | ``` 			unsigned char oldCrsrVis; 			short oldCrsrState; // // Hide cursor // 			oldCrsrVis = GetCrsrVis(); 			oldCrsrState = GetCrsrState(); 			SetCrsrVis((unsigned char) 0); 			SetCrsrState(oldCrsrState - 1); 			CopyBits(.....)  // // Restore old cursor // 			SetCrsrState(oldCrsrState); 			SetCrsrVis(oldCrsrVis); ``` |   The functions are defined as:   |  | | --- | | ``` enum {     CrsrRect = 0x83C,   /*[GLOBAL VAR]  Cursor hit rectangle [8 bytes]*/     TheCrsr  = 0x844,   /*[GLOBAL VAR]  Cursor data, mask & hotspot [68 bytes]*/     CrsrAddr = 0x888,   /*[GLOBAL VAR]  Address of data under cursor [long]*/     CrsrSave = 0x88C,   /*[GLOBAL VAR]  data under the cursor [64 bytes]*/     CrsrVis  = 0x8CC,   /*[GLOBAL VAR]  Cursor visible? [byte]*/     CrsrBusy = 0x8CD,   /*[GLOBAL VAR]  Cursor locked out? [byte]*/     CrsrNew  = 0x8CE,   /*[GLOBAL VAR]  Cursor changed? [byte]*/     CrsrState = 0x8D0,  /*[GLOBAL VAR]  Cursor nesting level [word]*/     CrsrObscure = 0x8D2 /*[GLOBAL VAR]  Cursor obscure semaphore [byte]*/   }; int IsCursorHidden(void); void SetCrsrVis(unsigned char cursorVisible); unsigned char GetCrsrVis(void); PicHandle DumpScreenArea(void); void ModCrsrState(short del); short GetCrsrState(void); void SetCrsrState(short val); void SetCrsrVis(unsigned char cursorVisible) {     *(unsigned char*)CrsrVis = cursorVisible; } unsigned char GetCrsrVis(void) {    return( *(unsigned char*)CrsrVis ); } void ModCrsrState(short del) { 	*(unsigned char*)CrsrState += del; } short GetCrsrState(void) { 	return ( *(unsigned char*)CrsrState ); } void SetCrsrState(short val) { 	*(unsigned char*)CrsrState = val; } int IsCursorHidden() { 	int retVal = 0;     unsigned char cursorVisible;     cursorVisible = *(unsigned char*)CrsrVis;     if (cursorVisible)         retVal = 0;     else         retVal = 1;     return (retVal); } ``` |   You can find a screen dumping sample in the latest Dev. CD. The complete path is:   |  | | --- | | ``` References:      Dev.CD Aug 96 TC           Sample Code                Snippets                     QuickDraw                          ScreenDump                               DumpScreen.c ``` | |

#### [Sep 27 1996]

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
