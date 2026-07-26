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
doc_path: '/documentation/foundation/notificationcenter/asyncmessage/makenotification(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage/makenotification(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/asyncmessage/makenotification%28_%3A%29.json'
content_hash: 'sha256:335cee135767aa9e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [AsyncMessage](../asyncmessage.md)

# makeNotification(_:)

<sub>Type Method</sub>

Converts a posted asynchronous message into a notification for any observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func makeNotification(_ message: Self) -> Notification
```

## Parameters

- `message` — The posted `AsyncMessage`.

## Return Value

The converted [Notification](../../notification.md).

## Discussion

To implement this method in your own `AsyncMessage` conformance, use the properties defined by the message to populate the [Notification](../../notification.md)’s [userInfo](../../notification/userinfo.md).

## Default Implementations

### NotificationCenter.AsyncMessage Implementations

- [makeNotification(_:)](<makenotification(__)-3760t.md>) — Converts a posted asynchronous message into a notification for any observers.

## See Also

### Converting between messages and notifications

- [makeMessage(_:)](<makemessage(__).md>) — Converts a posted notification into this asynchronous message type for any observers.
