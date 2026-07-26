---
title: 'build_starts(_:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_starts(_:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_starts(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_starts%28_%3Awith%3A%29.json'
content_hash: 'sha256:75fb65017b3d9bd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_starts(_:with:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_starts<Base, Prefix>(_ base: Base, with prefix: Prefix) -> PredicateExpressions.SequenceStartsWith<Base, Prefix> where Base : PredicateExpression, Prefix : PredicateExpression, Base.Output : Sequence, Prefix.Output : Sequence, Base.Output.Element : Equatable, Base.Output.Element == Prefix.Output.Element
```
