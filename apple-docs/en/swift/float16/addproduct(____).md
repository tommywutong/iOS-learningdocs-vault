---
title: 'addProduct(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/addproduct(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/addproduct(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/addproduct%28_%3A_%3A%29.json'
content_hash: 'sha256:62b9b688517e0635'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# addProduct(_:_:)

<sub>Instance Method</sub>

Adds the product of the two given values to this value in place, computed without intermediate rounding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addProduct(_ lhs: Float16, _ rhs: Float16)
```

## Parameters

- `lhs` — One of the values to multiply before adding to this value.

- `rhs` — The other value to multiply.
