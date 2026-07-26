---
title: 'init(wrappedValue:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/published/init(wrappedvalue:)'
source_url: 'https://developer.apple.com/documentation/combine/published/init(wrappedvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/published/init%28wrappedvalue%3A%29.json'
content_hash: 'sha256:876f1cdc4c0afe49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Published](../published.md)

# init(wrappedValue:)

<sub>Initializer</sub>

Creates the published instance with an initial wrapped value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(wrappedValue: Value)
```

## Parameters

- `wrappedValue` — The publisher’s initial value.

## Discussion

Don’t use this initializer directly. Instead, create a property with the `@Published` attribute, as shown here:

```swift
@Published var lastUpdated: Date = Date()
```

## See Also

### Creating a published instance

- [init(initialValue:)](<init(initialvalue_).md>) — Creates the published instance with an initial value.
