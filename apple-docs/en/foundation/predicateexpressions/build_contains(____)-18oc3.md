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
doc_path: '/documentation/foundation/predicateexpressions/build_contains(_:_:)-18oc3'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_contains(_:_:)-18oc3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_contains%28_%3A_%3A%29-18oc3.json'
content_hash: 'sha256:659f74ba35ccc158'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_contains(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_contains<Base, Other>(_ base: Base, _ other: Other) -> PredicateExpressions.CollectionContainsCollection<Base, Other> where Base : PredicateExpression, Other : PredicateExpression, Base.Output : Collection, Other.Output : Collection, Base.Output.Element : Equatable, Base.Output.Element == Other.Output.Element
```
