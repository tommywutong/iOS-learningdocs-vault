---
title: 'build_min(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_min(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_min(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_min%28_%3A%29.json'
content_hash: 'sha256:1aa98148650f325a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_min(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_min<Elements>(_ elements: Elements) -> PredicateExpressions.SequenceMinimum<Elements> where Elements : PredicateExpression, Elements.Output : Sequence, Elements.Output.Element : Comparable
```
