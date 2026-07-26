---
title: 'sort(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/sort(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/sort(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/sort%28using%3A%29.json'
content_hash: 'sha256:e3c66750dbf47e7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# sort(using:)

<sub>Instance Method</sub>

Sorts the receiving ordered set using a given array of sort descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sort(using sortDescriptors: [NSSortDescriptor])
```

## Parameters

- `sortDescriptors` — An array containing the `NSSortDescriptor` objects to use to sort the receiving ordered set’s contents.

## Discussion

See [NSSortDescriptor](../nssortdescriptor.md) for additional information.

## See Also

### Sorting Entries

- [- sortUsingComparator:](<sort(comparator_).md>) — Sorts the mutable ordered set using the comparison method specified by the comparator block.
- [- sortWithOptions:usingComparator:](<sort(options_usingcomparator_).md>) — Sorts the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
- [- sortRange:options:usingComparator:](<sortrange(__options_usingcomparator_).md>) — Sorts the specified range of the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
