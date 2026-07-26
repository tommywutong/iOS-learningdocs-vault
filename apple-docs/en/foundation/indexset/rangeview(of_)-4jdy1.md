---
title: 'rangeView(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/rangeview(of:)-4jdy1'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/rangeview(of:)-4jdy1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/rangeview%28of%3A%29-4jdy1.json'
content_hash: 'sha256:f1e220dbf3652154'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# rangeView(of:)

<sub>Instance Method</sub>

Returns a `Range`-based view of `self`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rangeView<R>(of range: R) -> IndexSet.RangeView where R : RangeExpression, R.Bound == Int
```

## Parameters

- `range` — A subrange of `self` to view.
