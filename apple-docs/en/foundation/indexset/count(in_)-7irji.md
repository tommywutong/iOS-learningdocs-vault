---
title: 'count(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/count(in:)-7irji'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/count(in:)-7irji'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/count%28in%3A%29-7irji.json'
content_hash: 'sha256:11b4b4dfe11815f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# count(in:)

<sub>Instance Method</sub>

Returns the count of integers in `self` that intersect `range`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func count<R>(in range: R) -> Int where R : RangeExpression, R.Bound == Int
```
