---
title: 'build_Conjunction(lhs:rhs:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_conjunction(lhs:rhs:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_conjunction(lhs:rhs:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_conjunction%28lhs%3Arhs%3A%29.json'
content_hash: 'sha256:805859b3d5391423'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_Conjunction(lhs:rhs:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_Conjunction<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.Conjunction<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output == Bool, RHS.Output == Bool
```
