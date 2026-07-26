---
title: willSave
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/willsave
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/willsave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/willsave.json'
content_hash: 'sha256:c0aae57550788cc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# willSave

<sub>Type Property</sub>

A notification that posts when the context is about to process pending inserts, changes, and deletes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let willSave: Notification.Name
```

## Discussion

> [!note] Note
> Notifications with this name don’t contain a `userInfo` dictionary.

## See Also

### Registering for notifications

- [didSave](didsave.md) — A notification that posts when the context finishes processing pending inserts, changes, and deletes.
- [NotificationKey](notificationkey.md) — Describes the data in the user info dictionary of a notification sent by a model context.
