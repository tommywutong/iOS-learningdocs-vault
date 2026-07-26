---
title: 'init(_:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/init%28_%3A%29.json'
content_hash: 'sha256:585fad07cc2ba1e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# init(_:)

<sub>Initializer</sub>

Creates a context that belongs to the specified model container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ container: ModelContainer)
```

## Parameters

- `container` — The model container to associate with the initialized context.

## Discussion

Use the context’s [container](container.md) property to access the model container after initializtion.

## See Also

### Creating a model context

- [ModelContainer](../modelcontainer.md) — An object that manages an app’s schema and model storage configuration.
