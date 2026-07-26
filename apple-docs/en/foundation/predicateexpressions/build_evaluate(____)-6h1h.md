---
title: 'build_evaluate(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_evaluate(_:_:)-6h1h'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_evaluate(_:_:)-6h1h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_evaluate%28_%3A_%3A%29-6h1h.json'
content_hash: 'sha256:ff22ea080e5b057f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_evaluate(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_evaluate<Condition, each Input>(_ predicate: Condition, _ input: repeat each Input) -> PredicateExpressions.PredicateEvaluate<Condition, repeat each Input> where Condition : PredicateExpression, repeat each Input : PredicateExpression, Condition.Output == Predicate<repeat (each Input).Output>
```
