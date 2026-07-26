---
title: 'abs(_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/abs(_:)'
source_url: 'https://developer.apple.com/documentation/swift/abs(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/abs%28_%3A%29.json'
content_hash: 'sha256:46c20557f1cc2e86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# abs(_:)

<sub>Function</sub>

Returns the absolute value of the given number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func abs<T>(_ x: T) -> T where T : Comparable, T : SignedNumeric
```

## Parameters

- `x` — A signed number.

## Return Value

The absolute value of `x`.

## Discussion

The absolute value of `x` must be representable in the same type. In particular, the absolute value of a signed, fixed-width integer type’s minimum cannot be represented.

```swift
let x = Int8.min
// x == -128
let y = abs(x)
// Overflow error
```

## See Also

### Finding the Sign and Magnitude

- [magnitude](int/magnitude-swift.property.md) — The magnitude of this value.
- [Magnitude](int/magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of this type.
- [signum()](<int/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
