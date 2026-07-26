---
title: 'NSDecimalCompare(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalcompare(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalcompare(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalcompare%28_%3A_%3A%29.json'
content_hash: 'sha256:cf81a3e76f4b3344'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalCompare(_:_:)

<sub>Function</sub>

Compares two decimal values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSDecimalCompare(_ leftOperand: UnsafePointer<Decimal>, _ rightOperand: UnsafePointer<Decimal>) -> ComparisonResult
```

## Return Value

`NSOrderedDescending` if `leftOperand` is bigger than `rightOperand`; `NSOrderedAscending` if `rightOperand` is bigger than `leftOperand`; or `NSOrderedSame` if the two operands are equal.

## Discussion

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

## See Also

### Comparing decimals

- [isEqual(to:)](<decimal/isequal(to_).md>) — Indicates whether this decimal is equal to the specified one.
- [isLess(than:)](<decimal/isless(than_).md>) — Indicates whether this decimal is less than the specified one.
- [isLessThanOrEqualTo(_:)](<decimal/islessthanorequalto(__).md>) — Indicates whether this decimal is less than or equal to the specified one.
- [isTotallyOrdered(belowOrEqualTo:)](<decimal/istotallyordered(beloworequalto_).md>) — Returns a Boolean value indicating whether this instance should precede the given value in an ascending sort.
- [distance(to:)](<decimal/distance(to_).md>) — Returns the distance from this value to the specified value.
- [advanced(by:)](<decimal/advanced(by_).md>) — Returns a new value advanced by the given distance.
