---
title: 'compare(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsnumber/compare(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsnumber/compare(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnumber/compare%28_%3A%29.json'
content_hash: 'sha256:6a5e03c4ea649c83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNumber](../nsnumber.md)

# compare(_:)

<sub>Instance Method</sub>

Returns an `NSComparisonResult` value that indicates whether the number object’s value is greater than, equal to, or less than a given number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compare(_ otherNumber: NSNumber) -> ComparisonResult
```

## Parameters

- `otherNumber` — The number to compare to the number object’s value. This value must not be `nil`. If the value is `nil`, the behavior is undefined and may change in future versions of macOS.

## Return Value

`NSOrderedAscending` if the value of `otherNumber` is greater than the number object’s, `NSOrderedSame` if they’re equal, and `NSOrderedDescending` if the value of `otherNumber` is less than the number object’s.

## Discussion

The [- compare:](<compare(__).md>) method follows the standard C rules for type conversion. For example, if you compare an `NSNumber` object that has an integer value with an `NSNumber` object that has a floating point value, the integer value is converted to a floating-point value for comparison.

## See Also

### Comparing NSNumber Objects

- [- isEqualToNumber:](<isequal(to_).md>) — Returns a Boolean value that indicates whether the number object’s value and a given number are equal.
