---
title: iOS 9.2 API Diffs
apple_id: TP40016605
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS92APIDiffs/Swift/UIKit.html
archived_at: '2026-07-18T02:57:12.948214Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.2 API Diffs](iOS%209.1%20to%20iOS%209.2%20API%20Differences.md)


# UIKit Changes for Swift

### UIKit

Modified [UICollectionViewUpdateItem](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionViewUpdateItem : NSObject {     var indexPathBeforeUpdate: NSIndexPath { get }     var indexPathAfterUpdate: NSIndexPath { get }     var updateAction: UICollectionUpdateAction { get } } ``` |
| To | ``` class UICollectionViewUpdateItem : NSObject {     var indexPathBeforeUpdate: NSIndexPath? { get }     var indexPathAfterUpdate: NSIndexPath? { get }     var updateAction: UICollectionUpdateAction { get } } ``` |

Modified [UICollectionViewUpdateItem.indexPathAfterUpdate](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/1617765-indexpathafterupdate)

|  | Declaration |
| --- | --- |
| From | ``` var indexPathAfterUpdate: NSIndexPath { get } ``` |
| To | ``` var indexPathAfterUpdate: NSIndexPath? { get } ``` |

Modified [UICollectionViewUpdateItem.indexPathBeforeUpdate](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/1617772-indexpathbeforeupdate)

|  | Declaration |
| --- | --- |
| From | ``` var indexPathBeforeUpdate: NSIndexPath { get } ``` |
| To | ``` var indexPathBeforeUpdate: NSIndexPath? { get } ``` |

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
