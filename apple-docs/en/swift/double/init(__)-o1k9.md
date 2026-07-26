---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/init(_:)-o1k9'
source_url: 'https://developer.apple.com/documentation/swift/double/init(_:)-o1k9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/init%28_%3A%29-o1k9.json'
content_hash: 'sha256:865c51c7091c1a13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance initialized to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ other: Double)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

The value of `other` is represented exactly by the new instance. A NaN passed as `other` results in another NaN, with a signaling NaN value converted to quiet NaN.

```swift
let x: Double = 21.25
let y = Double(x)
// y == 21.25

let z = Double(Double.nan)
// z.isNaN == true
```

## See Also

### Converting Floating-Point Values

- [init(_:)](<init(__)-1488d.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-5h7qh.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-aeox.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-9z7ob.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-7ag2w.md>)
- [init(sign:exponent:significand:)](<init(sign_exponent_significand_).md>) — Creates a new value from the given sign, exponent, and significand.
- [init(signOf:magnitudeOf:)](<init(signof_magnitudeof_).md>) — Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(_:)](<init(__)-1oh9r.md>) — Creates a new value, rounded to the closest possible representation.
- [init(truncating:)](<init(truncating_).md>)
