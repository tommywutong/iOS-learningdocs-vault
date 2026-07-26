---
title: 'formTruncatingRemainder(dividingBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/formtruncatingremainder(dividingby:)'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/formtruncatingremainder(dividingby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/formtruncatingremainder%28dividingby%3A%29.json'
content_hash: 'sha256:24d03318aedef14e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# formTruncatingRemainder(dividingBy:)

<sub>Instance Method</sub>

Replaces this value with the remainder of itself divided by the given value using truncating division.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formTruncatingRemainder(dividingBy other: Self)
```

## Parameters

- `other` — The value to use when dividing this value.

## Discussion

Performing truncating division with floating-point values results in a truncated integer quotient and a remainder. For values `x` and `y` and their truncated integer quotient `q`, the remainder `r` satisfies `x == y * q + r`.

The following example calculates the truncating remainder of dividing 8.625 by 0.75:

```swift
var x = 8.625
print(x / 0.75)
// Prints "11.5"

let q = (x / 0.75).rounded(.towardZero)
// q == 11.0
x.formTruncatingRemainder(dividingBy: 0.75)
// x == 0.375

let x1 = 0.75 * q + x
// x1 == 8.625
```

If this value and `other` are both finite numbers, the truncating remainder has the same sign as this value and is strictly smaller in magnitude than `other`. The `formTruncatingRemainder(dividingBy:)` method is always exact.
