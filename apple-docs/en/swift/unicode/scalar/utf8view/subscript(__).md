---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/scalar/utf8view/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/utf8view/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/utf8view/subscript%28_%3A%29.json'
content_hash: 'sha256:b50b77682a9b68b1'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [UTF8View](../utf8view.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the code unit at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: Int) -> UTF8.CodeUnit { get }
```

## Parameters

- `position` — The position of the element to access. `position` must be a valid index of the collection that is not equal to the `endIndex` property.
