---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/SafariServices.html
archived_at: '2026-07-18T02:56:36.443652Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# SafariServices Changes for Objective-C

### SafariServices

#### SFContentBlockerManager.h (Added)

Added [SFContentBlockerManager](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager)Added [+[SFContentBlockerManager reloadContentBlockerWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/1620151-reloadcontentblocker)Added [SFContentBlockerErrorCode](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode)Added [SFContentBlockerErrorDomain](https://developer.apple.com/documentation/safariservices/sfcontentblockererrordomain)Added [SFContentBlockerLoadingInterrupted](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/loadinginterrupted)Added [SFContentBlockerNoAttachmentFound](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/sfcontentblockernoattachmentfound)Added [SFContentBlockerNoExtensionFound](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/sfcontentblockernoextensionfound)

#### SFFoundation.h (Added)

Added #def SF_EXTERN

#### SFSafariViewController.h (Added)

Added [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller)Added [SFSafariViewController.delegate](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1621219-delegate)Added [-[SFSafariViewController initWithURL:]](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1621222-initwithurl)Added [-[SFSafariViewController initWithURL:entersReaderIfAvailable:]](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1621221-initwithurl)Added [SFSafariViewControllerDelegate](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate)Added [-[SFSafariViewControllerDelegate safariViewController:activityItemsForURL:title:]](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/1621216-safariviewcontroller)Added [-[SFSafariViewControllerDelegate safariViewController:didCompleteInitialLoad:]](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/1621215-safariviewcontroller)Added [-[SFSafariViewControllerDelegate safariViewControllerDidFinish:]](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/1621214-safariviewcontrollerdidfinish)

#### SSReadingList.h

Modified [+[SSReadingList defaultReadingList]](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621220-defaultreadinglist)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)defaultReadingList ``` |
| To | ``` + (SSReadingList * _Nullable)defaultReadingList ``` |

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
