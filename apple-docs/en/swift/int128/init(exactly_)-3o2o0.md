---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int128/init(exactly:)-3o2o0'
source_url: 'https://developer.apple.com/documentation/swift/int128/init(exactly:)-3o2o0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/init%28exactly%3A%29-3o2o0.json'
content_hash: 'sha256:db2961259e10c1b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance from the given integer, if it can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<T>(exactly source: T) where T : BinaryInteger
```

## Parameters

- `source` — A value to convert to this type.

## Discussion

If the value passed as `source` is not representable exactly, the result is `nil`. In the following example, the constant `x` is successfully created from a value of `100`, while the attempt to initialize the constant `y` from `1_000` fails because the `Int8` type can represent `127` at maximum:

```swift
let x = Int8(exactly: 100)
// x == Optional(100)
let y = Int8(exactly: 1_000)
// y == nil
```
