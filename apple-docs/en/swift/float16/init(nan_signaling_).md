---
title: 'init(nan:signaling:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(nan:signaling:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(nan:signaling:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28nan%3Asignaling%3A%29.json'
content_hash: 'sha256:7a2884ec89536494'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(nan:signaling:)

<sub>Initializer</sub>

Creates a NaN (“not a number”) value with the specified payload.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(nan payload: Float16.RawSignificand, signaling: Bool)
```

## Parameters

- `payload` — The payload to use for the new NaN value.

- `signaling` — Pass `true` to create a signaling NaN or `false` to create a quiet NaN.

## Discussion

NaN values compare not equal to every value, including themselves. Most operations with a NaN operand produce a NaN result. Don’t use the equal-to operator (`==`) to test whether a value is NaN. Instead, use the value’s `isNaN` property.

```swift
let x = Float16(nan: 0, signaling: false)
print(x == .nan)
// Prints "false"
print(x.isNaN)
// Prints "true"
```
