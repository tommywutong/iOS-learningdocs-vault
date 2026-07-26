---
title: 'expressionValue(with:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/expressionvalue(with:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/expressionvalue(with:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/expressionvalue%28with%3Acontext%3A%29.json'
content_hash: 'sha256:0a2cbd329d583842'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# expressionValue(with:context:)

<sub>Instance Method</sub>

Evaluates an expression using a specified object and context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func expressionValue(with object: Any?, context: NSMutableDictionary?) -> Any?
```

## Parameters

- `object` — The object against which the expression is evaluated.

- `context` — A dictionary that the expression can use to store temporary state for one predicate evaluation. Can be `nil`. Note that `context` is mutable, and that it can only be accessed during the evaluation of the expression. You must not attempt to retain it for use elsewhere.

## Return Value

The evaluated object.

## See Also

### Evaluating an Expression

- [- allowEvaluation](<allowevaluation().md>) — Forces a securely decoded expression to allow evaluation.
- [falseExpression](false.md) — An expression to evalutate if a conditional expression’s predicate evaluates to false.
- [trueExpression](true.md) — An expression to evalutate if a conditional expression’s predicate evaluates to true.
