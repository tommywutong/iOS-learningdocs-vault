---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/init(_:)-aeox'
source_url: 'https://developer.apple.com/documentation/swift/double/init(_:)-aeox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/init%28_%3A%29-aeox.json'
content_hash: 'sha256:3dd129c4ab982d10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance that approximates the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ other: Float16)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

The value of `other` is rounded to a representable value, if necessary. A NaN passed as `other` results in another NaN, with a signaling NaN value converted to quiet NaN.

```swift
let x: Float16 = 21.25
let y = Double(x)
// y == 21.25

let z = Double(Float16.nan)
// z.isNaN == true
```

## See Also

### Converting Floating-Point Values

- [init(_:)](<init(__)-1488d.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-o1k9.md>) — Creates a new instance initialized to the given value.
- [init(_:)](<init(__)-5h7qh.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-9z7ob.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-7ag2w.md>)
- [init(sign:exponent:significand:)](<init(sign_exponent_significand_).md>) — Creates a new value from the given sign, exponent, and significand.
- [init(signOf:magnitudeOf:)](<init(signof_magnitudeof_).md>) — Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(_:)](<init(__)-1oh9r.md>) — Creates a new value, rounded to the closest possible representation.
- [init(truncating:)](<init(truncating_).md>)
