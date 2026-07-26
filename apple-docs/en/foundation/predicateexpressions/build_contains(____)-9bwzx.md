---
title: 'build_contains(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_contains(_:_:)-9bwzx'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_contains(_:_:)-9bwzx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_contains%28_%3A_%3A%29-9bwzx.json'
content_hash: 'sha256:0ebb0acd18649ec9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_contains(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_contains<LHS, RHS>(_ lhs: LHS, _ rhs: RHS) -> PredicateExpressions.SequenceContains<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output : Equatable, RHS.Output == LHS.Output.Element
```
