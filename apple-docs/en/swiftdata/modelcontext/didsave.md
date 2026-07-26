---
title: didSave
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/didsave
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/didsave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/didsave.json'
content_hash: 'sha256:0729794a12716b8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# didSave

<sub>Type Property</sub>

A notification that posts when the context finishes processing pending inserts, changes, and deletes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let didSave: Notification.Name
```

## Discussion

The notification’s `userInfo` dictionary contains the persistent identifiers of any inserted, updated, or deleted models. Use the appropriate key to access those identifiers. For more information, see [NotificationKey](notificationkey.md).

## See Also

### Registering for notifications

- [willSave](willsave.md) — A notification that posts when the context is about to process pending inserts, changes, and deletes.
- [NotificationKey](notificationkey.md) — Describes the data in the user info dictionary of a notification sent by a model context.
