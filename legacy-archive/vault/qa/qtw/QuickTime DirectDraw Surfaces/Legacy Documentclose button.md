---
title: QuickTime DirectDraw Surfaces
apple_id: DTS10002164
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '1999-11-01'
source_url: https://developer.apple.com/library/archive/qa/qtw/qtw96.html
archived_at: '2026-07-18T02:38:53.289442Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime for Windows](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeforWindows-date.html)

|  |
| --- |
| Technical Q&A QTW96QuickTime DirectDraw Surfaces |

|  |  |  |
| --- | --- | --- |
| ---   Q: I'm trying to play a QuickTime 4 for Windows movie into my own `DirectDraw` surface. However, I cannot seem to get the QuickTime for Windows `QTSetDDPrimarySurface` function to draw to my surface properly. What do I need to do?  A: If you want QuickTime to use __your__ DirectDraw object, you need to pass a flag to the QuickTime for Windows `InitializeQTML` function to prevent QuickTime from creating its own `DirectDraw` object, as follows:   |  | | --- | | ``` InitializeQTML(kInitializeQTMLUseGDIFlag); ``` |    Keep in mind that QuickTime has 3 ways of talking to the screen: `DirectDraw`, `DCI`, and `GDI`. If `DirectDraw` doesn't work, QuickTime tries `DCI`, and if that doesn't work, QuickTime falls back to `GDI`. This decision making all occurs inside the `InitializeQTML` function.  Passing in the `kInitializeQTMLUseGDIFlag` flag forces QuickTime for Windows to __not__ use `DirectDraw` or `DCI` (which is what you want). Then, when you later tell us about your `DirectDraw` object, we'll go ahead and use that, just like you wanted.  Here's a short code snippet that uses the `InitializeQTML` function as described above, along with the QuickTime for Windows utility functions to tell QuickTime to draw into a specific `DirectDraw` surface:   |  | | --- | | ``` OSErr                                    err; LPDIRECTDRAWSURFACE4     theSurface4; LPDIRECTDRAWSURFACE       theSurface; HRESULT                               ddResult;  /* Initialize QuickTime using the kInitializeQTMLUseGDIFlag flag so QuickTime doesn't create its own DirectDraw object */ err = InitializeQTML(kInitializeQTMLUseGDIFlag); if (err == noErr) {     err = EnterMovies();     if (err == noErr)     {         /* now tell QuickTime to use our existing DirectDraw object */         err = QTSetDDObject(gDirectDrawObject);         if (err == noErr)         {             theSurface4 = gPrimarySurface;             if (theSurface4 != NULL)             {                 /* get a plain old DIRECTDRAWSURFACE interface to our                 primary surface, as this is the only interface that                 QuickTime can currently handle. */                 ddResult = theSurface4->QueryInterface(IID_IDirectDrawSurface,                           (LPVOID *)&theSurface);                 if (ddResult == DD_OK)                 {                     /* set QuickTime's primary surface */                     err = QTSetDDPrimarySurface(theSurface, 0);                     if (err == noErr)                     {                        /* release the DIRECTDRAWSURFACE interface */                        theSurface->Release();                     }                 }             }         }     } } ``` |    [Nov 01 1999] |

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
