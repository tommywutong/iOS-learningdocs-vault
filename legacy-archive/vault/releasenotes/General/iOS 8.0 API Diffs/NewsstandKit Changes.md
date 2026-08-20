---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/NewsstandKit.html
archived_at: '2026-07-18T02:55:59.487838Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# NewsstandKit Changes

## NewsstandKit

NKAssetDownload.hModified [NKAssetDownload.issue](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615800-issue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) NKIssue *issue ``` |
| To | ``` @property(readonly, weak) NKIssue *issue ``` |

Modified [NKAssetDownload.userInfo](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615811-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSDictionary *userInfo ``` |
| To | ``` @property(copy) NSDictionary *userInfo ``` |

NKIssue.hModified [NKIssue.contentURL](https://developer.apple.com/documentation/newsstandkit/nkissue/1615813-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *contentURL ``` |
| To | ``` @property(readonly, copy) NSURL *contentURL ``` |

NKLibrary.hModified [NKLibrary.currentlyReadingIssue](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615812-currentlyreadingissue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, retain) NKIssue *currentlyReadingIssue ``` |
| To | ``` @property(strong) NKIssue *currentlyReadingIssue ``` |

Modified [NKLibrary.downloadingAssets](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615806-downloadingassets)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSArray *downloadingAssets ``` |
| To | ``` @property(readonly, strong) NSArray *downloadingAssets ``` |

Modified [NKLibrary.issues](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615803-issues)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSArray *issues ``` |
| To | ``` @property(readonly, strong) NSArray *issues ``` |

NKNSURLConnectionAdditions.hModified [NSURLConnection.newsstandAssetDownload](https://developer.apple.com/documentation/foundation/nsurlconnection/1615799-newsstandassetdownload)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NKAssetDownload *newsstandAssetDownload ``` |
| To | ``` @property(readonly, weak) NKAssetDownload *newsstandAssetDownload ``` |

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
