---
title: ModelContext.NotificationKey
framework: SwiftData
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/notificationkey
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/notificationkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/notificationkey.json'
content_hash: 'sha256:02c03ef67e9ff361'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# ModelContext.NotificationKey

<sub>Enumeration</sub>

Describes the data in the user info dictionary of a notification sent by a model context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NotificationKey
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md)

## Topics

### Accessing notification keys

- [ModelContext.NotificationKey.deletedIdentifiers](notificationkey/deletedidentifiers.md) — A set of values identifying the context’s deleted models.
- [ModelContext.NotificationKey.insertedIdentifiers](notificationkey/insertedidentifiers.md) — A set of values identifying the context’s inserted models.
- [ModelContext.NotificationKey.invalidatedAllIdentifiers](notificationkey/invalidatedallidentifiers.md) — A set of values identifying the context’s invalidated models.
- [ModelContext.NotificationKey.updatedIdentifiers](notificationkey/updatedidentifiers.md) — A set of values identifying the context’s updated models.
- [ModelContext.NotificationKey.queryGeneration](notificationkey/querygeneration.md) — A token that indicates which generation of the model store SwiftData is using.
- [ModelContext.NotificationKey.historyTokens](notificationkey/historytokens.md) — A history token representing the persistent store state after the save.

## See Also

### Registering for notifications

- [willSave](willsave.md) — A notification that posts when the context is about to process pending inserts, changes, and deletes.
- [didSave](didsave.md) — A notification that posts when the context finishes processing pending inserts, changes, and deletes.
