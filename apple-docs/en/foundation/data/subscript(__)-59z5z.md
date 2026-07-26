---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/subscript(_:)-59z5z'
source_url: 'https://developer.apple.com/documentation/foundation/data/subscript(_:)-59z5z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/subscript%28_%3A%29-59z5z.json'
content_hash: 'sha256:a41f6eacbac61353'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the bytes at the specified range of indexes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<R>(rangeExpression: R) -> Data where R : RangeExpression, R.Bound : FixedWidthInteger { get set }
```
