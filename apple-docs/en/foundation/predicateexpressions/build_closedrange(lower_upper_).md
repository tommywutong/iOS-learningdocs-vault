---
title: 'build_ClosedRange(lower:upper:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_closedrange(lower:upper:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_closedrange(lower:upper:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_closedrange%28lower%3Aupper%3A%29.json'
content_hash: 'sha256:4bc3380c047c7c07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_ClosedRange(lower:upper:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_ClosedRange<LHS, RHS>(lower: LHS, upper: RHS) -> PredicateExpressions.ClosedRange<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Comparable, LHS.Output == RHS.Output
```
