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
doc_path: '/documentation/foundation/predicateexpressions/build_contains(_:_:)-9ulrw'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_contains(_:_:)-9ulrw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_contains%28_%3A_%3A%29-9ulrw.json'
content_hash: 'sha256:65f73c93f6d6dfce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_contains(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_contains<RangeExpression, Element>(_ range: RangeExpression, _ element: Element) -> PredicateExpressions.RangeExpressionContains<RangeExpression, Element> where RangeExpression : PredicateExpression, Element : PredicateExpression, RangeExpression.Output : RangeExpression, Element.Output == RangeExpression.Output.Bound
```
