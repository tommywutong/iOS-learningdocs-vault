---
title: 'init(forConditional:trueExpression:falseExpression:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(forconditional:trueexpression:falseexpression:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(forconditional:trueexpression:falseexpression:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28forconditional%3Atrueexpression%3Afalseexpression%3A%29.json'
content_hash: 'sha256:8ada5dd2b125da7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(forConditional:trueExpression:falseExpression:)

<sub>Initializer</sub>

Creates an expression that returns a result, depending on the value of predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forConditional predicate: NSPredicate, trueExpression: NSExpression, falseExpression: NSExpression)
```

## Parameters

- `predicate` — The predicate for determining whether the element belongs in the result collection.

- `trueExpression` — The expression for evaluation when the predicate evaluates to `true`.

- `falseExpression` — The expression for evaluation when the predicate evaluates to `false`.
