---
title: 'init(_:including:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/init(_:including:)-8ls7v'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/init(_:including:)-8ls7v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/init%28_%3Aincluding%3A%29-8ls7v.json'
content_hash: 'sha256:2dc4f3110db17a89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# init(_:including:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ container: AttributeContainer, including scope: KeyPath<AttributeScopes, S.Type>) throws where S : AttributeScope
```

## See Also

### Creating a Dictionary from an Attribute Container

- [init(_:including:)](<init(__including_)-7afz2.md>)
- [init(_:)](<init(__).md>)
