---
title: 'formRemainder(dividingBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/formremainder(dividingby:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/formremainder(dividingby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/formremainder%28dividingby%3A%29.json'
content_hash: 'sha256:0cb6f264ca640546'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# formRemainder(dividingBy:)

<sub>Instance Method</sub>

Replaces this value with the remainder of itself divided by the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formRemainder(dividingBy other: Float16)
```

## Parameters

- `other` — The value to use when dividing this value.

## Discussion

For two finite values `x` and `y`, the remainder `r` of dividing `x` by `y` satisfies `x == y * q + r`, where `q` is the integer nearest to `x / y`. If `x / y` is exactly halfway between two integers, `q` is chosen to be even. Note that `q` is _not_ `x / y` computed in floating-point arithmetic, and that `q` may not be representable in any available integer type.

The following example calculates the remainder of dividing 8.625 by 0.75:

```swift
var x = 8.625
print(x / 0.75)
// Prints "11.5"

let q = (x / 0.75).rounded(.toNearestOrEven)
// q == 12.0
x.formRemainder(dividingBy: 0.75)
// x == -0.375

let x1 = 0.75 * q + x
// x1 == 8.625
```

If this value and `other` are finite numbers, the remainder is in the closed range `-abs(other / 2)...abs(other / 2)`. The `formRemainder(dividingBy:)` method is always exact.
