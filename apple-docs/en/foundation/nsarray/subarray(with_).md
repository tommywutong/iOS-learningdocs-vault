---
title: 'subarray(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/subarray(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/subarray(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/subarray%28with%3A%29.json'
content_hash: 'sha256:c76162864fc1a82c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# subarray(with:)

<sub>Instance Method</sub>

Returns a new array containing the receiving array’s elements that fall within the limits specified by a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subarray(with range: NSRange) -> [Any]
```

## Parameters

- `range` — A range within the receiving array’s range of elements.

## Return Value

A new array containing the receiving array’s elements that fall within the limits specified by `range`.

## Discussion

If `range` isn’t within the receiving array’s range of elements, an `NSRangeException` is raised.

For example, the following code example creates an array containing the elements found in the first half of `wholeArray` (assuming `wholeArray` exists).

```objc
NSArray *halfArray;
NSRange theRange;
 
theRange.location = 0;
theRange.length = [wholeArray count] / 2;
 
halfArray = [wholeArray subarrayWithRange:theRange];
```

## See Also

### Deriving New Arrays

- [- arrayByAddingObject:](<adding(__).md>) — Returns a new array that is a copy of the receiving array with a given object added to the end.
- [- arrayByAddingObjectsFromArray:](<addingobjects(from_).md>) — Returns a new array that is a copy of the receiving array with the objects contained in another array added to the end.
- [- filteredArrayUsingPredicate:](<filtered(using_).md>) — Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.
