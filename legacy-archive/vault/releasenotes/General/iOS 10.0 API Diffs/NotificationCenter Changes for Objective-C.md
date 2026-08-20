---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/NotificationCenter.html
archived_at: '2026-07-18T02:54:57.825207Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# NotificationCenter Changes for Objective-C

### NotificationCenter

#### NCWidgetProviding.h

Removed UIVibrancyEffect(NotificationCenter)Added [-[NCWidgetProviding widgetActiveDisplayModeDidChange:withMaximumSize:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1649132-widgetactivedisplaymodedidchange)Added [NSExtensionContext.widgetActiveDisplayMode](https://developer.apple.com/documentation/foundation/nsextensioncontext/1649134-widgetactivedisplaymode)Added [NSExtensionContext.widgetLargestAvailableDisplayMode](https://developer.apple.com/documentation/foundation/nsextensioncontext/1649133-widgetlargestavailabledisplaymod)Added [-[NSExtensionContext widgetMaximumSizeForDisplayMode:]](https://developer.apple.com/documentation/foundation/nsextensioncontext/1649135-widgetmaximumsize)Added [+[UIVibrancyEffect widgetPrimaryVibrancyEffect]](https://developer.apple.com/documentation/uikit/uivibrancyeffect/1771278-widgetprimaryvibrancyeffect)Added [+[UIVibrancyEffect widgetSecondaryVibrancyEffect]](https://developer.apple.com/documentation/uikit/uivibrancyeffect/1771277-widgetsecondaryvibrancyeffect)Added NSExtensionContext(NCWidgetAdditions)Added UIVibrancyEffect(NCWidgetAdditions)Added UIVibrancyEffect(NCWidgetDeprecated)Modified [-[NCWidgetProviding widgetMarginInsetsForProposedMarginInsets:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490248-widgetmargininsets)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [+[UIVibrancyEffect notificationCenterVibrancyEffect]](https://developer.apple.com/documentation/uikit/uivibrancyeffect/1613917-notificationcenter)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### NCWidgetTypes.h (Added)

Added [NCWidgetDisplayMode](https://developer.apple.com/documentation/notificationcenter/ncwidgetdisplaymode)Added [NCWidgetDisplayModeCompact](https://developer.apple.com/documentation/notificationcenter/ncwidgetdisplaymode/compact)Added [NCWidgetDisplayModeExpanded](https://developer.apple.com/documentation/notificationcenter/ncwidgetdisplaymode/expanded)

#### NotificationCenterDefines.h (Added)

Added #def NOTIFICATION_CENTER_EXTERN

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
