---
title: AFPCommand() variation
apple_id: DTS10001413
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw01.html
archived_at: '2026-07-18T02:29:43.936085Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW01AFPCommand() variation |

|  |
| --- |
| ---   Q: I am trying to use the AppleTalk `AFPCommand()` call with a `csCode` of `afpGetFlDrParms`, but it isn't working properly. I need to get all of the information that is displayed in the Sharing window when a user selects a shared folder and chooses "Sharing..." from the Finder's File menu. I've checked the second edition of _Inside AppleTalk_ and the AppleShare 3.0 SDK, but I can't find anything to help me get this working. What should I do to get this specific `AFPCommand()` variation and `afpSetFlDrParms` to work?  A: There are very few good reasons to call the .XPP driver to talk to an AFP server directly. As noted in [Technical Note "NW 16 - Borrowed AFP Sessions"](https://developer.apple.com/library/archive/technotes/nw/nw_16.html) (in the section titled "Session Borrowing Rules and Restrictions"), "If it can be done with File Manager functions, use the File Manager functions -- don't use AFP calls." Here's how to get the information displayed in the Finder's "Sharing..." dialog using File Manager:  Where  You can obtain the Where information on AFP volumes with `PBGetVolMountInfoSize` (to get the volume mount record size) and `PBGetVolMountInfo`. You can also create an alias to the volume with NewAlias and use `GetAliasInfo` to extract the zone and server name from the alias record.  Connected As  Use `PBHGetLogInInfo` to obtain the Connected As name.  Privileges  You can obtain the Privileges information with `PBGetCatInfo` (zero `ioAcUser` as an input; the connected user's privileges are returned in the `ioAcUser` field) or with `PBHGetDirAccess`.  Owner, User/Group, and Everyone  Use `PBHGetDirAccess` to obtain the Owner, User/Group, and Everyone privileges. To map the user and group ID numbers from `PBHGetDirAccess` to the user/group names, use `PBHMapID`.  To change the Owner, User/Group, and Everyone privileges, use `PBHSetDirAccess`. You can map the user/group name(s) entered in the dialog (if the user changes them) to their user or group ID numbers with `PBHMapName` before calling `PBHSetDirAccess`.  If the volume is local, you can share or un-share it with PBShare and `PBUnshare`. To fill in the Owner and User/Group pop-up menus with the user and group names, use `PBGetUGEntry`. |

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
