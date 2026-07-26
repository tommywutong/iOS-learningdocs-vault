---
title: 'build_allSatisfy(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_allsatisfy(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_allsatisfy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_allsatisfy%28_%3A_%3A%29.json'
content_hash: 'sha256:191a47451108c241'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_allSatisfy(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_allSatisfy<LHS, RHS>(_ lhs: LHS, _ builder: (PredicateExpressions.Variable<LHS.Output.Element>) -> RHS) -> PredicateExpressions.SequenceAllSatisfy<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output == Bool
```
