---
title: 'insert(integersIn:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/insert(integersin:)-9wcrp'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/insert(integersin:)-9wcrp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/insert%28integersin%3A%29-9wcrp.json'
content_hash: 'sha256:d991059ae127d822'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# insert(integersIn:)

<sub>Instance Method</sub>

Insert a range of integers into the `IndexSet`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert<R>(integersIn range: R) where R : RangeExpression, R.Bound == Int
```
