---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/QuickLook.html
archived_at: '2026-07-18T02:56:57.705095Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# QuickLook Changes for Swift

### QuickLook

Modified [QLPreviewController](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class QLPreviewController : UIViewController {     class func canPreviewItem(_ item: QLPreviewItem!) -> Bool     unowned(unsafe) var dataSource: QLPreviewControllerDataSource!     func reloadData()     func refreshCurrentPreviewItem()     var currentPreviewItemIndex: Int     var currentPreviewItem: QLPreviewItem! { get }     unowned(unsafe) var delegate: QLPreviewControllerDelegate! } ``` |
| To | ``` class QLPreviewController : UIViewController {     class func canPreviewItem(_ item: QLPreviewItem) -> Bool     weak var dataSource: QLPreviewControllerDataSource?     func reloadData()     func refreshCurrentPreviewItem()     var currentPreviewItemIndex: Int     var currentPreviewItem: QLPreviewItem? { get }     weak var delegate: QLPreviewControllerDelegate? } ``` |

Modified [QLPreviewController.canPreviewItem(_: QLPreviewItem) -> Bool [class]](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/1617016-canpreviewitem)

|  | Declaration |
| --- | --- |
| From | ``` class func canPreviewItem(_ item: QLPreviewItem!) -> Bool ``` |
| To | ``` class func canPreviewItem(_ item: QLPreviewItem) -> Bool ``` |

Modified [QLPreviewController.currentPreviewItem](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/1617013-currentpreviewitem)

|  | Declaration |
| --- | --- |
| From | ``` var currentPreviewItem: QLPreviewItem! { get } ``` |
| To | ``` var currentPreviewItem: QLPreviewItem? { get } ``` |

Modified [QLPreviewController.dataSource](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/1617020-datasource)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var dataSource: QLPreviewControllerDataSource! ``` |
| To | ``` weak var dataSource: QLPreviewControllerDataSource? ``` |

Modified [QLPreviewController.delegate](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/1617005-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: QLPreviewControllerDelegate! ``` |
| To | ``` weak var delegate: QLPreviewControllerDelegate? ``` |

Modified [QLPreviewControllerDataSource](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdatasource)

|  | Declaration |
| --- | --- |
| From | ``` protocol QLPreviewControllerDataSource {     func numberOfPreviewItemsInPreviewController(_ controller: QLPreviewController!) -> Int     func previewController(_ controller: QLPreviewController!, previewItemAtIndex index: Int) -> QLPreviewItem! } ``` |
| To | ``` protocol QLPreviewControllerDataSource {     func numberOfPreviewItemsInPreviewController(_ controller: QLPreviewController) -> Int     func previewController(_ controller: QLPreviewController, previewItemAtIndex index: Int) -> QLPreviewItem } ``` |

Modified [QLPreviewControllerDataSource.numberOfPreviewItemsInPreviewController(_: QLPreviewController) -> Int](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdatasource/1617017-numberofpreviewitems)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func numberOfPreviewItemsInPreviewController(_ controller: QLPreviewController!) -> Int ``` | iOS 8.0 |
| To | ``` func numberOfPreviewItemsInPreviewController(_ controller: QLPreviewController) -> Int ``` | iOS 4.0 |

Modified [QLPreviewControllerDataSource.previewController(_: QLPreviewController, previewItemAtIndex: Int) -> QLPreviewItem](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdatasource/1617006-previewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func previewController(_ controller: QLPreviewController!, previewItemAtIndex index: Int) -> QLPreviewItem! ``` | iOS 8.0 |
| To | ``` func previewController(_ controller: QLPreviewController, previewItemAtIndex index: Int) -> QLPreviewItem ``` | iOS 4.0 |

Modified [QLPreviewControllerDelegate](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol QLPreviewControllerDelegate : NSObjectProtocol {     optional func previewControllerWillDismiss(_ controller: QLPreviewController!)     optional func previewControllerDidDismiss(_ controller: QLPreviewController!)     optional func previewController(_ controller: QLPreviewController!, shouldOpenURL url: NSURL!, forPreviewItem item: QLPreviewItem!) -> Bool     optional func previewController(_ controller: QLPreviewController!, frameForPreviewItem item: QLPreviewItem!, inSourceView view: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect     optional func previewController(_ controller: QLPreviewController!, transitionImageForPreviewItem item: QLPreviewItem!, contentRect contentRect: UnsafeMutablePointer<CGRect>) -> UIImage! } ``` |
| To | ``` protocol QLPreviewControllerDelegate : NSObjectProtocol {     optional func previewControllerWillDismiss(_ controller: QLPreviewController)     optional func previewControllerDidDismiss(_ controller: QLPreviewController)     optional func previewController(_ controller: QLPreviewController, shouldOpenURL url: NSURL, forPreviewItem item: QLPreviewItem) -> Bool     optional func previewController(_ controller: QLPreviewController, frameForPreviewItem item: QLPreviewItem, inSourceView view: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect     optional func previewController(_ controller: QLPreviewController, transitionImageForPreviewItem item: QLPreviewItem, contentRect contentRect: UnsafeMutablePointer<CGRect>) -> UIImage } ``` |

Modified [QLPreviewControllerDelegate.previewController(_: QLPreviewController, frameForPreviewItem: QLPreviewItem, inSourceView: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/1617007-previewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func previewController(_ controller: QLPreviewController!, frameForPreviewItem item: QLPreviewItem!, inSourceView view: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect ``` | iOS 8.0 |
| To | ``` optional func previewController(_ controller: QLPreviewController, frameForPreviewItem item: QLPreviewItem, inSourceView view: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect ``` | iOS 4.0 |

Modified [QLPreviewControllerDelegate.previewController(_: QLPreviewController, shouldOpenURL: NSURL, forPreviewItem: QLPreviewItem) -> Bool](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/1617018-previewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func previewController(_ controller: QLPreviewController!, shouldOpenURL url: NSURL!, forPreviewItem item: QLPreviewItem!) -> Bool ``` | iOS 8.0 |
| To | ``` optional func previewController(_ controller: QLPreviewController, shouldOpenURL url: NSURL, forPreviewItem item: QLPreviewItem) -> Bool ``` | iOS 4.0 |

Modified [QLPreviewControllerDelegate.previewController(_: QLPreviewController, transitionImageForPreviewItem: QLPreviewItem, contentRect: UnsafeMutablePointer<CGRect>) -> UIImage](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/1617021-previewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func previewController(_ controller: QLPreviewController!, transitionImageForPreviewItem item: QLPreviewItem!, contentRect contentRect: UnsafeMutablePointer<CGRect>) -> UIImage! ``` | iOS 8.0 |
| To | ``` optional func previewController(_ controller: QLPreviewController, transitionImageForPreviewItem item: QLPreviewItem, contentRect contentRect: UnsafeMutablePointer<CGRect>) -> UIImage ``` | iOS 4.0 |

Modified [QLPreviewControllerDelegate.previewControllerDidDismiss(_: QLPreviewController)](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/1617015-previewcontrollerdiddismiss)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func previewControllerDidDismiss(_ controller: QLPreviewController!) ``` | iOS 8.0 |
| To | ``` optional func previewControllerDidDismiss(_ controller: QLPreviewController) ``` | iOS 4.0 |

Modified [QLPreviewControllerDelegate.previewControllerWillDismiss(_: QLPreviewController)](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/1617014-previewcontrollerwilldismiss)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func previewControllerWillDismiss(_ controller: QLPreviewController!) ``` | iOS 8.0 |
| To | ``` optional func previewControllerWillDismiss(_ controller: QLPreviewController) ``` | iOS 4.0 |

Modified [QLPreviewItem](https://developer.apple.com/documentation/quartz/qlpreviewitem)

|  | Declaration |
| --- | --- |
| From | ``` protocol QLPreviewItem : NSObjectProtocol {     var previewItemURL: NSURL! { get }     optional var previewItemTitle: String! { get } } ``` |
| To | ``` protocol QLPreviewItem : NSObjectProtocol {     var previewItemURL: NSURL { get }     optional var previewItemTitle: String? { get } } ``` |

Modified [QLPreviewItem.previewItemTitle](https://developer.apple.com/documentation/quartz/qlpreviewitem/1419911-previewitemtitle)

|  | Declaration |
| --- | --- |
| From | ``` optional var previewItemTitle: String! { get } ``` |
| To | ``` optional var previewItemTitle: String? { get } ``` |

Modified [QLPreviewItem.previewItemURL](https://developer.apple.com/documentation/quicklook/qlpreviewitem/1419913-previewitemurl)

|  | Declaration |
| --- | --- |
| From | ``` var previewItemURL: NSURL! { get } ``` |
| To | ``` var previewItemURL: NSURL { get } ``` |

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
