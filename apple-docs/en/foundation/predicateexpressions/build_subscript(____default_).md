---
title: 'build_subscript(_:_:default:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_subscript(_:_:default:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_subscript(_:_:default:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_subscript%28_%3A_%3Adefault%3A%29.json'
content_hash: 'sha256:484dfdbe9828ae35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_subscript(_:_:default:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_subscript<Wrapped, Key, Default>(_ wrapped: Wrapped, _ key: Key, default: Default) -> PredicateExpressions.DictionaryKeyDefaultValueSubscript<Wrapped, Key, Default> where Wrapped : PredicateExpression, Key : PredicateExpression, Default : PredicateExpression, Wrapped.Output == [Key.Output : Default.Output], Key.Output : Hashable
```
