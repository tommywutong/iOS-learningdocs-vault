---
title: 'init(integersIn:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/init(integersin:)-2zs95'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/init(integersin:)-2zs95'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/init%28integersin%3A%29-2zs95.json'
content_hash: 'sha256:4a095d40e6cfef83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# init(integersIn:)

<sub>Initializer</sub>

Initialize an `IndexSet` with a range of integers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<R>(integersIn range: R) where R : RangeExpression, R.Bound == Int
```
