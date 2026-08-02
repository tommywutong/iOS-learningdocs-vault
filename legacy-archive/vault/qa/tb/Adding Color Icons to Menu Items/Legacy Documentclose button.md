---
title: Adding Color Icons to Menu Items
apple_id: DTS10002234
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-22'
source_url: https://developer.apple.com/library/archive/qa/tb/tb48.html
archived_at: '2026-07-18T02:38:57.434248Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB48Adding Color Icons to Menu Items |

|  |
| --- |
| ---   Q: Is there a way to display color icons in menus?  A: Absolutely. Here are two ways:   - If `SetMenuItemIconHandle` is available, use it. It affords   you a great deal of flexibility. - If not, then simply make a `'cicn'` resource with the   proper ID for the relevant menu item, and the system will use the   `'cicn'` instead of a 1-bit icon (`'ICON'`).   This trick works on any system with color QuickDraw. To support   systems both with and without color QuickDraw, simply provide both   1-bit (`'ICON'`) and color (`'cicn'`) icon   resources with the same ID.   Further Reference:  [Inside Macintosh: Menu Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/MenuManager/menumanager.html)  [Inside Macintosh: Icon Services and Icon Utilities](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/IconServUtili/iconservicesandutilities.html) [Dec 22 1998] |

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
