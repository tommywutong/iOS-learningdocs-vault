---
title: 'build_flatMap(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_flatmap(_:_:)-7d3x7'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_flatmap(_:_:)-7d3x7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_flatmap%28_%3A_%3A%29-7d3x7.json'
content_hash: 'sha256:4c0745b12c27f9ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_flatMap(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_flatMap<LHS, RHS, Wrapped, Result>(_ wrapped: LHS, _ builder: (PredicateExpressions.Variable<Wrapped>) -> RHS) -> PredicateExpressions.OptionalFlatMap<LHS, Wrapped, RHS, Result> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output == Wrapped?, RHS.Output == Result?
```
