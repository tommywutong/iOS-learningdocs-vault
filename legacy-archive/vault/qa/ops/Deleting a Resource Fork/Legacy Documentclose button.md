---
title: Deleting a Resource Fork
apple_id: DTS10001485
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/ops/ops04.html
archived_at: '2026-07-18T02:29:48.453173Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > File Management](https://developer.apple.com/referencelibrary/Carbon/idxFileManagement-date.html)
- [Carbon > Resource Management](https://developer.apple.com/referencelibrary/Carbon/idxResourceManagement-date.html)

|  |
| --- |
| Technical Q&A OPS04Deleting a Resource Fork |

|  |
| --- |
| Q How can I completely delete the resource fork associated with a file (so the file has absolutely no resource fork associated with it)?   A To delete a file fork without deleting the file, you need to open the file fork with the File Manager, set the fork's EOF to zero, and then close the file. The following code does this:  ``` pascal  OSErr   HDeleteFork(short vRefNum,                             long dirID,                             ConstStr255Param fileName,                             Boolean isResourceFork); /*  [[paragraph]] Delete a fork of a file without deleting the file.     The HDeleteFork function deletes a file's data or resource fork.     The isResourceFork parameter specifies the fork to delete.      vRefNum         input:  Volume specification.     dirID           input:  Directory ID.     fileName        input:  The name of the file.     isResourceFork  input:  The file fork to delete. If true,                       the resource fork is deleted; if false,     the data fork is deleted. */  pascal  OSErr   HDeleteFork(short vRefNum,                             long dirID,                             ConstStr255Param fileName,                             Boolean isResourceFork) {     OSErr   result;     short   refNum;      if ( isResourceFork )     {         result = HOpenRF(vRefNum, dirID, fileName, fsRdWrPerm, &refNum);     }     else     {         result = HOpenDF(vRefNum, dirID, fileName, fsRdWrPerm, &refNum);         if ( result == paramErr )         {         /* HOpenDF isn't supported under System 6, so retry with HOpen */             result = HOpen(vRefNum, dirID, fileName, fsRdWrPerm, &refNum);         }     }     if ( result == noErr )     {         result = SetEOF(refNum, 0);         (void) FSClose(refNum);     }      return ( result ); } ```   On HFS volumes, setting a file fork's EOF to zero releases all allocation blocks associated with the file. However, some foreign file systems add information to the volume's catalog when a resource fork is added and don't remove that data when you set the EOF to zero. For example, on ProDOS volumes, opening a resource fork for a file changes the file to an "extended" file, which can only be opened with GS/OS on an Apple IIgs (extended ProDOS files cannot be opened by ProDOS 8 on an Apple II). With file systems that exhibit this behavior, the only way to remove all traces of the file's resource fork is to copy the file's data fork and then delete the original file. The MoreFiles sample code on the Tool Chest edition of the Developer CD includes a routine called CopyFork that copies only the data fork. Updated: 1-June-95 |

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
