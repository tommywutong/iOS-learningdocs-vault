---
title: 'sort(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/sort(using:)-537vs'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/sort(using:)-537vs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/sort%28using%3A%29-537vs.json'
content_hash: 'sha256:4380cfda45ebd719'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# sort(using:)

<sub>Instance Method</sub>

Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sort(using comparator: Selector)
```

## Parameters

- `comparator` — A selector that specifies the comparison method to use to compare elements in the array. The `comparator` message is sent to each object in the array and has as its single argument another object in the array. The `comparator` method should return `NSOrderedAscending` if the array is smaller than the argument, `NSOrderedDescending` if the array is larger than the argument, and `NSOrderedSame` if they are equal.

## See Also

### Related Documentation

- [- sortedArrayUsingSelector:](<../nsarray/sortedarray(using_)-9nhh9.md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.

### Rearranging Content

- [- exchangeObjectAtIndex:withObjectAtIndex:](<exchangeobject(at_withobjectat_).md>) — Exchanges the objects in the array at given indexes.
- [- sortUsingDescriptors:](<sort(using_)-4eh07.md>) — Sorts the receiver using a given array of sort descriptors.
- [- sortUsingComparator:](<sort(comparator_).md>) — Sorts the receiver in ascending order using the comparison method specified by a given [Comparator](../comparator.md) block.
- [- sortWithOptions:usingComparator:](<sort(options_usingcomparator_).md>) — Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [Comparator](../comparator.md) block.
- [- sortUsingFunction:context:](<sort(__context_).md>) — Sorts the receiver in ascending order as defined by the comparison function `compare`.
