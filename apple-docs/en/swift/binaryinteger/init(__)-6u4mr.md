---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryinteger/init(_:)-6u4mr'
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/init(_:)-6u4mr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/init%28_%3A%29-6u4mr.json'
content_hash: 'sha256:46a568f59c4747a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

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
