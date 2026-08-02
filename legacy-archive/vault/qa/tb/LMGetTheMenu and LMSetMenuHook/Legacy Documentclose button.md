---
title: LMGetTheMenu and LMSetMenuHook
apple_id: DTS10002238
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-22'
source_url: https://developer.apple.com/library/archive/qa/tb/tb52.html
archived_at: '2026-07-18T02:38:57.609520Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB52LMGetTheMenu and LMSetMenuHook |

|  |
| --- |
| ---   Q: According to Inside Macintosh, `LMGetTheMenu` should return the menu ID of the currently highlighted menu, but the return value is always zero when I call `LMGetTheMenu` during the routine whose address I've passed to `LMSetMenuHook`. What am I missing?  A: Documentation on `LMGetTheMenu` is unclear. It is supposed to return the ID of the menu whose title is currently highlighted after a call to `MenuSelect`. However, Menu Manager does not update this variable while the user is selecting from a menu; it is updated only after a selection has been made. The bottom line is that `LMGetTheMenu` does not work at `MenuHook` time.  If you need to know when a specific menu is pulled down, you might be able to use a custom menu definition (`'MDEF'`) -- see the latest Tool Chest Edition of the Developer CD Series for sample code. Or, you could use `LMSetMBarHook`, whose parameter is called only when a menu is about to be drawn. You might then be able to use the passed rectangle to help you discover which menu is pulled down. However, neither of these methods is particularly recommended; it would be better to redesign your program so that it doesn't need to know these things.  Further Reference:  [Inside Macintosh: Menu Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/MenuManager/menumanager.html) [Dec 22 1998] |

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
