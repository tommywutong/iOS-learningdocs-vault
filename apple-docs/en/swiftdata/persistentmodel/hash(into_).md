---
title: 'hash(into:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/persistentmodel/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/persistentmodel/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/persistentmodel/hash%28into%3A%29.json'
content_hash: 'sha256:5458cc4a6229bf13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [PersistentModel](../persistentmodel.md)

# hash(into:)

<sub>Instance Method</sub>

Hashes the essential components of this value by feeding them into the given hasher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher` — The hasher to use when combining the components of this instance.

## Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> [!important] Important
> In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.
