---
title: 'addProduct(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/addproduct(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/addproduct(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/addproduct%28_%3A_%3A%29.json'
content_hash: 'sha256:82b9b843e9a14afe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# addProduct(_:_:)

<sub>Instance Method</sub>

Adds the product of the two given values to this value in place, computed without intermediate rounding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addProduct(_ lhs: Self, _ rhs: Self)
```

## Parameters

- `lhs` — One of the values to multiply before adding to this value.

- `rhs` — The other value to multiply.
