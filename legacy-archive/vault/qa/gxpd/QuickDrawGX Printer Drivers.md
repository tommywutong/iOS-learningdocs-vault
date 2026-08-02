---
title: QuickDrawGX Printer Drivers
apple_id: DTS10001217
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd02.html
archived_at: '2026-07-18T02:29:32.160881Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD02QuickDrawGX Printer Drivers |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I'm currently working on localizing our first QuickDrawGX driver release. We're using AppleGlot and most of the languages are fine. However, we're having a problem with the Japanese driver. Everything looks fine except for our Panel icon names. We have a driver-specific Options panel, and it contains a bunch of garbage characters. We're using a localized system to test and to view the driver's UI. Does the string being defined as a `pstring[31]` in the `gxPrintPanelType` have anything to do with our problem, such as possibly having two byte characters get messed up?  A: Both the font and the character data have to be set properly to display Japanese data. AppleGlot substitutes Japanese for English text, but it doesn't let you specify the fonts. Most resources only have text, with no associated font/script info, so the system has to guess what font to use. QuickDrawGX lets you specifically set the script code to match the text data.  Usually, the system uses the System or Application font, which in your case was Japanese, so this should have worked correctly. Since other icons in the list were displaying Japanese names, the code was obviously supporting Japanese text, but something was mistakenly telling it that your garbage text was Roman instead of Japanese. We looked at the data structure that included the text, and the following field was the `ScriptID` field, which was, in fact, set to smRoman. Changing this to `smJapanese` (1) and then rebuilding the resource file solves the problem.  In general, GX is good about associating a script ID with all-text data. This allows multiple scripts to be supported at once (which is good). It does mean, however, that you have to watch for this problem when localizing your product. There may also be other places in your product where this is an issue. To find these, search the resource files for `'smRoman'` and scrutinize those areas where it's found. Be aware that `smRoman` may also be represented by the constant 0, if it was not defined properly. |

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
