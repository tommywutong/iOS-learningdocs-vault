---
title: 'indexRange(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/indexrange(in:)-6057o'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/indexrange(in:)-6057o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/indexrange%28in%3A%29-6057o.json'
content_hash: 'sha256:f3e634cf601a5abe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# indexRange(in:)

<sub>Instance Method</sub>

Return a `Range<IndexSet.Index>` which can be used to subscript the index set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indexRange<R>(in range: R) -> Range<IndexSet.Index> where R : RangeExpression, R.Bound == Int
```

## Parameters

- `range` — The range of integers to include.

## Discussion

The resulting range is the range of the intersection of the integers in `range` with the index set.
