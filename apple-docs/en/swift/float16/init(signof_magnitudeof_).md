---
title: 'init(signOf:magnitudeOf:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(signof:magnitudeof:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(signof:magnitudeof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28signof%3Amagnitudeof%3A%29.json'
content_hash: 'sha256:7862591fe7d703e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(signOf:magnitudeOf:)

<sub>Initializer</sub>

Creates a new floating-point value using the sign of one value and the magnitude of another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(signOf sign: Float16, magnitudeOf mag: Float16)
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
