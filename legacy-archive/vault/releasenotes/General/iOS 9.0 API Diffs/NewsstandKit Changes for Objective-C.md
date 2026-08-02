---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/NewsstandKit.html
archived_at: '2026-07-18T02:56:35.956292Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# NewsstandKit Changes for Objective-C

### NewsstandKit

#### NKIssue.h

Modified [NKIssue.downloadingAssets](https://developer.apple.com/documentation/newsstandkit/nkissue/1615791-downloadingassets)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *downloadingAssets ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NKAssetDownload *> *downloadingAssets ``` |

#### NKLibrary.h

Modified [NKLibrary.downloadingAssets](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615806-downloadingassets)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSArray *downloadingAssets ``` |
| To | ``` @property(readonly, strong, nonnull) NSArray<NKAssetDownload *> *downloadingAssets ``` |

Modified [NKLibrary.issues](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615803-issues)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSArray *issues ``` |
| To | ``` @property(readonly, strong, nonnull) NSArray<NKIssue *> *issues ``` |

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
