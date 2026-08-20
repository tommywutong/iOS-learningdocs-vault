---
title: Determining volume size
apple_id: DTS10001194
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-09-14'
source_url: https://developer.apple.com/library/archive/qa/fl/fl08.html
archived_at: '2026-07-18T02:29:28.935452Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > File Management](https://developer.apple.com/referencelibrary/Carbon/idxFileManagement-date.html)

|  |
| --- |
| Technical Q&A FL08Determining volume size |

|  |  |
| --- | --- |
| ---   Q: I have an application that needs to report a disk's size and total free space available. How do I ensure that I get the correct information on all systems?  A: The answer to getting the correct volume size depends on what version of the Mac OS you are running and what calls are implemented for finding the volume size.  If all you want is a call that "does the right thing" then look no further than [MoreFiles'](https://developer.apple.com/dev/techsupport/source/Files.html) `XGetVInfo` function. If, however, you would like an explanation of what to do for all of the cases, then read on.  There are three ways of getting this information:   - Call `PBXGetVolInfo`; - Walk the Volume Control Block (VCB) list; or - Call `PBHGetVInfo`.   You can determine the best method by calling `Gestalt` with the `gestaltFSAttr` selector, and checking the `gestaltFSSupports4GBVols` and `gestaltFSSupports2TBVols` bits. PBXGetVolInfo If the `gestaltFSSupports2TBVols` bit is set, then you should call `PBXGetVolInfo`. `PBXGetVolInfo` is backwardly compatible with small volumes, and works for all volumes sizes currently supported by the Mac OS.  If you are writing PowerPC code, [Q&A FL07](Legacy%20Documentclose%20button-2.md) has the needed glue code to call `PBXGetVolInfo` from PowerPC code.  The `PBXGetVolInfo` call works almost exactly as `PBHGetVInfo`. However, it uses a `XVolumeParam` structure, rather than a `HVolumeParam` structure. The two structures are the same, except that the `XVolumeParam` structure has two additional fields to contain the extra information needed to return information about volumes larger than 2 GB, and it uses a previously unused field in the `HVolumeParam` structure. The `filler2` field in `HVolumeParam` is the `ioXVersion` field in the `XVolumeParam`structure (make sure you set it to _0_ for this version of `PBXGetVolInfo`). The extra fields in the `XVolumeParam` structure are:  `UnsignedWide ioVTotalBytes; /* total number of bytes on volume */  UnsignedWide ioVFreeBytes; /* number of free bytes on volume */`    |  | | --- | | __Note:__  If you care about the number of allocation blocks, you will have to calculate that value yourself because `ioVNmAlBlks` is still an unsigned short in the `XVolumeParam` structure. An HFS+ volume can have a many more than 65535 allocation blocks, so this value can be wrong. By using `ioVTotalBytes` and `ioVAlBlkSiz` you can calculate the correct number of allocation blocks (`ioVTotalBytes/ioVAlBlkSiz` = allocation block size). |   Volume Control Blocks If the `gestaltFSSupports2TBVols` bit is not set, but the `gestaltFSSupports4GBVols` bit is set, then you will want to walk the VCB list to get the correct information.  System 7.5 introduced support for volumes larger than 2 GB, up to a maximum of 4 GB. However, `PBHGetVInfo` does not report volume sizes larger than 2 GB. For compatibility reasons, the System 7.5 `PBHGetVInfo` call was changed to pin the number of allocation blocks and free allocation blocks reported so as to always be 2 GB or less. This change was made because a significant number of programs use signed math to determine the volume size and free space. They do not work if the real values are returned.  For example, if the allocation block size is `0xFE00` (the largest possible under System 7.5), the total number of allocation blocks and number of free allocation blocks is pinned to `0x8102`.  The volume's VCB still contains the real values, so code that needs the real values can still get to them via the VCB directly.  See the DTS sample code [MoreFiles](https://developer.apple.com/dev/techsupport/source/Files.html) for a routine (`HGetVInfo`) that shows how to access the VCB to get the actual number of allocation blocks. PBHGetVInfo The last option should be used only if you are running on a Macintosh where `Gestalt` returns that neither the `gestaltFSSupports4GBVols` bit nor the `gestaltFSSupports2TBVols` bit is set. In this case, call `PBHGetVInfo` to get the volume information. This is the most basic way of determining a volume size, and this method works on all Macintoshes with HFS support and on all volumes (though it does not return the correct information for volumes greater than 2 GB in size). |

#### [Sep 14 1998]

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
