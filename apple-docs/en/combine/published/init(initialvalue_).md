---
title: 'init(initialValue:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/published/init(initialvalue:)'
source_url: 'https://developer.apple.com/documentation/combine/published/init(initialvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/published/init%28initialvalue%3A%29.json'
content_hash: 'sha256:26f0145dfb224e2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Published](../published.md)

# init(initialValue:)

<sub>Initializer</sub>

Creates the published instance with an initial value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(initialValue: Value)
```

## Parameters

- `initialValue` — The publisher’s initial value.

## Discussion

Don’t use this initializer directly. Instead, create a property with the `@Published` attribute, as shown here:

```swift
@Published var lastUpdated: Date = Date()
```

## See Also

### Creating a published instance

- [init(wrappedValue:)](<init(wrappedvalue_).md>) — Creates the published instance with an initial wrapped value.
