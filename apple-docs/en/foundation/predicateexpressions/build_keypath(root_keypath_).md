---
title: 'build_KeyPath(root:keyPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_keypath(root:keypath:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_keypath(root:keypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_keypath%28root%3Akeypath%3A%29.json'
content_hash: 'sha256:3cb6b0b42180d08d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_KeyPath(root:keyPath:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_KeyPath<Root, Value>(root: Root, keyPath: any KeyPath<Root.Output, Value> & Sendable) -> PredicateExpressions.KeyPath<Root, Value> where Root : PredicateExpression
```
