---
title: 'sort(_:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/sort(_:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/sort(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/sort%28_%3Acontext%3A%29.json'
content_hash: 'sha256:1e596ef9061d5d5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# sort(_:context:)

<sub>Instance Method</sub>

Sorts the receiver in ascending order as defined by the comparison function `compare`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sort(_ compare: (Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)
```

## Parameters

- `compare` — The comparison function to use to compare two elements at a time. The function’s parameters are two objects to compare and the context parameter, `context`. The function should return `NSOrderedAscending` if the first element is smaller than the second, `NSOrderedDescending` if the first element is larger than the second, and `NSOrderedSame` if the elements are equal.

- `context` — The context argument to be passed to the compare function.

## Discussion

This approach allows the comparison to be based on some outside parameter, such as whether character sorting is case sensitive or case insensitive.

## See Also

### Related Documentation

- [- sortedArrayUsingFunction:context:](<../nsarray/sortedarray(__context_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.

### Rearranging Content

- [- exchangeObjectAtIndex:withObjectAtIndex:](<exchangeobject(at_withobjectat_).md>) — Exchanges the objects in the array at given indexes.
- [- sortUsingDescriptors:](<sort(using_)-4eh07.md>) — Sorts the receiver using a given array of sort descriptors.
- [- sortUsingComparator:](<sort(comparator_).md>) — Sorts the receiver in ascending order using the comparison method specified by a given [Comparator](../comparator.md) block.
- [- sortWithOptions:usingComparator:](<sort(options_usingcomparator_).md>) — Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [Comparator](../comparator.md) block.
- [- sortUsingSelector:](<sort(using_)-537vs.md>) — Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.
