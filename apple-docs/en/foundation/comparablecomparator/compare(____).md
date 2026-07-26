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
doc_path: '/documentation/foundation/comparablecomparator/compare(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/comparablecomparator/compare(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/comparablecomparator/compare%28_%3A_%3A%29.json'
content_hash: 'sha256:ef28dfa889186544'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ComparableComparator](../comparablecomparator.md)

# compare(_:_:)

<sub>Instance Method</sub>

Provides the relative ordering of two elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compare(_ lhs: Compared, _ rhs: Compared) -> ComparisonResult
```

## Parameters

- `lhs` — The first element to compare.

- `rhs` — The second element to compare.

## Return Value

The relative ordering between the two elements.

## Discussion

The method returns flipped comparisons if the sort order is [SortOrder.reverse](../sortorder/reverse.md).
