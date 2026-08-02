---
title: Standard File Package
apple_id: DTS10001190
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/fl/fl04.html
archived_at: '2026-07-18T02:29:28.668076Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Carbon](https://developer.apple.com/referencelibrary/Carbon/index.html)

|  |
| --- |
| Technical Q&A FL04Standard File Package |

|  |  |  |
| --- | --- | --- |
| ---   Q: Where does the Standard File Package get its icons?  A: The Standard File Package uses `PBDTGetIcon` to get icon data from the desktop database. You can observe this by entering the following command in MacsBug to place a break point on the call:   |  | | --- | | ``` atb _HFSDispatch d0=23 ``` |   The sample code calls `PBDTGetIcon`.   |  | | --- | | ``` static OSErr GetIconHandle(Handle h) {    OSErr err;    short DTrefNum;    Rect srcRect;    Str255 volName = "\pMacintosh HD";    short i;    IcnInfo ic;    pb.ioCompletion = NULL;    pb.ioVRefNum = 0;    pb.ioNamePtr = volName;    err= PBDTGetPath(&pb);    if( err ) return err;    DTrefNum = pb.ioDTRefNum;    HLock(h);    b.ioCompletion = NULL;    b.ioDTRefNum = DTrefNum;    b.ioTagInfo = 0L;    b.ioDTBuffer = *h;    b.ioDTReqCount = kLarge8BitIconSize; /* ask for the largest */    b.ioFileCreator = 'ttxt';       /* hard wiring these values */    b.ioFileType = 'APPL';    err = PBDTGetIcon(&b,0);    HUnlock(h);    return(err); } ``` |   Disclaimer: This code has not been fully tested, so it is provided on an as- is basis only. You are responsible for all testing, if you decide to include it in any of your own code. |

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
