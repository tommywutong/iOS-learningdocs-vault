---
title: 'makeMessage(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/mainactormessage/makemessage(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage/makemessage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/mainactormessage/makemessage%28_%3A%29.json'
content_hash: 'sha256:761592cdf4a7f4a8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MainActorMessage](../mainactormessage.md)

# makeMessage(_:)

<sub>Type Method</sub>

Converts a posted notification into this main actor message type for any observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor static func makeMessage(_ notification: Notification) -> Self?
```

## Parameters

- `notification` — The posted [Notification](../../notification.md).

## Return Value

The converted `MainActorMessage` or `nil` if conversion is not possible.

## Discussion

To implement this method in your own `MainActorMessage` conformance, retrieve values from the [Notification](../../notification.md)’s [userInfo](../../notification/userinfo.md) and set them as properties on the message.

## Default Implementations

### NotificationCenter.MainActorMessage Implementations

- [makeMessage(_:)](<makemessage(__)-7vlo6.md>) — Converts a posted notification into this main actor message type for any observers.

## See Also

### Converting between messages and notifications

- [makeNotification(_:)](<makenotification(__).md>) — Converts a posted main actor message into a notification for any observers.
