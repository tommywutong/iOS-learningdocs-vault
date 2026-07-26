---
title: 'addingProduct(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/addingproduct(_:_:)-81yl5'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/addingproduct(_:_:)-81yl5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/addingproduct%28_%3A_%3A%29-81yl5.json'
content_hash: 'sha256:31ee2bae83d8845d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# addingProduct(_:_:)

<sub>Instance Method</sub>

Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addingProduct(_ lhs: Self, _ rhs: Self) -> Self
```

## Parameters

- `lhs` — One of the values to multiply before adding to this value.

- `rhs` — The other value to multiply.

## Return Value

The product of `lhs` and `rhs`, added to this value.

## Discussion

This method is equivalent to the C `fma` function and implements the `fusedMultiplyAdd` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
