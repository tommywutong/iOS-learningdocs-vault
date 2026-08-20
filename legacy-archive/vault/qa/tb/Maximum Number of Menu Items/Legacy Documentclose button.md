---
title: Maximum Number of Menu Items
apple_id: DTS10002243
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-22'
source_url: https://developer.apple.com/library/archive/qa/tb/tb57.html
archived_at: '2026-07-18T02:38:57.815905Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB57Maximum Number of Menu Items |

|  |
| --- |
| ---   Q: Can the standard Macintosh menu definition function (`'MDEF'`) handle menus with more than 255 items? If not, how can I write code to do this?  A: The standard MDEF has a hard limit of 255 items. To handle more than this number, you will have to write your own MDEF.  Apple advises against writing an MDEF that handles more than 255 items because the speed of menu drawing, scrolling, and highlighting will tend toward unacceptably slow. Also, selecting from a menu which has more than 50 or so items is a very unpleasant experience for the user.  (If your interface lets users add items to a menu and the user commonly chooses to add more than 50, you should think about whether there is a better way to provide interface for the functionality in question. However, allowing users to add "too many" items of their own accord is certainly better than burdening them with that many items without asking permission first.)  A better method of choosing from large numbers of items, such as fonts, would be to allow the user to select from a scrolling list presented in a dialog. Key presses in the dialog would scroll the list to match (similar to the file list in Standard File).  Finally, really cool applications would allow users to customize the Font menu, preferably both for the application's default and for each document. Users would be able to choose which fonts appeared in the Fonts menu but would still have access to the others via the scrolling list.  This does not rule out other methods that you may have thought of to relieve the user of wading through hundreds of items.  Further Reference:  [Inside Macintosh: Menu Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/MenuManager/menumanager.html)  [Inside Macintosh: List Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/ListManager/listmanager.html)  [Human Interface Guidelines](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/HumanInterfaceGuide/humaninterfaceguide.html) [Dec 22 1998] |

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
