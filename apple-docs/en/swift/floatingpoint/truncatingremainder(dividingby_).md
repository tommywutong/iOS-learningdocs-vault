---
title: 'truncatingRemainder(dividingBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/truncatingremainder(dividingby:)'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/truncatingremainder(dividingby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/truncatingremainder%28dividingby%3A%29.json'
content_hash: 'sha256:0c96e183727d92ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# truncatingRemainder(dividingBy:)

<sub>Instance Method</sub>

Returns the remainder of this value divided by the given value using truncating division.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func truncatingRemainder(dividingBy other: Self) -> Self
```

## Parameters

- `other` — The value to use when dividing this value.

## Return Value

The remainder of this value divided by `other` using truncating division.

## Discussion

Performing truncating division with floating-point values results in a truncated integer quotient and a remainder. For values `x` and `y` and their truncated integer quotient `q`, the remainder `r` satisfies `x == y * q + r`.

The following example calculates the truncating remainder of dividing 8.625 by 0.75:

```swift
let x = 8.625
print(x / 0.75)
// Prints "11.5"

let q = (x / 0.75).rounded(.towardZero)
// q == 11.0
let r = x.truncatingRemainder(dividingBy: 0.75)
// r == 0.375

let x1 = 0.75 * q + r
// x1 == 8.625
```

If this value and `other` are both finite numbers, the truncating remainder has the same sign as this value and is strictly smaller in magnitude than `other`. The `truncatingRemainder(dividingBy:)` method is always exact.

## Default Implementations

### FloatingPoint Implementations

- [truncatingRemainder(dividingBy:)](<truncatingremainder(dividingby_)-6ay9c.md>) — Returns the remainder of this value divided by the given value using truncating division.
