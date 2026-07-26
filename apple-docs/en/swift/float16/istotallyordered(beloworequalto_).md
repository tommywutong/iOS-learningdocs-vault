---
title: 'isTotallyOrdered(belowOrEqualTo:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/istotallyordered(beloworequalto:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/istotallyordered(beloworequalto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/istotallyordered%28beloworequalto%3A%29.json'
content_hash: 'sha256:01104516bd2b142e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# isTotallyOrdered(belowOrEqualTo:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isTotallyOrdered(belowOrEqualTo other: Self) -> Bool
```

## Parameters

- `other` — A floating-point value to compare to this value.

## Return Value

`true` if this value is ordered below or the same as `other` in a total ordering of the floating-point type; otherwise, `false`.

## Discussion

This relation is a refinement of the less-than-or-equal-to operator (`<=`) that provides a total order on all values of the type, including signed zeros and NaNs.

The following example uses `isTotallyOrdered(belowOrEqualTo:)` to sort an array of floating-point values, including some that are NaN:

```swift
var numbers = [2.5, 21.25, 3.0, .nan, -9.5]
numbers.sort { !$1.isTotallyOrdered(belowOrEqualTo: $0) }
print(numbers)
// Prints "[-9.5, 2.5, 3.0, 21.25, nan]"
```

The `isTotallyOrdered(belowOrEqualTo:)` method implements the total order relation as defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
