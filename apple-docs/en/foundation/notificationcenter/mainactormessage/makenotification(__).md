---
title: 'makeNotification(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/mainactormessage/makenotification(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage/makenotification(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/mainactormessage/makenotification%28_%3A%29.json'
content_hash: 'sha256:e273d7523c4616a1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MainActorMessage](../mainactormessage.md)

# makeNotification(_:)

<sub>Type Method</sub>

Converts a posted main actor message into a notification for any observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor static func makeNotification(_ message: Self) -> Notification
```

## Parameters

- `message` — The posted `MainActorMessage`.

## Return Value

The converted [Notification](../../notification.md).

## Discussion

To implement this method in your own `MainActorMessage` conformance, use the properties defined by the message to populate the [Notification](../../notification.md)’s [userInfo](../../notification/userinfo.md).

## Default Implementations

### NotificationCenter.MainActorMessage Implementations

- [makeNotification(_:)](<makenotification(__)-4xbaj.md>) — Converts a posted main actor message into a notification for any observers.

## See Also

### Converting between messages and notifications

- [makeMessage(_:)](<makemessage(__).md>) — Converts a posted notification into this main actor message type for any observers.
