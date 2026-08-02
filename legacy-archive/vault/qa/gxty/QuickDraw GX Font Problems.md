---
title: QuickDraw GX Font Problems
apple_id: DTS10001266
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxty/gxty07.html
archived_at: '2026-07-18T02:29:34.781969Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Text & Fonts](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTextFonts-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Text & Fonts](https://developer.apple.com/referencelibrary/TextFonts/index.html)

|  |
| --- |
| Technical Q&A GXTY07QuickDraw GX Font Problems |

|  |
| --- |
| ---   Q: I've enclosed a Tekton font suitcase that causes an error in the sample app, GXWrite, and in any other app that uses GX. The error message states that there is a font-scaler table missing. However, this font does not cause problems in other non-GX applications. There is a FOND resource and a NFNT resource, but no `'sfnt'` resource. The documentation says that GX can work with Type 1, TrueTypeGX, or `'NFNT'` fonts.  I've had similar problems when PostScript font suitcases are dragged directly to the font folder without going through the `TypeEnabler`. Bitmap font suitcases that have no `'sfnt'` resource work fine in non-GX apps, but GX has problems with them.  The TrueType font "Bauhaus 93" that ships with Microsoft Word 6.0 also causes an "Unknown kerning table format" error. How can I identify these problem fonts before the app unexpectedly crashes? The SDK sample code for building a font menu does not check for valid font types, and GX doesn't recognize that these fonts are bad until I try to access them. Is there any way to check this before building the font menu so these fonts are not included in the menu, or is there another way to avoid this problem?  A: While all bitmap, TrueType, and Type 1 fonts can be used on a system running GX, all Type 1 fonts must pass through the Type Enabler before GX can use the outlines within the font. This is because Type 1 fonts do not have the GX `'sfnt'` wrapper around them, and because they are not `'NFNT'` fonts.  The scaler for Type 1 font data must be installed to avoid getting the types of errors you are describing. The scalers for bitmap, TrueType, and TrueType GX fonts are incorporated in the QuickDraw GX extension, but the scaler for Type 1 fonts is not. GX sends the message, "there is a font scaler table missing," because the Type 1 scaler is not installed. ATM GX must be running on your system to use Type 1 fonts with GX.  To determine if a scaler is installed before adding a font to your menu, you should call `GXCountFontGlyphs` (...) (see page 7-35, _Inside Macintosh QuickDraw GX: Typography_). Pass in the font in question, and GX will tell you the number of glyphs within the font. This call has very little overhead. If the font scaler is not installed or turned off, you get a 0 (zero) back as the function result. At this point, you can decide what to tell the user.  There is a known bug in the Font Enabler that returns "Error: bad cmap language for [font name]." A new version of the Type 1 Enabler that corrects this problem is included with QuickDraw GX v1.1.1.  `GXFindFonts` passes back a list of the fonts that QuickDraw GX can use (resource type of `'sfnt'`). If a Type 1 font has not been through the Type 1 Enabler, the font won't show up on the font list passed back by `GXFindFonts` (...) (see page 7-33, _Inside Macintosh QuickDraw GX: Typography_). Your application should only add the fonts to your font menu that `GXFindFonts` (...) finds.  QuickDraw GX was designed to use only the information contained in the font to do it's work. We want the font developer to have complete control over how information (glyphs, kerning, alternate character sets, justification, etc.) is used from within a font when a glyph is drawn on the screen or sent to a printer. Therefore, we must assume that the font contains the correct information. We realize this allows certain problems to develop, like the one you are experiencing. That is why we created Font Validator -- to allow users to check their fonts when they have problems. The problems will diminish as fonts get fixed and as various font developers release their GX fonts.  To prevent any font whatsoever from giving your application problems, your app location has to check all of the font's tables in the same manner that Font Validator does. This is possible, since we've published the entire specification for QuickDraw GX fonts. This specification is on the GX SDK and the MacOS SDK. The amount of work required to implement this feature may not be worth the effort, especially when you consider that a lot of GX fonts are going to be released in the near future.  When Font Validator gives you a "warning," the problem it detected is unlikely to cause trouble for GX (i.e., GX should be able to figure things out). GX also posts "warnings" to your application. Usually, when Font Validator posts a warning, the GX "Quick Fix" option can handle it. However, when Font Validator posts an "error," it is cause for concern. An error means the font has a problem which must be fixed before GX can use it. There are some errors that are not fatal, however -- just inefficient. |

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
