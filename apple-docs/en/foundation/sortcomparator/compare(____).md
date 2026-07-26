---
title: 'compare(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/sortcomparator/compare(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/sortcomparator/compare(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortcomparator/compare%28_%3A_%3A%29.json'
content_hash: 'sha256:b58285ae8a079cff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SortComparator](../sortcomparator.md)

# compare(_:_:)

<sub>Instance Method</sub>

Provides the relative ordering of two elements based on the sort order of the comparator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compare(_ lhs: Self.Compared, _ rhs: Self.Compared) -> ComparisonResult
```

## Parameters

- `lhs` — The first element to compare.

- `rhs` — The second element to compare.

## Return Value

The relative ordering between the two elements according to the sort order of the comparator.

## See Also

### Using a Comparator

- [Compared](compared.md) — A type that the sort comparator can compare.
