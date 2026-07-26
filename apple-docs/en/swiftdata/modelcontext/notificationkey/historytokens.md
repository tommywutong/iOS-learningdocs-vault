---
title: ModelContext.NotificationKey.historyTokens
framework: SwiftData
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext/notificationkey/historytokens
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/notificationkey/historytokens'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/notificationkey/historytokens.json'
content_hash: 'sha256:4c7b68ee23ee1ec1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftData](../../../swiftdata.md) · [ModelContext](../../modelcontext.md) · [NotificationKey](../notificationkey.md)

# ModelContext.NotificationKey.historyTokens

<sub>Case</sub>

A history token representing the persistent store state after the save.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case historyTokens
```

## Discussion

This key is available in `ModelContext.didSave` notifications (it is not present in `willSave` notifications). The value is an instance conforming to `HistoryToken`.

Use this token with `HistoryDescriptor` to fetch only changes that occurred after this save operation:

```swift
NotificationCenter.default.addObserver(
    forName: ModelContext.didSave,
    object: nil,
    queue: nil
) { notification in
    guard let token = notification.userInfo?[ModelContext.NotificationKey.historyToken] as? DefaultHistoryToken else {
        return
    }

    // Use token to fetch changes since this save
    let descriptor = HistoryDescriptor<DefaultHistoryTransaction>(
        predicate: #Predicate { $0.token > token }
    )
}
```

## See Also

### Accessing notification keys

- [ModelContext.NotificationKey.deletedIdentifiers](deletedidentifiers.md) — A set of values identifying the context’s deleted models.
- [ModelContext.NotificationKey.insertedIdentifiers](insertedidentifiers.md) — A set of values identifying the context’s inserted models.
- [ModelContext.NotificationKey.invalidatedAllIdentifiers](invalidatedallidentifiers.md) — A set of values identifying the context’s invalidated models.
- [ModelContext.NotificationKey.updatedIdentifiers](updatedidentifiers.md) — A set of values identifying the context’s updated models.
- [ModelContext.NotificationKey.queryGeneration](querygeneration.md) — A token that indicates which generation of the model store SwiftData is using.
