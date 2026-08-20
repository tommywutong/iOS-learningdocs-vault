---
title: Accessing File Control Blocks
apple_id: DTS10001196
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '1999-10-05'
source_url: https://developer.apple.com/library/archive/qa/fl/fl10.html
archived_at: '2026-07-18T02:29:28.994846Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > File Management](https://developer.apple.com/referencelibrary/Carbon/idxFileManagement-date.html)

|  |
| --- |
| Technical Q&A FL10Accessing File Control Blocks |

|  |  |
| --- | --- |
| ---   Q: What is the correct way to access a file control block (FCB) for an open file?  A: The correct way to access the information from an FCB is to use `FSGetForkCBInfo` (or its parameter block variants `PBGetForkCBInfoSync` and `PBGetForkCBInfoAsync`, or `PBGetFCBInfoSync` and `PBGetFCBInfoAsync` on pre-Mac OS 9.0 systems). In cases where you need immediate access to the FCB it may be necessary to use the File System Manager (FSM) FCB accessors. If FSM is available, you should never access the FCB table or file control blocks (FCBs) directly.  In Mac OS 9.0, FCBs are no longer stored in a table pointed to by the low-memory global `FCBSPtr`. If your software accesses FCBs using this low-memory global, it will either not work in mysterious ways (for 68K code), or halt the system with a `dsMustUseFCBAccessors` (119) system error (PowerPC code that calls `LMGetFCBSPtr`, `LMSetFCBSPtr`, or `LMSetFSFCBLen`).   |  | | --- | | __WARNING:__  Do not assume a file reference number is an offset into a table of FCBs pointed to by the low-memory global `FCBSPtr`, or that the length of an FCB is stored in the low-memory global `FSFCBLen`. This is no longer the case in Mac OS 9.0 and higher. |   There is really only one good reason to access an FCB immediately: your code is the file system that controls the volume on which the open file resides.  Application-level code should always use File Manager routines to get information from the FCB for an open file. Appropriate File Manager routines include:   - the high-level routine `FSGetForkCBInfo`   (Mac OS 9.0 and higher) - the parameter block routines   `PBGetForkCBInfoSync` and   `PBGetForkCBInfoAsync` (Mac OS 9.0 and higher) - the parameter block routines   `PBGetFCBInfoSync` or   `PBGetFCBInfoAsync` (pre-Mac OS 9.0)   The only fields in the FCB not returned by these routines are either file system specific, or they are reserved for the File Manager’s own use. (For example, some fields in an FCB are used for different purposes by the built-in (HFS or HFS Plus) file system than what they are used for by the File Exchange (DOS or ProDOS) file system.) In addition, some network file systems (for example, AppleShare) use `PBGetFCBInfo` to update the information they keep in the FCB, so accessing the FCB immediately may give you stale data.  However, we recognize that there are circumstances where developers need immediate access to the FCB, for example, a file system trap patch, or debugging tools such as MacsBug’s FILE `dcmd`. In the interest of allowing useful things to keep working, and to allow future enhancements to the File Manager, we now require that you access FCBs using accessor functions. The accessor functions have been public since 1994 as part of the File System Manager (FSM) and FSM has been part of Mac OS since System 7.5. You can check for the presence of FSM with `Gestalt` by requesting the `gestaltFSAttr` selector and checking for the `gestaltHasFileSystemManager` bit in the response.  The four FCB accessor functions are:   1. `UTLocateFCB`, which finds an FCB by file    number and volume. (You can also search by filename and    volume, but that is not very useful since multiple files    can have the same name on a volume.) 2. `UTLocateNextFCB`, which finds additional    FCBs (after using `UTLocateFCB`) by file    number (or name) and volume. 3. `UTIndexFCB`, which indexes through the    open FCBs on a volume. 4. `UTResolveFCB`, which maps a file    reference number to its FCB.   All four functions return a pointer to an FCB and all but `UTResolveFCB` (where the file reference number is an input parameter) also return the corresponding file reference number for the FCB.  A recap of the rules:   - use File Manager routines to access FCB information   in most cases; - if you must access the FCB directly, use the FSM   accessor functions `UTLocateFCB`,   `UTLocateNextFCB`, `UTIndexFCB`,   and `UTResolveFCB`; and - only look at the FCB table when FSM is not available   (that is, prior to System 7.5).   For more information on this topic, see DTS [Technote 1184, “FCBs, Now and Forever.”](https://developer.apple.com/library/archive/technotes/tn/tn1184.html) |

#### [Oct 05 1999]

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
