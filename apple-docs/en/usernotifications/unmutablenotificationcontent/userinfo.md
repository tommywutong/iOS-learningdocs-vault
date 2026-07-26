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
doc_path: /documentation/usernotifications/unmutablenotificationcontent/userinfo
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/userinfo.json'
content_hash: 'sha256:ac806a42a6017c13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# userInfo

<sub>Instance Property</sub>

The custom data to associate with the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any] { get set }
```

## Discussion

Use this property to associate custom information with the notification. The contents of the dictionary aren’t seen by the user, but are accessible to your app or to any notification-related app extensions.

The keys in this dictionary must be types that can be serialized into the property-list format. For information about property-list types, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## See Also

### Providing supplementary content

- [attachments](attachments.md) — The visual and audio attachments to display alongside the notification’s main content.
