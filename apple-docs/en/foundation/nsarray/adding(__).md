---
title: 'adding(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/adding(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/adding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/adding%28_%3A%29.json'
content_hash: 'sha256:af2dcd4c54c62e32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# adding(_:)

<sub>Instance Method</sub>

Returns a new array that is a copy of the receiving array with a given object added to the end.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func adding(_ anObject: Any) -> [Any]
```

## Parameters

- `anObject` — An object.

## Return Value

A new array that is a copy of the receiving array with `anObject` added to the end.

## Discussion

If `anObject` is `nil`, an `NSInvalidArgumentException` is raised.

## See Also

### Related Documentation

- [- addObject:](<../nsmutablearray/add(__).md>) — Inserts a given object at the end of the array.

### Deriving New Arrays

- [- arrayByAddingObjectsFromArray:](<addingobjects(from_).md>) — Returns a new array that is a copy of the receiving array with the objects contained in another array added to the end.
- [- filteredArrayUsingPredicate:](<filtered(using_).md>) — Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.
- [- subarrayWithRange:](<subarray(with_).md>) — Returns a new array containing the receiving array’s elements that fall within the limits specified by a given range.
