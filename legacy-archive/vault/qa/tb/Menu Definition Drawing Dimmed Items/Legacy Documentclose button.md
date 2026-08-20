---
title: Menu Definition Drawing Dimmed Items
apple_id: DTS10002236
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-22'
source_url: https://developer.apple.com/library/archive/qa/tb/tb50.html
archived_at: '2026-07-18T02:38:57.492693Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB50Menu Definition Drawing Dimmed Items |

|  |
| --- |
| ---   Q: What's the correct method for a custom menu definition function (`'MDEF'`) to dim menu items? What's the preferred method for determining whether to draw in a gray color, or paint the items with a gray pattern?  A: When Appearance Manager 1.0.1 or later is present, you should use the theme brush constants (such as `kThemeTextColorMenuItemDisabled`).  When Appearance Manager 1.0.1 or later is NOT present, the proper method for dimming text in menu items is to use the `grayishTextOr` transfer mode. This mode takes into account both color and black-and-white screens. A simple method for dimming non-text items is to set the `OpColor` to gray, and then draw the nontext item in Blend mode.  Further Reference:  [Inside Macintosh: Menu Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/MenuManager/menumanager.html)  [Inside Macintosh: Appearance Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/AppManager/appearancemanager.html)  [Inside Macintosh: QuickDraw Text](https://developer.apple.com/documentation/macos8/TextIntlSvcs/QuickDrawText/quickdrawtext.html)  [Inside Macintosh: QuickDraw](https://developer.apple.com/documentation/macos8/MultimediaGraphics/QuickDraw/quickdraw.html)  [Q&A QD59: grayishTextOr and Mac OS 8.5](../../qd/grayishTextOr%20and%20Mac%20OS%208.5.md) [Dec 22 1998] |

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
