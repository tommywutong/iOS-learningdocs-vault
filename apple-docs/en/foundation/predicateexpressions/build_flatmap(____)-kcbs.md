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
doc_path: '/documentation/foundation/predicateexpressions/build_flatmap(_:_:)-kcbs'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_flatmap(_:_:)-kcbs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_flatmap%28_%3A_%3A%29-kcbs.json'
content_hash: 'sha256:6578674c4d3e799f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_flatMap(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_flatMap<LHS, RHS, Wrapped, Result>(_ wrapped: LHS, _ builder: (PredicateExpressions.Variable<Wrapped>) -> RHS) -> PredicateExpressions.OptionalFlatMap<LHS, Wrapped, RHS, Result> where LHS : PredicateExpression, RHS : PredicateExpression, Result == RHS.Output, LHS.Output == Wrapped?
```
