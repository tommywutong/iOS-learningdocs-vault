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
doc_path: '/documentation/foundation/indexset/rangeview(of:)-5xqe8'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/rangeview(of:)-5xqe8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/rangeview%28of%3A%29-5xqe8.json'
content_hash: 'sha256:d9b12d63a4607e0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# rangeView(of:)

<sub>Instance Method</sub>

Returns a `Range`-based view of `self`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rangeView(of range: Range<IndexSet.Element>) -> IndexSet.RangeView
```

## Parameters

- `range` — A subrange of `self` to view.

## See Also

### Getting a Range-Based View

- [rangeView](rangeview-swift.property.md) — Returns a `Range`-based view of the entire contents of `self`.
- [RangeView](rangeview-swift.struct.md) — A view of the contents of an IndexSet, organized by range.
