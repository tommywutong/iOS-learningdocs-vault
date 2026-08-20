---
title: Impossibility of Extracting File System Information from the WindowPtr
apple_id: DTS10001491
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/ops/ops10.html
archived_at: '2026-07-18T02:29:49.405865Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS10Impossibility of Extracting File System Information from the WindowPtr |

|  |
| --- |
| Q I need to get the full pathname to a document in a callback where the only relevant piece of information I have is the WindowPtr for the window that will contain the document. I know the filename, but I do not know the directory ID or volume reference number. Is there any way to obtain the dirID and vRefNum from the WindowRecord?   A Unfortunately, there is no way to extract the file system information you need from a WindowRecord. The WindowRecord includes only structural human interface information which might include the file name (actually the document's title). Windows provide a means of presenting the data of documents for the user, but the WindowRecords have no knowledge of where to find the file system information. As you have implied, you must have the directory ID and volume reference number to extract a full pathname. Knowing the vRefNum and the parent dirID, you would be able to use one of the FullPath routines in the DTS Sample Code MoreFiles.  If you knew the file reference number, you could call PBGetFCBInfo() to get the vRefNum and dirID, then use MoreFiles to get your full pathname. PBGetFCBInfo() gives information about open files (files in the file control block queue). You call PBGetFCBInfo() like this:   ```  pascal    OSErr    GetFileLocation(short refNum,         short *vRefNum,         long *dirID,         StringPtr fileName)  {      FCBPBRec pb;      OSErr error;       pb.ioNamePtr = fileName;      pb.ioVRefNum = 0;      pb.ioRefNum = refNum;      pb.ioFCBIndx = 0;      error = PBGetFCBInfoSync(&pb);      *vRefNum = pb.ioFCBVRefNum;      *dirID = pb.ioFCBParID;      return (error);  } ```   __See Also__:   - For more information on File Control Blocks, see _Inside Macintosh: Files,_pp. 2-81 through 2-83. - For more information on PBGetFCBInfo, see _Inside Macintosh: Files_, pp.   2-237 through 2-238.  Updated: 14-May-96 |

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
