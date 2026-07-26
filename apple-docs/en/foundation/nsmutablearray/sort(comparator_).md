---
title: 'sort(comparator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/sort(comparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/sort(comparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/sort%28comparator%3A%29.json'
content_hash: 'sha256:988b380b884f1dfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# sort(comparator:)

<sub>Instance Method</sub>

Sorts the receiver in ascending order using the comparison method specified by a given [Comparator](../comparator.md) block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sort(comparator cmptr: (Any, Any) -> ComparisonResult)
```

## Parameters

- `cmptr` — A comparator block.

## See Also

### Related Documentation

- [- sortedArrayUsingDescriptors:](<../nsarray/sortedarray(using_)-82wi1.md>) — Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.

### Rearranging Content

- [- exchangeObjectAtIndex:withObjectAtIndex:](<exchangeobject(at_withobjectat_).md>) — Exchanges the objects in the array at given indexes.
- [- sortUsingDescriptors:](<sort(using_)-4eh07.md>) — Sorts the receiver using a given array of sort descriptors.
- [- sortWithOptions:usingComparator:](<sort(options_usingcomparator_).md>) — Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [Comparator](../comparator.md) block.
- [- sortUsingFunction:context:](<sort(__context_).md>) — Sorts the receiver in ascending order as defined by the comparison function `compare`.
- [- sortUsingSelector:](<sort(using_)-537vs.md>) — Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.
