---
title: Calling GetMenu Redundantly
apple_id: DTS10002231
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-22'
source_url: https://developer.apple.com/library/archive/qa/tb/tb45.html
archived_at: '2026-07-18T02:38:57.288059Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB45Calling GetMenu Redundantly |

|  |  |
| --- | --- |
| ---      |  | | --- | | __IMPORTANT:__  This Q&A has been retired. As there are differences in the behavior of this routine when it is called more than one time across various versions of the system software, applications should never call the following routine more than once for any of their menus:   ``` MenuHandle GetMenu(short resourceID);  - or - MenuHandle MacGetMenu(short resourceID); ```   If your application will need to access a menu more than once, then it should call this routine during its initialization sequence, and cache the value returned in a variable for reference later on. |      Q: Why does Inside Macintosh warn about calling `GetMenu` only once for a particular menu? I've done this before (by accident), and testing with the usual stress tools and in the field turns up no problems.  A: `GetMenu` loads the `'MENU'` resource, uses the menu definition function resource (`'MDEF'`) ID to load the proper `'MDEF'`, and then stores the handle to the `'MDEF'` inside the `MenuHandle`.  In the original (64K) ROMs [which are present only in the Mac 128 and 512], the problem was that `GetMenu` would not check to see if the menu had been previously loaded, and would assume that the high byte of the `'MENU'` record held the ID of the `'MDEF'` to load; in fact, it actually held the high byte of the handle to the `'MDEF'`.  This problem was fixed in the 128K ROMs (Mac Plus and 512Ke) and all subsequent systems. Unless your application needs to run on a 128K or 512K Macintosh (unlikely in this day and age), it's safe to call `GetMenu` repeatedly.  Finally, although it's safe today, it's probably not advisable over the long run. Future versions of the Mac OS API may do such things as return to your application a new handle based on the resource template, not just a modified resource handle. So, when you get a chance, do revise your code to avoid calling `GetMenu` redundantly, even though it won't crash you today.  Further Reference:  [Inside Macintosh: Menu Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/MenuManager/menumanager.html) [Dec 22 1998] |

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
