---
title: 'sortedArray(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/sortedarray(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/sortedarray(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/sortedarray%28using%3A%29.json'
content_hash: 'sha256:1b070a3596a23c6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# sortedArray(using:)

<sub>Instance Method</sub>

Returns an array of the ordered set’s elements sorted as specified by a given array of sort descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sortedArray(using sortDescriptors: [NSSortDescriptor]) -> [Any]
```

## Parameters

- `sortDescriptors` — An array of [NSSortDescriptor](../nssortdescriptor.md) objects.

## Return Value

An `NSArray` containing the ordered set’s elements sorted as specified by `sortDescriptors`.

## Discussion

The first descriptor specifies the primary key path to be used in sorting the ordered set’s elements. Any subsequent descriptors are used to further refine sorting of objects with duplicate values. See [NSSortDescriptor](../nssortdescriptor.md) for additional information.

## See Also

### Creating a Sorted Array

- [- sortedArrayUsingComparator:](<sortedarray(comparator_).md>) — Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block
- [- sortedArrayWithOptions:usingComparator:](<sortedarray(options_usingcomparator_).md>) — Returns an array that lists the receiving ordered set’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
