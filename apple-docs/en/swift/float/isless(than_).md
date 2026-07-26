---
title: 'isLess(than:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/isless(than:)'
source_url: 'https://developer.apple.com/documentation/swift/float/isless(than:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/isless%28than%3A%29.json'
content_hash: 'sha256:b5180ec915aa841d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# isLess(than:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this instance is less than the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isLess(than other: Float) -> Bool
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

## See Also

### Comparing Values

- [Floating-Point Operators for Float](../floating-point-operators-for-float.md) — Perform arithmetic and bitwise operations or compare values.
- [isEqual(to:)](<isequal(to_).md>) — Returns a Boolean value indicating whether this instance is equal to the given value.
- [isLessThanOrEqualTo(_:)](<islessthanorequalto(__).md>) — Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [isTotallyOrdered(belowOrEqualTo:)](<istotallyordered(beloworequalto_).md>) — Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [maximum(_:_:)](<maximum(____).md>) — Returns the greater of the two given values.
- [maximumMagnitude(_:_:)](<maximummagnitude(____).md>) — Returns the value with greater magnitude.
- [minimum(_:_:)](<minimum(____).md>) — Returns the lesser of the two given values.
- [minimumMagnitude(_:_:)](<minimummagnitude(____).md>) — Returns the value with lesser magnitude.
