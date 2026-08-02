---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/SafariServices.html
archived_at: '2026-07-18T02:54:58.595063Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# SafariServices Changes for Objective-C

### SafariServices

#### SFContentBlockerManager.h

Added [+[SFContentBlockerManager getStateOfContentBlockerWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/1639499-getstateofcontentblocker)Modified [SFContentBlockerErrorDomain](https://developer.apple.com/documentation/safariservices/sfcontentblockererrordomain)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [SFContentBlockerLoadingInterrupted](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/loadinginterrupted)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [SFContentBlockerNoAttachmentFound](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/sfcontentblockernoattachmentfound)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [SFContentBlockerNoExtensionFound](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/sfcontentblockernoextensionfound)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### SFContentBlockerState.h (Added)

Added [SFContentBlockerState](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate)Added [SFContentBlockerState.enabled](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate/1639520-enabled)

#### SFError.h (Added)

Added [SFErrorCode](https://developer.apple.com/documentation/safariservices/sferrorcode)Added [SFErrorDomain](https://developer.apple.com/documentation/safariservices/sferrordomain)Added [SFErrorLoadingInterrupted](https://developer.apple.com/documentation/safariservices/sferror/code/loadinginterrupted)Added [SFErrorNoAttachmentFound](https://developer.apple.com/documentation/safariservices/sferrorcode/sferrornoattachmentfound)Added [SFErrorNoExtensionFound](https://developer.apple.com/documentation/safariservices/sferrorcode/sferrornoextensionfound)

#### SFSafariViewController.h

Added [SFSafariViewController.preferredBarTintColor](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/2274394-preferredbartintcolor)Added [SFSafariViewController.preferredControlTintColor](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/2274393-preferredcontroltintcolor)

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
