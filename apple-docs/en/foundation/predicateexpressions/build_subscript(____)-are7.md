---
title: 'build_subscript(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_subscript(_:_:)-are7'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_subscript(_:_:)-are7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_subscript%28_%3A_%3A%29-are7.json'
content_hash: 'sha256:75c28351022c08a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_subscript(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_subscript<Wrapped, Index>(_ wrapped: Wrapped, _ index: Index) -> PredicateExpressions.CollectionIndexSubscript<Wrapped, Index> where Wrapped : PredicateExpression, Index : PredicateExpression, Wrapped.Output : Collection, Index.Output == Wrapped.Output.Index
```
