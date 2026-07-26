---
title: 'build_Division(lhs:rhs:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_division(lhs:rhs:)-958g1'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_division(lhs:rhs:)-958g1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_division%28lhs%3Arhs%3A%29-958g1.json'
content_hash: 'sha256:b12e8e6481d20527'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_Division(lhs:rhs:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_Division<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.IntDivision<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : BinaryInteger, LHS.Output == RHS.Output
```
