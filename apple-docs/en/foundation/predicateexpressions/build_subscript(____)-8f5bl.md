---
title: 'build_subscript(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_subscript(_:_:)-8f5bl'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_subscript(_:_:)-8f5bl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_subscript%28_%3A_%3A%29-8f5bl.json'
content_hash: 'sha256:f59148f3c61ed848'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_subscript(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_subscript<Wrapped, Range>(_ wrapped: Wrapped, _ range: Range) -> PredicateExpressions.CollectionRangeSubscript<Wrapped, Range> where Wrapped : PredicateExpression, Range : PredicateExpression, Wrapped.Output : Collection, Range.Output == Range<Wrapped.Output.Index>
```
