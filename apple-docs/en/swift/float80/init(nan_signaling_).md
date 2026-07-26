---
title: 'init(nan:signaling:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/init(nan:signaling:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(nan:signaling:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28nan%3Asignaling%3A%29.json'
content_hash: 'sha256:551ab0b9e962cc4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(nan:signaling:)

<sub>Initializer</sub>

Creates a NaN (“not a number”) value with the specified payload.

<sub>macOS</sub>

```swift
init(nan payload: Float80.RawSignificand, signaling: Bool)
```

## Parameters

- `payload` — The payload to use for the new NaN value.

- `signaling` — Pass `true` to create a signaling NaN or `false` to create a quiet NaN.

## Discussion

NaN values compare not equal to every value, including themselves. Most operations with a NaN operand produce a NaN result. Don’t use the equal-to operator (`==`) to test whether a value is NaN. Instead, use the value’s `isNaN` property.

```swift
let x = Float80(nan: 0, signaling: false)
print(x == .nan)
// Prints "false"
print(x.isNaN)
// Prints "true"
```
