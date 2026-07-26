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
doc_path: '/documentation/foundation/notificationcenter/mainactormessage/makemessage(_:)-7vlo6'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage/makemessage(_:)-7vlo6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/mainactormessage/makemessage%28_%3A%29-7vlo6.json'
content_hash: 'sha256:219d581ca18b49cc'
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
