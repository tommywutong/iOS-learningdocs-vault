---
title: 'init(signOf:magnitudeOf:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(signof:magnitudeof:)-1oylh'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(signof:magnitudeof:)-1oylh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28signof%3Amagnitudeof%3A%29-1oylh.json'
content_hash: 'sha256:f46bbeff0ece0e48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(signOf:magnitudeOf:)

<sub>Initializer</sub>

Creates a new floating-point value using the sign of one value and the magnitude of another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(signOf: Self, magnitudeOf: Self)
```

## Parameters

- `signOf` — A value from which to use the sign. The result of the initializer has the same sign as `signOf`.

- `magnitudeOf` — A value from which to use the magnitude. The result of the initializer has the same magnitude as `magnitudeOf`.

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
