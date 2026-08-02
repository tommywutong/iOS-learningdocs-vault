---
title: Closing PPC ports
apple_id: DTS10001372
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/ic/ic01.html
archived_at: '2026-07-18T02:29:40.346201Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Interapplication Communication](https://developer.apple.com/referencelibrary/Carbon/idxInterapplicationCommunication-date.html)

|  |
| --- |
| Technical Q&A IC01Closing PPC ports |

|  |
| --- |
| ---   Q: I have two apps that communicate with Apple Events. When I call `PPCBrowser` to bring up the Program Linking dialog box, I'd like to filter the list of Macs shown only to Macs running my program. However, since the Apple Event Manager opens the PPC port for communication with other systems, my app can't specify an NBP type to pass as `theLocNBPType` parameter to `PPCBrowser`. Is there a workaround?  A: The routines `AddPPCNBPAlias` and `RemoveNBPAlias` in the file AppleTalk.c in DTS.Lib should help you accomplish your goal of filtering to only systems that are running your application. The complete path to AppleTalk.c on the November 1994 Developer CD is:  Dev.CD Nov 94:Sample Code:AppsToGo:DTS.Lib:AppleTalk.c  The sample Kibitz uses `AddPPCNBPAlias` and `RemoveNBPAlias` to allow filtering to only systems that are running a copy of Kibitz, so you can use the Kibitz source code as an example. |

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
