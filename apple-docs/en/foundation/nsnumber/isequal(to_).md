---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsnumber/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsnumber/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnumber/isequal%28to%3A%29.json'
content_hash: 'sha256:5c0becf30a0d7987'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNumber](../nsnumber.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the number object’s value and a given number are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to number: NSNumber) -> Bool
```

## Parameters

- `number` — The number to compare to the number object’s value.

## Return Value

[true](../../swift/true.md) if the number object’s value and `number` are equal, otherwise [false](../../swift/false.md).

## Discussion

Two `NSNumber` objects are considered equal if they have the same id values or if they have equivalent values (as determined by the [- compare:](<compare(__).md>) method).

This method is more efficient than [- compare:](<compare(__).md>) if you know the two objects are numbers.

## See Also

### Comparing NSNumber Objects

- [- compare:](<compare(__).md>) — Returns an `NSComparisonResult` value that indicates whether the number object’s value is greater than, equal to, or less than a given number.
