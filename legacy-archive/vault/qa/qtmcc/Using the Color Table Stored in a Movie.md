---
title: Using the Color Table Stored in a Movie
apple_id: DTS10001946
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc03.html
archived_at: '2026-07-18T02:38:46.640652Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMCC03Using the Color Table Stored in a Movie |

|  |
| --- |
| Q How can I use the color table stored in a QuickTime movie?   A This varies between the Macintosh and Windows. For the Macintosh, the Movie Controller has a specific flag, mcFlagsUseWindowPalette, that lets you use the 'clut' atom value, or:  ``` void AddControllerFunctionality(MovieController mc) {     long controllerFlags;  // Specify here the functionality you want to have added to the movie controller.  // CLUT Table use     MCDoAction(mc, mcActionGetFlags, &controllerFlags);     MCDoAction(mc, mcActionSetFlags, (void *) (controllerFlags |                                                mcFlagsUseWindowPalette)); } ```   Note that the MoviePlayer does this by default.  Windows has similar code for enabling the use of the color table:   ``` MCDoAction(myMovieController, mcActionSetFlags, (LPVOID) mcFlagsUseWindowPalette); ```   For the Macintosh, without the Movie Controller:   ``` SetMovieColorTable  pascal OSErr SetMovieColorTable(Movie theMovie, CTabHandle ctab) ```   SetMovieColorTable allows a color table to be associated with a movie. The color table is passed in the ctab parameter. If the movie already has a color table, it will be replaced with the new one. If nil is passed for the color table, any existing color table will be removed. The Movie Toolbox makes a copy of the passed in color table. The movie's color table is stored with the movie, and is transferred by CopyMovieSettings.  The color table may be used to modify the palette of the indexed display devices when the movie is played back. If the movie controller is used, this happens automatically is the mcFlagsUseWindowPalette flag on the movie controller is set. In applications which do not use the movie controller, the color table should be retrieved using GetMovieColorTable and passed on to the Palette Manager.   ``` GetMovieColorTable  pascal OSErr GetMovieColorTable(Movie theMovie, CTabHandle *ctab) ```   GetMovieColorTable returns a copy of the movie's color table. If the movie does not have a color table, \*ctab is set to nil. The color table is attached to the movie using SetMovieColorTable.  For Windows, without the Movie Controller:  Certain pictures may be stored with additional data defining a custom palette. You can extract this palette with GetPicturePalette(GetMoviePict(theMovie)), and then use it in your Windows application to obtain a more faithful rendering of a picture:   ``` PicHandle phPicture; HDC hdc; HPALETTE hpalPicture RECT rcPicture;  // Standard Windows call to see if driver can handle a palette if (GetDeviceCaps (hdc, RASTERCAPS) & RC_PALETTE) {    hpalPicture = GetPicturePalette (phPicture);    SelectPalette (hdc, hpalPicture,0);    RealizePalette (hdc); } DrawPicture (hdc, phPicture, &rcPicture, NULL); ... DeleteObject (hpalPicture); ```   Note that the movie has just one single 'clut' resource, that means that you can't have multiple palettes, or palettes that change based on the frame contents. For more information, see develop #10 - In Search of the Optimal Palette, Good & Othmer. [Jun 01 1995] |

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
