---
title: Menu Issues, Drawing, Removal & Increasing Size
apple_id: DTS10002196
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb10.html
archived_at: '2026-07-18T02:38:55.521742Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB10Menu Issues, Drawing, Removal & Increasing Size |

|  |
| --- |
| Q I need to have a CICN menu that has states of enabled, disabled, enabled-hilited, enabled-checked-hilited, and enabled-checked. I've noticed that these update slowly on my PowerPC 6100 66. What optimization can be done to improve the drawing of the various states?   A The trick is that you want to hop into ResEdit and create an 'ICON', and a corresponding cicn with the same ID number. The ID number must be between 257 and 511. Now, when you edit the cicn, you can go under the cicn menu and select "Icon Size" to resize it to be 16x16 (or whatever you like). Next, edit your MENU resource and select "Choose Icon" from the "MENU" menu. This lets you select your small cicn that you just created.  The other way is to create a 'cicn', then open the MENU resource, and select "open using template" from the Resource menu. You open the resource using the MENU template. For the Icon# field of the menu item you want to append cicn to, simply enter the result of 'cicn' resource id - 256. Q What happens if I need to remove the Help menu and Applications menu from my menu list so they no longer appear in my applications menu?   A From the Macintosh application interface standpoint, it's a bad idea. According to the Macintosh Human Interface guidelines, the menu bar should always contain the standard menus: the Apple menu, the File menu, the Edit menu, the Help menu, and the Application menu. Also, the Menu Manager will continually prevent this from working. Every time the Menu Manager notices that these menus are not there (e.g., at MenuSelect time, or at DrawMenuBar time) it will add them again. They must be there. Q Is it possible to make the Mac menu bar within my application larger than the standard 20 pixels (without patching any traps), and what sort of trouble might this cause for me?   A Yes. Just use the same technique for hiding the menu bar in reverse. Part of hiding the menu bar is changing the low memory global MBarHeight to 1 or 0. To make the menu bar taller, just change that value to the height you want (in pixels). Note that this technique won't change the size of the text or the position of the title text. [May 01 1995] |

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
