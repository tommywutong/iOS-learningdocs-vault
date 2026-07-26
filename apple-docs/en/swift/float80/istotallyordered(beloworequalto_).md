---
title: 'isTotallyOrdered(belowOrEqualTo:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/istotallyordered(beloworequalto:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/istotallyordered(beloworequalto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/istotallyordered%28beloworequalto%3A%29.json'
content_hash: 'sha256:0cf6de2db36d03e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isTotallyOrdered(belowOrEqualTo:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.

<sub>macOS</sub>

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
