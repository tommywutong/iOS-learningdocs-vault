---
title: Adding Special Folders
apple_id: DTS10002187
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb01.html
archived_at: '2026-07-18T02:38:54.906704Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB01Adding Special Folders |

|  |
| --- |
| Q We are working on an update to our file-launching utility, which is similar to Launcher. We want to let the user easily add "Special Folders," such as the System Folder and the Control Panels folder (basically, all the FindFolder folders). We are experiencing a few problems: 1. There doesn't seem to be a way to find out about new special folders (for the application) without using a new header file and compiling with special cases for these items. Is there a generic way that to do this (I know we are not supposed to use the fld# resource)?  2. I know we could treat these folders as a special case, but then we also have to treat the icons as special cases. This creates a problem because some of the icon numbers are not in the header file. What should we do?  3. There are some folders in System 7.5, notably the Documents folder, the Recent Files folder, the Recent Servers folder, and so on, that are not in the header files or in the fld# resource. How do we deal with these? A Unfortunately, there is no way to check for folders without using the constants that are defined in Folders.h, and you cannot use FindFolder to generically find folders that are added in new system releases. Folder types which are not defined in Folders.h should be regarded as private (for System use only), and you should not create files in these folders. The documentation for FindFolder assumes that the only folders applications will add files to are the 'Preferences' and 'Temporary Items' folders. However, it's understandable that, in some circumstances, your utility might need to access other folders, but this access should be restricted to the folders listed in Inside Macintosh. The folders introduced in System 7.5, such as the Recent Applications, Recent Documents, and Recent Servers folders are only for the use of the Apple Menu Options control panel, and you should avoid accessing them. The 'ShutDown Items' folder, which was introduced in System 7 Pro, is not included in Folders.h, but it is defined in the fld# resource with an id of 'shdf'. You should avoid accessing this folder also.  As you have noticed, the fld# resource contains only the folders defined in Inside Macintosh and included in Folders.h (with the exception of the folders used by the Extensions Manager). If new system releases introduce folders which developers need to access, then the folder constant will be made available. There is no way to use FindFolder without explicitly referencing the folder's signature, so you'd have to update your code, if this happens.  For folder icons, you have to use the icons documented in Inside Macintosh or included in icons.h. The icon ID for any folder which is not documented should be regarded as subject to change.  _Inside Macintosh: Toolbox Essentials_, pages 7 - 53 through 7 - 57 _Inside Macintosh:Finding Directories_   _More Macintosh Toolbox_, page 1 - 132, "System Folder icons" [May 01 1995] |

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
