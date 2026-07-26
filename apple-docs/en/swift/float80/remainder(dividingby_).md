---
title: 'remainder(dividingBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/remainder(dividingby:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/remainder(dividingby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/remainder%28dividingby%3A%29.json'
content_hash: 'sha256:af9e3313ed504a1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# remainder(dividingBy:)

<sub>Instance Method</sub>

Returns the remainder of this value divided by the given value.

<sub>macOS</sub>

```swift
func remainder(dividingBy other: Self) -> Self
```

## Parameters

- `other` — The value to use when dividing this value.

## Return Value

The remainder of this value divided by `other`.

## Discussion

For two finite values `x` and `y`, the remainder `r` of dividing `x` by `y` satisfies `x == y * q + r`, where `q` is the integer nearest to `x / y`. If `x / y` is exactly halfway between two integers, `q` is chosen to be even. Note that `q` is _not_ `x / y` computed in floating-point arithmetic, and that `q` may not be representable in any available integer type.

The following example calculates the remainder of dividing 8.625 by 0.75:

```swift
let x = 8.625
print(x / 0.75)
// Prints "11.5"

let q = (x / 0.75).rounded(.toNearestOrEven)
// q == 12.0
let r = x.remainder(dividingBy: 0.75)
// r == -0.375

let x1 = 0.75 * q + r
// x1 == 8.625
```

If this value and `other` are finite numbers, the remainder is in the closed range `-abs(other / 2)...abs(other / 2)`. The `remainder(dividingBy:)` method is always exact. This method implements the remainder operation defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
