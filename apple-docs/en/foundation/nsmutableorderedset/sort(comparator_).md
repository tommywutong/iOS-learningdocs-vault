---
title: 'sort(comparator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/sort(comparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/sort(comparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/sort%28comparator%3A%29.json'
content_hash: 'sha256:39b8a3df58eb0428'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# sort(comparator:)

<sub>Instance Method</sub>

Sorts the mutable ordered set using the comparison method specified by the comparator block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sort(comparator cmptr: (Any, Any) -> ComparisonResult)
```

## Parameters

- `cmptr` — A comparator block.

## See Also

### Sorting Entries

- [- sortUsingDescriptors:](<sort(using_).md>) — Sorts the receiving ordered set using a given array of sort descriptors.
- [- sortWithOptions:usingComparator:](<sort(options_usingcomparator_).md>) — Sorts the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
- [- sortRange:options:usingComparator:](<sortrange(__options_usingcomparator_).md>) — Sorts the specified range of the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
