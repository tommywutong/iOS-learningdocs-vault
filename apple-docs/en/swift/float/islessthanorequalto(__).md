---
title: 'isLessThanOrEqualTo(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/islessthanorequalto(_:)'
source_url: 'https://developer.apple.com/documentation/swift/float/islessthanorequalto(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/islessthanorequalto%28_%3A%29.json'
content_hash: 'sha256:6ab28c4bd06868cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# isLessThanOrEqualTo(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this instance is less than or equal to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isLessThanOrEqualTo(_ other: Float) -> Bool
```

## Parameters

- `other` — The value to compare with this value.

## Return Value

`true` if `other` is greater than this value; otherwise, `false`. If either this value or `other` is NaN, the result of this method is `false`.

## Discussion

This method serves as the basis for the less-than-or-equal-to operator (`<=`) for floating-point values. Some special cases apply:

- Because NaN is incomparable with any value, this method returns `false` when called on NaN or when NaN is passed as `other`.
- `-infinity` compares less than or equal to all values except NaN.
- Every value except NaN compares less than or equal to `+infinity`.

The following example shows the behavior of the `isLessThanOrEqualTo(_:)` method with different kinds of values:

```swift
let x = 15.0
x.isLessThanOrEqualTo(20.0)
// true
x.isLessThanOrEqualTo(.nan)
// false
Double.nan.isLessThanOrEqualTo(x)
// false
```

The `isLessThanOrEqualTo(_:)` method implements the less-than-or-equal predicate defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

### Comparing Values

- [Floating-Point Operators for Float](../floating-point-operators-for-float.md) — Perform arithmetic and bitwise operations or compare values.
- [isEqual(to:)](<isequal(to_).md>) — Returns a Boolean value indicating whether this instance is equal to the given value.
- [isLess(than:)](<isless(than_).md>) — Returns a Boolean value indicating whether this instance is less than the given value.
- [isTotallyOrdered(belowOrEqualTo:)](<istotallyordered(beloworequalto_).md>) — Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [maximum(_:_:)](<maximum(____).md>) — Returns the greater of the two given values.
- [maximumMagnitude(_:_:)](<maximummagnitude(____).md>) — Returns the value with greater magnitude.
- [minimum(_:_:)](<minimum(____).md>) — Returns the lesser of the two given values.
- [minimumMagnitude(_:_:)](<minimummagnitude(____).md>) — Returns the value with lesser magnitude.
