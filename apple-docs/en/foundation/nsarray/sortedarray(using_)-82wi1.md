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
doc_path: '/documentation/foundation/nsarray/sortedarray(using:)-82wi1'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/sortedarray(using:)-82wi1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/sortedarray%28using%3A%29-82wi1.json'
content_hash: 'sha256:9127cbb8f307e14d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# sortedArray(using:)

<sub>Instance Method</sub>

Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sortedArray(using sortDescriptors: [NSSortDescriptor]) -> [Any]
```

## Parameters

- `sortDescriptors` — An array of `NSSortDescriptor` objects.

## Return Value

A copy of the receiving array sorted as specified by `sortDescriptors`.

## Discussion

The first descriptor specifies the primary key path to be used in sorting the receiving array’s contents. Any subsequent descriptors are used to further refine sorting of objects with duplicate values. See [NSSortDescriptor](../nssortdescriptor.md) for additional information.

## See Also

### Sorting

- [sortedArrayHint](sortedarrayhint.md) — Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [- sortedArrayUsingFunction:context:hint:](<sortedarray(__context_hint_).md>).
- [- sortedArrayUsingFunction:context:](<sortedarray(__context_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingFunction:context:hint:](<sortedarray(__context_hint_).md>) — Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [- sortedArrayUsingSelector:](<sortedarray(using_)-9nhh9.md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [- sortedArrayUsingComparator:](<sortedarray(comparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [- sortedArrayWithOptions:usingComparator:](<sortedarray(options_usingcomparator_).md>) — Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [Comparator](../comparator.md) — Defines the signature for a block object used for comparison operations.
