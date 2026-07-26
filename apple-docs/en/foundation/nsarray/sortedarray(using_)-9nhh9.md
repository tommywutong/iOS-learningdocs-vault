---
title: 'sortedArray(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/sortedarray(using:)-9nhh9'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/sortedarray(using:)-9nhh9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/sortedarray%28using%3A%29-9nhh9.json'
content_hash: 'sha256:c4f98d4c268cc4fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# sortedArray(using:)

<sub>Instance Method</sub>

Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sortedArray(using comparator: Selector) -> [Any]
```

## Parameters

- `comparator` — A selector that identifies the method to use to compare two elements at a time. The method should return `NSOrderedAscending` if the receiving array is smaller than the argument, `NSOrderedDescending` if the receiving array is larger than the argument, and `NSOrderedSame` if they are equal.

## Return Value

An array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by the selector `comparator`.

## Discussion

The new array contains references to the receiving array’s elements, not copies of them.

The `comparator` message is sent to each object in the array and has as its single argument another object in the array.

For example, an array of `NSString` objects can be sorted by using the [- caseInsensitiveCompare:](<../nsstring/caseinsensitivecompare(__).md>) method declared in the `NSString` class. Assuming `anArray` exists, a sorted version of the array can be created in this way:

```objc
     NSArray *sortedArray =
         [anArray sortedArrayUsingSelector:@selector(caseInsensitiveCompare:)];
```

## See Also

### Sorting

- [sortedArrayHint](sortedarrayhint.md) — Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [- sortedArrayUsingFunction:context:hint:](<sortedarray(__context_hint_).md>).
- [- sortedArrayUsingFunction:context:](<sortedarray(__context_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingFunction:context:hint:](<sortedarray(__context_hint_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingDescriptors:](<sortedarray(using_)-82wi1.md>) — Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [- sortedArrayUsingComparator:](<sortedarray(comparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [- sortedArrayWithOptions:usingComparator:](<sortedarray(options_usingcomparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [Comparator](../comparator.md) — Defines the signature for a block object used for comparison operations.
