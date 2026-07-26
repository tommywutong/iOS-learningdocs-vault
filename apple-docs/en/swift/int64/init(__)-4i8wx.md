---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int64/init(_:)-4i8wx'
source_url: 'https://developer.apple.com/documentation/swift/int64/init(_:)-4i8wx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int64/init%28_%3A%29-4i8wx.json'
content_hash: 'sha256:62f30b9c0d1a1516'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int64](../int64.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance from the given integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ source: T) where T : BinaryInteger
```

## Parameters

- `source` — A value to convert to this type of integer. The value passed as `source` must be representable in this type.

## Discussion

Use this initializer to convert from another integer type when you know the value is within the bounds of this type. Passing a value that can’t be represented in this type results in a runtime error.

In the following example, the constant `y` is successfully created from `x`, an `Int` instance with a value of `100`. Because the `Int8` type can represent `127` at maximum, the attempt to create `z` with a value of `1000` results in a runtime error.

```swift
let x = 100
let y = Int8(x)
// y == 100
let z = Int8(x * 10)
// Error: Not enough bits to represent the given value
```
