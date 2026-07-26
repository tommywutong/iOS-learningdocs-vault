---
title: 'init(sign:exponent:significand:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(sign:exponent:significand:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(sign:exponent:significand:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28sign%3Aexponent%3Asignificand%3A%29.json'
content_hash: 'sha256:2fc449af99aaaf4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(sign:exponent:significand:)

<sub>Initializer</sub>

Creates a new value from the given sign, exponent, and significand.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(sign: FloatingPointSign, exponent: Int, significand: Float16)
```

## Parameters

- `sign` — The sign to use for the new value.

- `exponent` — The new value’s exponent.

- `significand` — The new value’s significand.

## Discussion

The following example uses this initializer to create a new `Double` instance. `Double` is a binary floating-point type that has a radix of `2`.

```swift
let x = Double(sign: .plus, exponent: -2, significand: 1.5)
// x == 0.375
```

This initializer is equivalent to the following calculation, where `**` is exponentiation, computed as if by a single, correctly rounded, floating-point operation:

```swift
let sign: FloatingPointSign = .plus
let exponent = -2
let significand = 1.5
let y = (sign == .minus ? -1 : 1) * significand * Double.radix ** exponent
// y == 0.375
```

As with any basic operation, if this value is outside the representable range of the type, overflow or underflow occurs, and zero, a subnormal value, or infinity may result. In addition, there are two other edge cases:

- If the value you pass to `significand` is zero or infinite, the result is zero or infinite, regardless of the value of `exponent`.
- If the value you pass to `significand` is NaN, the result is NaN.

For any floating-point value `x` of type `F`, the result of the following is equal to `x`, with the distinction that the result is canonicalized if `x` is in a noncanonical encoding:

```swift
let x0 = F(sign: x.sign, exponent: x.exponent, significand: x.significand)
```

This initializer implements the `scaleB` operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
