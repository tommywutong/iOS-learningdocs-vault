---
title: 'intersects(integersIn:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/intersects(integersin:)-9cq7w'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/intersects(integersin:)-9cq7w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/intersects%28integersin%3A%29-9cq7w.json'
content_hash: 'sha256:b8b9e281a6693617'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# intersects(integersIn:)

<sub>Instance Method</sub>

Returns `true` if `self` intersects any of the integers in `range`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersects<R>(integersIn range: R) -> Bool where R : RangeExpression, R.Bound == Int
```
