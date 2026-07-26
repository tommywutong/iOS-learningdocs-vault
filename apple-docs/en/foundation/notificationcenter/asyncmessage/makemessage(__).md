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
doc_path: '/documentation/foundation/notificationcenter/asyncmessage/makemessage(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage/makemessage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/asyncmessage/makemessage%28_%3A%29.json'
content_hash: 'sha256:c0101ea6a5c53090'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [AsyncMessage](../asyncmessage.md)

# makeMessage(_:)

<sub>Type Method</sub>

Converts a posted notification into this asynchronous message type for any observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func makeMessage(_ notification: Notification) -> Self?
```

## Parameters

- `notification` — The posted [Notification](../../notification.md).

## Return Value

The converted `AsyncMessage`, or `nil` if conversion is not possible.

## Discussion

To implement this method in your own `AsyncMessage` conformance, retrieve values from the [Notification](../../notification.md)’s [userInfo](../../notification/userinfo.md) and set them as properties on the message.

## Default Implementations

### NotificationCenter.AsyncMessage Implementations

- [makeMessage(_:)](<makemessage(__)-2l2y5.md>) — Converts a posted notification into this asynchronous message type for any observers.

## See Also

### Converting between messages and notifications

- [makeNotification(_:)](<makenotification(__).md>) — Converts a posted asynchronous message into a notification for any observers.
