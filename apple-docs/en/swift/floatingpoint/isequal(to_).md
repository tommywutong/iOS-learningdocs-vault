---
title: 'isEqual(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/isequal%28to%3A%29.json'
content_hash: 'sha256:8f91da3cd35b8c77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this instance is equal to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to other: Self) -> Bool
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
