---
title: 'configurationName(forStoreIdentifier:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontainer/configurationname(forstoreidentifier:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontainer/configurationname(forstoreidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontainer/configurationname%28forstoreidentifier%3A%29.json'
content_hash: 'sha256:ef24acd48c57e5ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContainer](../modelcontainer.md)

# configurationName(forStoreIdentifier:)

<sub>Instance Method</sub>

Returns the configuration name associated with the given on-disk store identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func configurationName(forStoreIdentifier identifier: String) -> String?
```

## Parameters

- `identifier` — A store identifier string, for example from `PersistentIdentifier.storeIdentifier` or a history transaction’s store identifier.

## Return Value

The `name` of the `ModelConfiguration` that backs the given store, or `nil` if no store with that identifier exists in this container or if `invalidate()` has been called.

## Discussion

Use this when you already have a store identifier — such as `PersistentIdentifier.storeIdentifier` from a fetched object or a store identifier from a history transaction — and need to map it back to the human-readable configuration name that produced that store.
