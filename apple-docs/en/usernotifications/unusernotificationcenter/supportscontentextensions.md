---
title: supportsContentExtensions
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unusernotificationcenter/supportscontentextensions
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/supportscontentextensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenter/supportscontentextensions.json'
content_hash: 'sha256:3fbf6f041b76969e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNUserNotificationCenter](../unusernotificationcenter.md)

# supportsContentExtensions

<sub>Instance Property</sub>

A Boolean value that indicates whether the device supports notification content extensions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var supportsContentExtensions: Bool { get }
```

## Discussion

Notification content extensions let you customize the appearance of the alerts displayed for your app’s notifications. The value of this property is [true](../../swift/true.md) for devices that support notification content extensions and [false](../../swift/false.md) for devices that do not support them. For information about how to implement a notification content extension, see [Customizing the Appearance of Notifications](../../usernotificationsui/customizing-the-appearance-of-notifications.md).

## See Also

### Processing received notifications

- [delegate](delegate.md) — The notification center’s delegate.
- [UNUserNotificationCenterDelegate](../unusernotificationcenterdelegate.md) — An interface for processing incoming notifications and responding to notification actions.
