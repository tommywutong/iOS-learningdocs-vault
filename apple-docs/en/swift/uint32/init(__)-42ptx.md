---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint32/init(_:)-42ptx'
source_url: 'https://developer.apple.com/documentation/swift/uint32/init(_:)-42ptx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint32/init%28_%3A%29-42ptx.json'
content_hash: 'sha256:3d137f60adeabae6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt32](../uint32.md)

# init(_:)

<sub>Initializer</sub>

Creates an integer from the given floating-point value, rounding toward zero.

<sub>macOS</sub>

```swift
init(_ source: Float80)
```

## Parameters

- `source` — A floating-point value to convert to an integer. `source` must be representable in this type after rounding toward zero.

## Discussion

Any fractional part of the value passed as `source` is removed, rounding the value toward zero.

```swift
let x = Int(21.5)
// x == 21
let y = Int(-21.5)
// y == -21
```

If `source` is outside the bounds of this type after rounding toward zero, a runtime error may occur.

```swift
let z = UInt(-21.5)
// Error: ...the result would be less than UInt.min
```
