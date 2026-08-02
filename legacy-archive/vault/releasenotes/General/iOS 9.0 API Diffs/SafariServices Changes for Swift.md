---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/SafariServices.html
archived_at: '2026-07-18T02:56:57.849649Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# SafariServices Changes for Swift

### SafariServices

Added [SFContentBlockerErrorCode [enum]](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode)Added [SFContentBlockerErrorCode.LoadingInterrupted](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/sfcontentblockerloadinginterrupted)Added [SFContentBlockerErrorCode.NoAttachmentFound](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/noattachmentfound)Added [SFContentBlockerErrorCode.NoExtensionFound](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/sfcontentblockernoextensionfound)Added [SFContentBlockerManager](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager)Added [SFContentBlockerManager.reloadContentBlockerWithIdentifier(_: String, completionHandler: ((NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/1620151-reloadcontentblocker)Added [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller)Added [SFSafariViewController.delegate](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1621219-delegate)Added [SFSafariViewController.init(URL: NSURL)](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1621222-initwithurl)Added [SFSafariViewController.init(URL: NSURL, entersReaderIfAvailable: Bool)](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1621221-init)Added [SFSafariViewControllerDelegate](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate)Added [SFSafariViewControllerDelegate.safariViewController(_: SFSafariViewController, activityItemsForURL: NSURL, title: String?) -> [UIActivity]](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/1621216-safariviewcontroller)Added [SFSafariViewControllerDelegate.safariViewController(_: SFSafariViewController, didCompleteInitialLoad: Bool)](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/1621215-safariviewcontroller)Added [SFSafariViewControllerDelegate.safariViewControllerDidFinish(_: SFSafariViewController)](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/1621214-safariviewcontrollerdidfinish)Added [SFContentBlockerErrorDomain](https://developer.apple.com/documentation/safariservices/sfcontentblockererrordomain)Modified [SSReadingList](https://developer.apple.com/documentation/safariservices/ssreadinglist)

|  | Declaration |
| --- | --- |
| From | ``` class SSReadingList : NSObject {     class func defaultReadingList() -> Self!     init!()     class func supportsURL(_ URL: NSURL!) -> Bool     func addReadingListItemWithURL(_ URL: NSURL!, title title: String!, previewText previewText: String!, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class SSReadingList : NSObject {     class func defaultReadingList() -> SSReadingList?     init()     class func supportsURL(_ URL: NSURL) -> Bool     func addReadingListItemWithURL(_ URL: NSURL, title title: String?, previewText previewText: String?) throws } ``` |

Modified [SSReadingList.addReadingListItemWithURL(_: NSURL, title: String?, previewText: String?) throws](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621226-additem)

|  | Declaration |
| --- | --- |
| From | ``` func addReadingListItemWithURL(_ URL: NSURL!, title title: String!, previewText previewText: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func addReadingListItemWithURL(_ URL: NSURL, title title: String?, previewText previewText: String?) throws ``` |

Modified [SSReadingList.defaultReadingList() -> SSReadingList? [class]](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621220-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultReadingList() -> Self! ``` |
| To | ``` class func defaultReadingList() -> SSReadingList? ``` |

Modified [SSReadingList.supportsURL(_: NSURL) -> Bool [class]](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621224-supportsurl)

|  | Declaration |
| --- | --- |
| From | ``` class func supportsURL(_ URL: NSURL!) -> Bool ``` |
| To | ``` class func supportsURL(_ URL: NSURL) -> Bool ``` |

Modified [SSReadingListErrorCode [enum]](https://developer.apple.com/documentation/safariservices/ssreadinglisterror/code)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

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
