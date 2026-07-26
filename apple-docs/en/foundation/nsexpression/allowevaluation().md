---
title: allowEvaluation()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression/allowevaluation()
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/allowevaluation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/allowevaluation%28%29.json'
content_hash: 'sha256:36df5db020e396e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# allowEvaluation()

<sub>Instance Method</sub>

Forces a securely decoded expression to allow evaluation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func allowEvaluation()
```

## Discussion

When securely decoding an `NSExpression` object encoded using [NSSecureCoding](../nssecurecoding.md), evaluation is disabled because it is potentially unsafe to evaluate expressions you get out of an archive.

Before you enable evaluation, you should validate key paths, selectors, etc to ensure no erroneous or malicious code will be executed. Once you’ve preflighted the expression, you can enable the expression for evaluation by calling `allowEvaluation`.

## See Also

### Evaluating an Expression

- [- expressionValueWithObject:context:](<expressionvalue(with_context_).md>) — Evaluates an expression using a specified object and context.
- [falseExpression](false.md) — An expression to evalutate if a conditional expression’s predicate evaluates to false.
- [trueExpression](true.md) — An expression to evalutate if a conditional expression’s predicate evaluates to true.
