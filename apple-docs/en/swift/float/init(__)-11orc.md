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
doc_path: '/documentation/swift/float/init(_:)-11orc'
source_url: 'https://developer.apple.com/documentation/swift/float/init(_:)-11orc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28_%3A%29-11orc.json'
content_hash: 'sha256:0486bebb1e9f21d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance that approximates the given value.

<sub>macOS</sub>

```swift
init(_ other: Float80)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

The value of `other` is rounded to a representable value, if necessary. A NaN passed as `other` results in another NaN, with a signaling NaN value converted to quiet NaN.

```swift
let x: Float80 = 21.25
let y = Float(x)
// y == 21.25

let z = Float(Float80.nan)
// z.isNaN == true
```

## See Also

### Converting Floating-Point Values

- [init(_:)](<init(__)-1488f.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-1oh9p.md>) — Creates a new value, rounded to the closest possible representation.
- [init(_:)](<init(__)-1kp2p.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-975tv.md>) — Creates a new instance initialized to the given value.
- [init(_:)](<init(__)-5soww.md>)
- [init(_:)](<init(__)-ussz.md>) — Creates a new instance that approximates the given value.
- [init(signOf:magnitudeOf:)](<init(signof_magnitudeof_).md>) — Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(sign:exponent:significand:)](<init(sign_exponent_significand_).md>) — Creates a new value from the given sign, exponent, and significand.
- [init(truncating:)](<init(truncating_).md>)
