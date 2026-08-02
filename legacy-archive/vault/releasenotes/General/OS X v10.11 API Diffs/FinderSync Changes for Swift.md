---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/FinderSync.html
archived_at: '2026-07-18T02:53:32.695652Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# FinderSync Changes for Swift

### FinderSync

Modified [FIFinderSync](https://developer.apple.com/documentation/findersync/fifindersync)

|  | Declaration |
| --- | --- |
| From | ``` class FIFinderSync : NSObject, FIFinderSyncProtocol, NSExtensionRequestHandling, NSObjectProtocol { } ``` |
| To | ``` class FIFinderSync : NSObject, FIFinderSyncProtocol, NSExtensionRequestHandling { } ``` |

Modified [FIFinderSyncController](https://developer.apple.com/documentation/findersync/fifindersynccontroller)

|  | Declaration |
| --- | --- |
| From | ``` class FIFinderSyncController : NSExtensionContext {     class func defaultController() -> Self!     var directoryURLs: Set<NSObject>!     func setBadgeImage(_ image: NSImage!, label label: String!, forBadgeIdentifier badgeID: String!)     func setBadgeIdentifier(_ badgeID: String!, forURL url: NSURL!)     func targetedURL() -> NSURL!     func selectedItemURLs() -> [AnyObject]! } ``` |
| To | ``` class FIFinderSyncController : NSExtensionContext {     class func defaultController() -> Self     var directoryURLs: Set<NSURL>!     func setBadgeImage(_ image: NSImage, label label: String?, forBadgeIdentifier badgeID: String)     func setBadgeIdentifier(_ badgeID: String, forURL url: NSURL)     func targetedURL() -> NSURL?     func selectedItemURLs() -> [NSURL]? } ``` |

Modified [FIFinderSyncController.defaultController() -> Self [class]](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501588-defaultcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultController() -> Self! ``` |
| To | ``` class func defaultController() -> Self ``` |

Modified [FIFinderSyncController.directoryURLs](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501579-directoryurls)

|  | Declaration |
| --- | --- |
| From | ``` var directoryURLs: Set<NSObject>! ``` |
| To | ``` var directoryURLs: Set<NSURL>! ``` |

Modified [FIFinderSyncController.selectedItemURLs() -> [NSURL]?](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501575-selecteditemurls)

|  | Declaration |
| --- | --- |
| From | ``` func selectedItemURLs() -> [AnyObject]! ``` |
| To | ``` func selectedItemURLs() -> [NSURL]? ``` |

Modified [FIFinderSyncController.setBadgeIdentifier(_: String, forURL: NSURL)](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501577-setbadgeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func setBadgeIdentifier(_ badgeID: String!, forURL url: NSURL!) ``` |
| To | ``` func setBadgeIdentifier(_ badgeID: String, forURL url: NSURL) ``` |

Modified [FIFinderSyncController.setBadgeImage(_: NSImage, label: String?, forBadgeIdentifier: String)](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501583-setbadgeimage)

|  | Declaration |
| --- | --- |
| From | ``` func setBadgeImage(_ image: NSImage!, label label: String!, forBadgeIdentifier badgeID: String!) ``` |
| To | ``` func setBadgeImage(_ image: NSImage, label label: String?, forBadgeIdentifier badgeID: String) ``` |

Modified [FIFinderSyncController.targetedURL() -> NSURL?](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501595-targetedurl)

|  | Declaration |
| --- | --- |
| From | ``` func targetedURL() -> NSURL! ``` |
| To | ``` func targetedURL() -> NSURL? ``` |

Modified [FIFinderSyncProtocol](https://developer.apple.com/documentation/findersync/fifindersyncprotocol)

|  | Declaration |
| --- | --- |
| From | ``` protocol FIFinderSyncProtocol {     optional func menuForMenuKind(_ menu: FIMenuKind) -> NSMenu!     optional func beginObservingDirectoryAtURL(_ url: NSURL!)     optional func endObservingDirectoryAtURL(_ url: NSURL!)     optional func requestBadgeIdentifierForURL(_ url: NSURL!)     optional var toolbarItemName: String! { get }     @NSCopying optional var toolbarItemImage: NSImage! { get }     optional var toolbarItemToolTip: String! { get } } ``` |
| To | ``` protocol FIFinderSyncProtocol {     optional func menuForMenuKind(_ menu: FIMenuKind) -> NSMenu?     optional func beginObservingDirectoryAtURL(_ url: NSURL)     optional func endObservingDirectoryAtURL(_ url: NSURL)     optional func requestBadgeIdentifierForURL(_ url: NSURL)     optional var toolbarItemName: String { get }     @NSCopying optional var toolbarItemImage: NSImage { get }     optional var toolbarItemToolTip: String { get } } ``` |

Modified [FIFinderSyncProtocol.beginObservingDirectoryAtURL(_: NSURL)](https://developer.apple.com/documentation/findersync/1501586-fifindersync/1501578-beginobservingdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` optional func beginObservingDirectoryAtURL(_ url: NSURL!) ``` |
| To | ``` optional func beginObservingDirectoryAtURL(_ url: NSURL) ``` |

Modified [FIFinderSyncProtocol.endObservingDirectoryAtURL(_: NSURL)](https://developer.apple.com/documentation/findersync/1501586-fifindersync/1501582-endobservingdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` optional func endObservingDirectoryAtURL(_ url: NSURL!) ``` |
| To | ``` optional func endObservingDirectoryAtURL(_ url: NSURL) ``` |

Modified [FIFinderSyncProtocol.menuForMenuKind(_: FIMenuKind) -> NSMenu?](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/1501585-menu)

|  | Declaration |
| --- | --- |
| From | ``` optional func menuForMenuKind(_ menu: FIMenuKind) -> NSMenu! ``` |
| To | ``` optional func menuForMenuKind(_ menu: FIMenuKind) -> NSMenu? ``` |

Modified [FIFinderSyncProtocol.requestBadgeIdentifierForURL(_: NSURL)](https://developer.apple.com/documentation/findersync/1501586-fifindersync/1501589-requestbadgeidentifierforurl)

|  | Declaration |
| --- | --- |
| From | ``` optional func requestBadgeIdentifierForURL(_ url: NSURL!) ``` |
| To | ``` optional func requestBadgeIdentifierForURL(_ url: NSURL) ``` |

Modified [FIFinderSyncProtocol.toolbarItemImage](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/1501580-toolbaritemimage)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying optional var toolbarItemImage: NSImage! { get } ``` |
| To | ``` @NSCopying optional var toolbarItemImage: NSImage { get } ``` |

Modified [FIFinderSyncProtocol.toolbarItemName](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/1501574-toolbaritemname)

|  | Declaration |
| --- | --- |
| From | ``` optional var toolbarItemName: String! { get } ``` |
| To | ``` optional var toolbarItemName: String { get } ``` |

Modified [FIFinderSyncProtocol.toolbarItemToolTip](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/1501590-toolbaritemtooltip)

|  | Declaration |
| --- | --- |
| From | ``` optional var toolbarItemToolTip: String! { get } ``` |
| To | ``` optional var toolbarItemToolTip: String { get } ``` |

Modified [FIMenuKind [enum]](https://developer.apple.com/documentation/findersync/fimenukind)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

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
