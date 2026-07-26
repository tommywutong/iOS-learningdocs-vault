---
title: 'sort(options:usingComparator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/sort(options:usingcomparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/sort(options:usingcomparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/sort%28options%3Ausingcomparator%3A%29.json'
content_hash: 'sha256:efca0477c31a2e6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# sort(options:usingComparator:)

<sub>Instance Method</sub>

Sorts the mutable ordered set using the specified options and the comparison method specified by a given comparator block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sort(options opts: NSSortOptions = [], usingComparator cmptr: (Any, Any) -> ComparisonResult)
```

## Parameters

- `opts` — A bitmask that specifies the options for the sort (whether it should be performed concurrently and whether it should be performed stably).

- `cmptr` — A comparator block.

## See Also

### Sorting Entries

- [- sortUsingDescriptors:](<sort(using_).md>) — Sorts the receiving ordered set using a given array of sort descriptors.
- [- sortUsingComparator:](<sort(comparator_).md>) — Sorts the mutable ordered set using the comparison method specified by the comparator block.
- [- sortRange:options:usingComparator:](<sortrange(__options_usingcomparator_).md>) — Sorts the specified range of the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
