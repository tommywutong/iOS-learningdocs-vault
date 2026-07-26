---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/init(_:)-66i0w'
source_url: 'https://developer.apple.com/documentation/swift/int/init(_:)-66i0w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/init%28_%3A%29-66i0w.json'
content_hash: 'sha256:197d2dedfcdadde0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

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

## See Also

### Converting Floating-Point Values

- [init(_:)](<init(__)-6gt9z.md>)
- [init(_:)](<init(__)-8vbwo.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<init(__)-2oscb.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<init(__)-3huv0.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<init(__)-5q6q5.md>)
