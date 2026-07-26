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
doc_path: '/documentation/swift/float/init(_:)-1oh9p'
source_url: 'https://developer.apple.com/documentation/swift/float/init(_:)-1oh9p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28_%3A%29-1oh9p.json'
content_hash: 'sha256:6c45814016c58a68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# init(_:)

<sub>Initializer</sub>

Creates a new value, rounded to the closest possible representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Source>(_ value: Source) where Source : BinaryInteger
```

## Parameters

- `value` — The integer to convert to a floating-point value.

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## See Also

### Converting Floating-Point Values

- [init(_:)](<init(__)-1488f.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-1kp2p.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-975tv.md>) — Creates a new instance initialized to the given value.
- [init(_:)](<init(__)-11orc.md>) — Creates a new instance that approximates the given value.
- [init(_:)](<init(__)-5soww.md>)
- [init(_:)](<init(__)-ussz.md>) — Creates a new instance that approximates the given value.
- [init(signOf:magnitudeOf:)](<init(signof_magnitudeof_).md>) — Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(sign:exponent:significand:)](<init(sign_exponent_significand_).md>) — Creates a new value from the given sign, exponent, and significand.
- [init(truncating:)](<init(truncating_).md>)
