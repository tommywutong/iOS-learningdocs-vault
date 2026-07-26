---
title: 'isLess(than:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/isless(than:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/isless(than:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/isless%28than%3A%29.json'
content_hash: 'sha256:af8bf1045e90c85e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isLess(than:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this instance is less than the given value.

<sub>macOS</sub>

```swift
func isLess(than other: Float80) -> Bool
```

## Parameters

- `other` — The value to compare with this value.

## Return Value

`true` if this value is less than `other`; otherwise, `false`. If either this value or `other` is NaN, the result of this method is `false`.

## Discussion

This method serves as the basis for the less-than operator (`<`) for floating-point values. Some special cases apply:

- Because NaN compares not less than nor greater than any value, this method returns `false` when called on NaN or when NaN is passed as `other`.
- `-infinity` compares less than all values except for itself and NaN.
- Every value except for NaN and `+infinity` compares less than `+infinity`.

The following example shows the behavior of the `isLess(than:)` method with different kinds of values:

```swift
let x = 15.0
x.isLess(than: 20.0)
// true
x.isLess(than: .nan)
// false
Double.nan.isLess(than: x)
// false
```

The `isLess(than:)` method implements the less-than predicate defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
