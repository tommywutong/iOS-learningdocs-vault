---
title: Unpopped Popup Menus and Mac OS 8.5
apple_id: DTS10002230
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-22'
source_url: https://developer.apple.com/library/archive/qa/tb/tb44.html
archived_at: '2026-07-18T02:38:57.219796Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB44Unpopped Popup Menus and Mac OS 8.5 |

|  |
| --- |
| ---   Q: My menu definition function (`'MDEF'`) supports messages 4 and 5, which allow it to draw itself in the "unpopped" state in a popup menu control. Under Mac OS 8.5, my MDEF no longer receives these messages. What gives?  A: In versions 7.0 through 8.1 of Mac OS, the popup menu control definition function would send two messages, `mCalcItemMsg` and `mDrawItemMsg`, to the MDEF used by the menu in a popup menu control. In order to maintain a uniform appearance for popup menus, it was deemed necessary to remove the support for these messages in Mac OS 8.5.  The most common use of this facility seems to have been to put color swatches into an "unpopped" menu. It is, however, possible to display color swatches without a custom MDEF.  One way is illustrated by the new sample "ColorPopUpMenus", available on the Tool Chest Edition of the Developer CD Series.  Another way to work with icons in menu items is via the function `SetMenuItemIconHandle`.  Further Reference:  [Inside Macintosh: Menu Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/MenuManager/menumanager.html)  [Inside Macintosh: Control Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/ControlManager/controlmanager.html)  [Human Interface Guidelines](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/HumanInterfaceGuide/humaninterfaceguide.html) [Dec 22 1998] |

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
