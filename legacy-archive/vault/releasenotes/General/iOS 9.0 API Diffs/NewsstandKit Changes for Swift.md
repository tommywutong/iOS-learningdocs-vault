---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/NewsstandKit.html
archived_at: '2026-07-18T02:56:56.268220Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# NewsstandKit Changes for Swift

### NewsstandKit

Modified [NKAssetDownload](https://developer.apple.com/documentation/newsstandkit/nkassetdownload)

|  | Declaration |
| --- | --- |
| From | ``` class NKAssetDownload : NSObject {     weak var issue: NKIssue! { get }     var identifier: String! { get }     var userInfo: [NSObject : AnyObject]!     @NSCopying var URLRequest: NSURLRequest! { get }     func downloadWithDelegate(_ delegate: NSURLConnectionDownloadDelegate!) -> NSURLConnection! } ``` |
| To | ``` class NKAssetDownload : NSObject {     weak var issue: NKIssue? { get }     var identifier: String { get }     var userInfo: [NSObject : AnyObject]?     @NSCopying var URLRequest: NSURLRequest { get }     func downloadWithDelegate(_ delegate: NSURLConnectionDownloadDelegate) -> NSURLConnection } ``` |

Modified [NKAssetDownload.downloadWithDelegate(_: NSURLConnectionDownloadDelegate) -> NSURLConnection](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615792-download)

|  | Declaration |
| --- | --- |
| From | ``` func downloadWithDelegate(_ delegate: NSURLConnectionDownloadDelegate!) -> NSURLConnection! ``` |
| To | ``` func downloadWithDelegate(_ delegate: NSURLConnectionDownloadDelegate) -> NSURLConnection ``` |

Modified [NKAssetDownload.identifier](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615807-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String { get } ``` |

Modified [NKAssetDownload.issue](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615800-issue)

|  | Declaration |
| --- | --- |
| From | ``` weak var issue: NKIssue! { get } ``` |
| To | ``` weak var issue: NKIssue? { get } ``` |

Modified [NKAssetDownload.URLRequest](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615802-urlrequest)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URLRequest: NSURLRequest! { get } ``` |
| To | ``` @NSCopying var URLRequest: NSURLRequest { get } ``` |

Modified [NKAssetDownload.userInfo](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615811-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

Modified [NKIssue](https://developer.apple.com/documentation/newsstandkit/nkissue)

|  | Declaration |
| --- | --- |
| From | ``` class NKIssue : NSObject {     var downloadingAssets: [AnyObject]! { get }     @NSCopying var contentURL: NSURL! { get }     var status: NKIssueContentStatus { get }     var name: String! { get }     @NSCopying var date: NSDate! { get }     func addAssetWithRequest(_ request: NSURLRequest!) -> NKAssetDownload! } ``` |
| To | ``` class NKIssue : NSObject {     var downloadingAssets: [NKAssetDownload] { get }     @NSCopying var contentURL: NSURL { get }     var status: NKIssueContentStatus { get }     var name: String { get }     @NSCopying var date: NSDate { get }     func addAssetWithRequest(_ request: NSURLRequest) -> NKAssetDownload } ``` |

Modified [NKIssue.addAssetWithRequest(_: NSURLRequest) -> NKAssetDownload](https://developer.apple.com/documentation/newsstandkit/nkissue/1615794-addasset)

|  | Declaration |
| --- | --- |
| From | ``` func addAssetWithRequest(_ request: NSURLRequest!) -> NKAssetDownload! ``` |
| To | ``` func addAssetWithRequest(_ request: NSURLRequest) -> NKAssetDownload ``` |

Modified [NKIssue.contentURL](https://developer.apple.com/documentation/newsstandkit/nkissue/1615813-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var contentURL: NSURL! { get } ``` |
| To | ``` @NSCopying var contentURL: NSURL { get } ``` |

Modified [NKIssue.date](https://developer.apple.com/documentation/newsstandkit/nkissue/1615809-date)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var date: NSDate! { get } ``` |
| To | ``` @NSCopying var date: NSDate { get } ``` |

Modified [NKIssue.downloadingAssets](https://developer.apple.com/documentation/newsstandkit/nkissue/1615791-downloadingassets)

|  | Declaration |
| --- | --- |
| From | ``` var downloadingAssets: [AnyObject]! { get } ``` |
| To | ``` var downloadingAssets: [NKAssetDownload] { get } ``` |

Modified [NKIssue.name](https://developer.apple.com/documentation/newsstandkit/nkissue/1615789-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [NKIssueContentStatus [enum]](https://developer.apple.com/documentation/newsstandkit/nkissuecontentstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NKLibrary](https://developer.apple.com/documentation/newsstandkit/nklibrary)

|  | Declaration |
| --- | --- |
| From | ``` class NKLibrary : NSObject {     var issues: [AnyObject]! { get }     var downloadingAssets: [AnyObject]! { get }     var currentlyReadingIssue: NKIssue!     class func sharedLibrary() -> NKLibrary!     func issueWithName(_ name: String!) -> NKIssue!     func addIssueWithName(_ name: String!, date date: NSDate!) -> NKIssue!     func removeIssue(_ issue: NKIssue!) } ``` |
| To | ``` class NKLibrary : NSObject {     var issues: [NKIssue] { get }     var downloadingAssets: [NKAssetDownload] { get }     var currentlyReadingIssue: NKIssue?     class func sharedLibrary() -> NKLibrary?     func issueWithName(_ name: String) -> NKIssue?     func addIssueWithName(_ name: String, date date: NSDate) -> NKIssue     func removeIssue(_ issue: NKIssue) } ``` |

Modified [NKLibrary.addIssueWithName(_: String, date: NSDate) -> NKIssue](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615804-addissuewithname)

|  | Declaration |
| --- | --- |
| From | ``` func addIssueWithName(_ name: String!, date date: NSDate!) -> NKIssue! ``` |
| To | ``` func addIssueWithName(_ name: String, date date: NSDate) -> NKIssue ``` |

Modified [NKLibrary.currentlyReadingIssue](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615812-currentlyreadingissue)

|  | Declaration |
| --- | --- |
| From | ``` var currentlyReadingIssue: NKIssue! ``` |
| To | ``` var currentlyReadingIssue: NKIssue? ``` |

Modified [NKLibrary.downloadingAssets](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615806-downloadingassets)

|  | Declaration |
| --- | --- |
| From | ``` var downloadingAssets: [AnyObject]! { get } ``` |
| To | ``` var downloadingAssets: [NKAssetDownload] { get } ``` |

Modified [NKLibrary.issues](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615803-issues)

|  | Declaration |
| --- | --- |
| From | ``` var issues: [AnyObject]! { get } ``` |
| To | ``` var issues: [NKIssue] { get } ``` |

Modified [NKLibrary.issueWithName(_: String) -> NKIssue?](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615796-issue)

|  | Declaration |
| --- | --- |
| From | ``` func issueWithName(_ name: String!) -> NKIssue! ``` |
| To | ``` func issueWithName(_ name: String) -> NKIssue? ``` |

Modified [NKLibrary.removeIssue(_: NKIssue)](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615810-removeissue)

|  | Declaration |
| --- | --- |
| From | ``` func removeIssue(_ issue: NKIssue!) ``` |
| To | ``` func removeIssue(_ issue: NKIssue) ``` |

Modified [NKLibrary.sharedLibrary() -> NKLibrary? [class]](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615801-sharedlibrary)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedLibrary() -> NKLibrary! ``` |
| To | ``` class func sharedLibrary() -> NKLibrary? ``` |

Modified [NSURLConnection.newsstandAssetDownload](https://developer.apple.com/documentation/foundation/nsurlconnection/1615799-newsstandassetdownload)

|  | Declaration |
| --- | --- |
| From | ``` weak var newsstandAssetDownload: NKAssetDownload! { get } ``` |
| To | ``` weak var newsstandAssetDownload: NKAssetDownload? { get } ``` |

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
