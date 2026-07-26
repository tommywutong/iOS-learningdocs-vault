---
title: 'build_caseInsensitiveCompare(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_caseinsensitivecompare(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_caseinsensitivecompare(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_caseinsensitivecompare%28_%3A_%3A%29.json'
content_hash: 'sha256:668b1fa67fb3a723'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_caseInsensitiveCompare(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_caseInsensitiveCompare<Root, Other>(_ root: Root, _ other: Other) -> PredicateExpressions.StringCaseInsensitiveCompare<Root, Other> where Root : PredicateExpression, Other : PredicateExpression, Root.Output : StringProtocol, Other.Output : StringProtocol
```
