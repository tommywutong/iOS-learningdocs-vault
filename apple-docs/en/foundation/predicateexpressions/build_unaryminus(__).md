---
title: 'build_UnaryMinus(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_unaryminus(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_unaryminus(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_unaryminus%28_%3A%29.json'
content_hash: 'sha256:7d68546b52313f2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_UnaryMinus(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_UnaryMinus<T>(_ inner: T) -> PredicateExpressions.UnaryMinus<T> where T : PredicateExpression, T.Output : SignedNumeric
```
