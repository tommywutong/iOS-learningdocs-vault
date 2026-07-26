---
title: 'init(signOf:magnitudeOf:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/init(signof:magnitudeof:)'
source_url: 'https://developer.apple.com/documentation/swift/double/init(signof:magnitudeof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/init%28signof%3Amagnitudeof%3A%29.json'
content_hash: 'sha256:e6ae14b12130da12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# init(signOf:magnitudeOf:)

<sub>Initializer</sub>

Creates a new floating-point value using the sign of one value and the magnitude of another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(signOf sign: Double, magnitudeOf mag: Double)
```

## Discussion

The following example uses this initializer to create a new `Double` instance with the sign of `a` and the magnitude of `b`:

```swift
let a = -21.5
let b = 305.15
let c = Double(signOf: a, magnitudeOf: b)
print(c)
// Prints "-305.15"
```

This initializer implements the IEEE 754 `copysign` operation.

## See Also

### Converting Floating-Point Values

- [init(_:)](<init(__)-1488d.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-o1k9.md>) — Creates a new instance initialized to the given value.
- [init(_:)](<init(__)-5h7qh.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-aeox.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-9z7ob.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-7ag2w.md>)
- [init(sign:exponent:significand:)](<init(sign_exponent_significand_).md>) — Creates a new value from the given sign, exponent, and significand.
- [init(_:)](<init(__)-1oh9r.md>) — Creates a new value, rounded to the closest possible representation.
- [init(truncating:)](<init(truncating_).md>)
