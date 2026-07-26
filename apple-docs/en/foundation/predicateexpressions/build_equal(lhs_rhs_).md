---
title: 'build_Equal(lhs:rhs:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_equal(lhs:rhs:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_equal(lhs:rhs:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_equal%28lhs%3Arhs%3A%29.json'
content_hash: 'sha256:11154790bc9da1b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_Equal(lhs:rhs:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_Equal<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.Equal<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Equatable, LHS.Output == RHS.Output
```
