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
doc_path: '/documentation/foundation/notificationcenter/mainactormessage/makenotification(_:)-4xbaj'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage/makenotification(_:)-4xbaj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/mainactormessage/makenotification%28_%3A%29-4xbaj.json'
content_hash: 'sha256:a026002cef0bf797'
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
