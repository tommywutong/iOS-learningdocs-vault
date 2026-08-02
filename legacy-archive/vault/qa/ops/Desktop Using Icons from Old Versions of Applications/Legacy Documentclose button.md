---
title: Desktop Using Icons from Old Versions of Applications
apple_id: DTS10001484
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-03-26'
source_url: https://developer.apple.com/library/archive/qa/ops/ops03.html
archived_at: '2026-07-18T02:29:48.407750Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS03Desktop Using Icons from Old Versions of Applications |

|  |
| --- |
| Q My application has suddenly stopped using the correct icons. In the past, it has properly constructed BNDL and FREF consistently, and as of last week, the correct application and document ICONS appeared on my desktop(s). Now, however, I am getting icons from an earlier version of the program. I rebuilt all my desktops, drag-copied the application to another folder, and launched it, but none of these things helped. Everything seemed to work properly after I made changes last week, and I haven't changed any of the resources since then. I even tried to un-set the INITed flag, thinking that might help record the icon in the desktop.  What should I do to force the desktop to record the new icons when I create a new version of an application? A BNDL resources can be mysterious and frustrating to deal with at times. However, there are some general guidelines to follow which should alleviate most problems: \* Eliminate all other copies of your application anywhere on your system. All older versions that use the same creator and file types must be removed. Older versions affect the Finder database when you rebuild the desktop (i.e., the Finder defaults back to your original BNDL resource).  \* Make sure the BNDL bit is checked in the ResEdit Get Info box for the application resource, and that the Inited bit is unchecked, before you rebuild the desktop.  \* Check all ICON numbers to be sure they match their BNDL numbers, and make sure the signature in the BNDL resource matches the Creator in the Info window. It is also advisable to start your numbering scheme from 128 (the default), rather than trying to use an extravagant number system.  \* Rebuild the desktop, bearing in mind that if older versions of your application exist anywhere on the system, the Finder defaults to the icons from those old copies and never looks at your new BNDL resources. If you removed all of the old copies, the Finder checks your BNDL during the desktop rebuild, checks the INITed bit, and displays your icons appropriately.  If you have to leave older versions of your application on your hard disk for some reason, store them in a manner that prevents their outdated BNDL information from being included in the Desktop Database (e.g., put them in a compressed archive). Q When a new version of an application is copied onto the hard disk (or copied between folders) and then launched, doesn't the application replace the icon entries in the Desktop Database with the ones in the new version? When you upgrade some applications, they change all the icons, including those from older document files, even when you have multiple versions of the application on your hard disk. How can I force a desktop rebuild on the boot disk (other than holding down the Command and Option keys during startup)?   A Applications don't replace the icon records in the Desktop Database when you copy a new version of the application to your hard disk. Instead, the Finder reads the application's Finder information to determine whether it has "seen" the application or any of its files before. It does this by examining the hasBeenInited bit in the fdFlags field of the FInfo record returned inioFlFndrInfo by PBGetFInfo or PBGetCatInfo. If the hasBeenInited bit is set, the Finder assumes it has seen the file before, and it uses the BNDL information that is already in the Desktop Database to display an icon for the application. If the Finder hasn't seen the file previously, it gives it a position on the desktop or in a window, and it reads the file's BNDL resource (if any) and adds whatever information it finds to the volume's Desktop Database. Note that the Finder does not necessarily display the new icon if it comes across older BNDL info for the same creator. In other words, copying a new version of an application with the same creator does not cause the icon information to be replaced. It merely adds another BNDL resource to the Desktop Database. The Finder displays the first icon it encounters in the Desktop Database, regardless of whether a newer icon exists elsewhere in the database.  The only guaranteed way to get the system to "forget" the older icons it knows for a given creator is to rebuild the desktop after removing older copies of the application. The easiest way to avoid these problems is to use a shareware utility called BNDL Banger, which lets you decide which icons you want displayed. [Mar 26 2001] |

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
