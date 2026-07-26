---
title: true
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression/true
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/true'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/true.json'
content_hash: 'sha256:07bbf9732ca452ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# true

<sub>Instance Property</sub>

An expression to evalutate if a conditional expression’s predicate evaluates to true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var `true`: NSExpression { get }
```

## Discussion

Accessing this property raises an exception if it isn’t applicable to the expression.

## See Also

### Evaluating an Expression

- [- expressionValueWithObject:context:](<expressionvalue(with_context_).md>) — Evaluates an expression using a specified object and context.
- [- allowEvaluation](<allowevaluation().md>) — Forces a securely decoded expression to allow evaluation.
- [falseExpression](false.md) — An expression to evalutate if a conditional expression’s predicate evaluates to false.
