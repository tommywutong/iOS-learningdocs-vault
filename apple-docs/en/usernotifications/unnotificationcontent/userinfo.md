---
title: userInfo
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcontent/userinfo
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/userinfo.json'
content_hash: 'sha256:2428d648b72c36d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# userInfo

<sub>Instance Property</sub>

The custom data to associate with the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any] { get }
```

## Discussion

For remote notifications, this property contains the entire notification payload. For local notifications, you configure the property directly before scheduling the notification.

The keys in this dictionary must be property-list types—that’s, they must be types that can be serialized into the property-list format. For information about property-list types, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## See Also

### Accessing supplementary content

- [attachments](attachments.md) — The visual and audio attachments to display alongside the notification’s main content.
