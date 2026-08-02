---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/QuickLook.html
archived_at: '2026-07-18T02:54:58.430216Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# QuickLook Changes for Objective-C

### QuickLook

#### QLPreviewController.h

Added [-[QLPreviewControllerDelegate previewController:transitionViewForPreviewItem:]](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/1648425-previewcontroller)Modified [QLPreviewController.dataSource](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/1617020-datasource)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak) id<QLPreviewControllerDataSource> dataSource ``` |
| To | ``` @property(nonatomic, weak) id<QLPreviewControllerDataSource> dataSource ``` |

Modified [QLPreviewController.delegate](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/1617005-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak) id<QLPreviewControllerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak) id<QLPreviewControllerDelegate> delegate ``` |

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
