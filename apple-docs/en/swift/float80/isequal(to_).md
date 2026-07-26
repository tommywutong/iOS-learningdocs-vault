---
title: 'isEqual(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/isequal%28to%3A%29.json'
content_hash: 'sha256:819786c593832f0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this instance is equal to the given value.

<sub>macOS</sub>

```swift
func isEqual(to other: Float80) -> Bool
```

## Parameters

- `other` — The value to compare with this value.

## Return Value

`true` if `other` has the same value as this instance; otherwise, `false`. If either this value or `other` is NaN, the result of this method is `false`.

## Discussion

This method serves as the basis for the equal-to operator (`==`) for floating-point values. When comparing two values with this method, `-0` is equal to `+0`. NaN is not equal to any value, including itself. For example:

```swift
let x = 15.0
x.isEqual(to: 15.0)
// true
x.isEqual(to: .nan)
// false
Double.nan.isEqual(to: .nan)
// false
```

The `isEqual(to:)` method implements the equality predicate defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
