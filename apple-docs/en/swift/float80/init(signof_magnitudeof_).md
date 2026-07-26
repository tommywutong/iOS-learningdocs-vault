---
title: 'init(signOf:magnitudeOf:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/init(signof:magnitudeof:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(signof:magnitudeof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28signof%3Amagnitudeof%3A%29.json'
content_hash: 'sha256:11d529631c53b55c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(signOf:magnitudeOf:)

<sub>Initializer</sub>

Creates a new floating-point value using the sign of one value and the magnitude of another.

<sub>macOS</sub>

```swift
init(signOf sign: Float80, magnitudeOf mag: Float80)
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
