---
title: 'contains(integersIn:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/contains(integersin:)-4k1o8'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/contains(integersin:)-4k1o8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/contains%28integersin%3A%29-4k1o8.json'
content_hash: 'sha256:832e0c87a89da518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# contains(integersIn:)

<sub>Instance Method</sub>

Returns `true` if `self` contains all of the integers in `range`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains<R>(integersIn range: R) -> Bool where R : RangeExpression, R.Bound == Int
```
