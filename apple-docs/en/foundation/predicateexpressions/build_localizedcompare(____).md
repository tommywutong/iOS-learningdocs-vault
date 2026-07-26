---
title: 'build_localizedCompare(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_localizedcompare(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_localizedcompare(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_localizedcompare%28_%3A_%3A%29.json'
content_hash: 'sha256:2f8d5eb94da4e91a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_localizedCompare(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_localizedCompare<Root, Other>(_ root: Root, _ other: Other) -> PredicateExpressions.StringLocalizedCompare<Root, Other> where Root : PredicateExpression, Other : PredicateExpression, Root.Output : StringProtocol, Other.Output : StringProtocol
```
