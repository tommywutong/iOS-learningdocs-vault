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
doc_path: '/documentation/foundation/predicateexpressions/build_subscript(_:_:)-61z8t'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_subscript(_:_:)-61z8t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_subscript%28_%3A_%3A%29-61z8t.json'
content_hash: 'sha256:7a7c3c04c30d754d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_subscript(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_subscript<Wrapped, Key, Value>(_ wrapped: Wrapped, _ key: Key) -> PredicateExpressions.DictionaryKeySubscript<Wrapped, Key, Value> where Wrapped : PredicateExpression, Key : PredicateExpression, Wrapped.Output == [Key.Output : Value], Key.Output : Hashable
```
