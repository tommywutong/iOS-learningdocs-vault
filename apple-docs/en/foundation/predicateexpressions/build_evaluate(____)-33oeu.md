---
title: 'build_evaluate(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_evaluate(_:_:)-33oeu'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_evaluate(_:_:)-33oeu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_evaluate%28_%3A_%3A%29-33oeu.json'
content_hash: 'sha256:a6715d25e1c78a1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_evaluate(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_evaluate<Transformation, each Input, Output>(_ expression: Transformation, _ input: repeat each Input) -> PredicateExpressions.ExpressionEvaluate<Transformation, repeat each Input, Output> where Transformation : PredicateExpression, repeat each Input : PredicateExpression, Transformation.Output == Expression<repeat (each Input).Output, Output>
```
