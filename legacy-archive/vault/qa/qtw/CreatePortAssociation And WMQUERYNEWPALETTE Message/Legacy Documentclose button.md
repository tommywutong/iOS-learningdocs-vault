---
title: CreatePortAssociation And  WM_QUERYNEWPALETTE Message
apple_id: DTS10002159
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '1998-09-21'
source_url: https://developer.apple.com/library/archive/qa/qtw/qtw91.html
archived_at: '2026-07-18T02:38:53.166750Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime for Windows](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeforWindows-date.html)

|  |
| --- |
| Technical Q&A QTW91CreatePortAssociation And WM_QUERYNEWPALETTE Message |

|  |
| --- |
| Q Under QuickTime 3 for Windows, my window procedure never receives `WM_QUERYNEWPALETTE` messages if I've called `CreatePortAssociation` in the same window procedure on `WM_CREATE` events. What's going on?    A You are right in that the window procedure for the `HWND` does not get forwarded the `WM_QUERYNEWPALETTE` message. To get around this, you can use the Mac toolbox functions `NSetPalette` and `ActivatePalette` to activate your custom palette. However, because of this anomaly in QTML (not forwarding this message), you need to work around it by capturing the `WndProc` and calling back through for all messages except the palette one (because you'll use `NSetPalette` and `ActivatePalette` to assert the palette instead). Here's a code snippet which illustrates this:  ``` qtmlWndProc = SetWindowLong(hWnd, GWL_WNDPROC, MyNewWndProc);  LRESULT CALLBACK MyWndProc() {   if (message == WM_QUERYNEWPALETTE)   {     // do your thing   }   else     CallWindowProc(qtmlWndProc, ...); } ```   Note that this is kind of messy since you need to avoid going recursive with QTML calling back to you from within that `CallWindowProc`.  Of course, you can always use the Win32 palette routines anywhere in your code to assert a custom palette. After you change the color environment, simply ensure that you make the QuickTime `GDevice` match. Here's pseudo-code describing how to make the `GDevice` match:  1) Call `SelectPalette` and `RealizePalette` to change the hardware palette  2) Call `GetSystemPaletteEntries` to get the colors back from Windows  3) Convert the palette entries into a QuickTime ColorTable  4) Move the color table entries into the `(**(**GetMainDevice()).gdPMap).pmTable`  Note also you can create a custom palette and associate it with your movie using the QuickTime 3 `GetMovieColorTable()` and `SetMovieColorTable()` functions. If you're going to display your movie along with a movie controller, and you want the custom palette to be used when the movie is activated, simply use the `MCDoAction` function and the `mcFlagsUseWindowPalette` flag. [Sep 21 1998] |

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
