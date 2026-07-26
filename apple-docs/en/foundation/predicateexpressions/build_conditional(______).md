---
title: 'build_Conditional(_:_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_conditional(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_conditional(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_conditional%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cbe9947fb8bb5ad3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_Conditional(_:_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_Conditional<Test, If, Else>(_ test: Test, _ trueBranch: If, _ falseBranch: Else) -> PredicateExpressions.Conditional<Test, If, Else> where Test : PredicateExpression, If : PredicateExpression, Else : PredicateExpression, Test.Output == Bool, If.Output == Else.Output
```
