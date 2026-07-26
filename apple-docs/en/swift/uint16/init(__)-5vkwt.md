---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint16/init(_:)-5vkwt'
source_url: 'https://developer.apple.com/documentation/swift/uint16/init(_:)-5vkwt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint16/init%28_%3A%29-5vkwt.json'
content_hash: 'sha256:45a8cae715dd1231'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt16](../uint16.md)

# init(_:)

<sub>Initializer</sub>

Creates an integer from the given floating-point value, rounding toward zero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ source: Float16)
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
