---
title: 'storeIdentifier(forConfigurationNamed:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontainer/storeidentifier(forconfigurationnamed:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontainer/storeidentifier(forconfigurationnamed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontainer/storeidentifier%28forconfigurationnamed%3A%29.json'
content_hash: 'sha256:7a48309dbb3f0649'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContainer](../modelcontainer.md)

# storeIdentifier(forConfigurationNamed:)

<sub>Instance Method</sub>

Returns the on-disk store identifier for the given configuration name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func storeIdentifier(forConfigurationNamed name: String) -> String?
```

## Parameters

- `name` — The `name` value from the `ModelConfiguration` used to create the store.

## Return Value

The store identifier string, or `nil` if no store is associated with `name` or if `invalidate()` has been called on this container.

## Discussion

Store identifiers are stable strings derived from the backing file path or the store’s own initialization — they are _not_ the configuration name. Use this function when you have the name you passed to `ModelConfiguration` and need the corresponding identifier to filter a `HistoryDescriptor`, interpret `PersistentIdentifier.storeIdentifier`, or route to a specific store.

If no `ModelConfiguration` was given an explicit name at initialization time, the default name is `"default"`.
