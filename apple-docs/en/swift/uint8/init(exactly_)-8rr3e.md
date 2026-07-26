---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint8/init(exactly:)-8rr3e'
source_url: 'https://developer.apple.com/documentation/swift/uint8/init(exactly:)-8rr3e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8/init%28exactly%3A%29-8rr3e.json'
content_hash: 'sha256:f65401c8d3cb5fdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt8](../uint8.md)

# init(exactly:)

<sub>Initializer</sub>

Creates an integer from the given floating-point value, if it can be represented exactly.

<sub>macOS</sub>

```swift
init?(exactly source: Float80)
```

## Parameters

- `source` — A floating-point value to convert to an integer.

## Discussion

If the value passed as `source` is not representable exactly, the result is `nil`. In the following example, the constant `x` is successfully created from a value of `21.0`, while the attempt to initialize the constant `y` from `21.5` fails:

```swift
let x = Int(exactly: 21.0)
// x == Optional(21)
let y = Int(exactly: 21.5)
// y == nil
```
