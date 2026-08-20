---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/NotificationCenter.html
archived_at: '2026-07-18T02:56:56.339119Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# NotificationCenter Changes for Swift

### NotificationCenter

Modified [NCUpdateResult [enum]](https://developer.apple.com/documentation/notificationcenter/ncupdateresult)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NCWidgetController](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class NCWidgetController : NSObject {     class func widgetController() -> Self!     func setHasContent(_ flag: Bool, forWidgetWithBundleIdentifier bundleID: String!) } ``` |
| To | ``` class NCWidgetController : NSObject {     class func widgetController() -> Self     func setHasContent(_ flag: Bool, forWidgetWithBundleIdentifier bundleID: String) } ``` |

Modified [NCWidgetController.setHasContent(_: Bool, forWidgetWithBundleIdentifier: String)](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller/1456693-sethascontent)

|  | Declaration |
| --- | --- |
| From | ``` func setHasContent(_ flag: Bool, forWidgetWithBundleIdentifier bundleID: String!) ``` |
| To | ``` func setHasContent(_ flag: Bool, forWidgetWithBundleIdentifier bundleID: String) ``` |

Modified [NCWidgetController.widgetController() -> Self [class]](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller/1456687-widgetcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class func widgetController() -> Self! ``` |
| To | ``` class func widgetController() -> Self ``` |

Modified [NCWidgetProviding](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding)

|  | Declaration |
| --- | --- |
| From | ``` protocol NCWidgetProviding : NSObjectProtocol {     optional func widgetPerformUpdateWithCompletionHandler(_ completionHandler: ((NCUpdateResult) -> Void)!)     optional func widgetMarginInsetsForProposedMarginInsets(_ defaultMarginInsets: UIEdgeInsets) -> UIEdgeInsets } ``` |
| To | ``` protocol NCWidgetProviding : NSObjectProtocol {     optional func widgetPerformUpdateWithCompletionHandler(_ completionHandler: (NCUpdateResult) -> Void)     optional func widgetMarginInsetsForProposedMarginInsets(_ defaultMarginInsets: UIEdgeInsets) -> UIEdgeInsets } ``` |

Modified [NCWidgetProviding.widgetPerformUpdateWithCompletionHandler(_: (NCUpdateResult) -> Void)](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490262-widgetperformupdatewithcompletio)

|  | Declaration |
| --- | --- |
| From | ``` optional func widgetPerformUpdateWithCompletionHandler(_ completionHandler: ((NCUpdateResult) -> Void)!) ``` |
| To | ``` optional func widgetPerformUpdateWithCompletionHandler(_ completionHandler: (NCUpdateResult) -> Void) ``` |

Modified [UIVibrancyEffect.notificationCenterVibrancyEffect() -> UIVibrancyEffect [class]](https://developer.apple.com/documentation/uikit/uivibrancyeffect/1613917-notificationcentervibrancyeffect)

|  | Declaration |
| --- | --- |
| From | ``` class func notificationCenterVibrancyEffect() -> UIVibrancyEffect! ``` |
| To | ``` class func notificationCenterVibrancyEffect() -> UIVibrancyEffect ``` |

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
