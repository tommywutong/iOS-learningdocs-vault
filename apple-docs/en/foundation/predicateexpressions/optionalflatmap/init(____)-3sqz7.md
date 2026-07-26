---
title: 'init(_:_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/optionalflatmap/init(_:_:)-3sqz7'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/optionalflatmap/init(_:_:)-3sqz7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/optionalflatmap/init%28_%3A_%3A%29-3sqz7.json'
content_hash: 'sha256:76493aaa2ecad533'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [PredicateExpressions](../../predicateexpressions.md) · [OptionalFlatMap](../optionalflatmap.md)

# init(_:_:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ wrapped: LHS, _ builder: (PredicateExpressions.Variable<Wrapped>) -> RHS) where RHS.Output == Result?
```
