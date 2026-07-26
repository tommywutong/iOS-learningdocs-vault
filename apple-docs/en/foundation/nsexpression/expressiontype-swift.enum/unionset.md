---
title: NSExpression.ExpressionType.unionSet
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression/expressiontype-swift.enum/unionset
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/expressiontype-swift.enum/unionset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/expressiontype-swift.enum/unionset.json'
content_hash: 'sha256:fc21d58d61b9780b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSExpression](../../nsexpression.md) · [ExpressionType](../expressiontype-swift.enum.md)

# NSExpression.ExpressionType.unionSet

<sub>Case</sub>

An expression that creates a union of the results of two nested expressions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case unionSet
```

## See Also

### Constants

- [NSConstantValueExpressionType](constantvalue.md) — An expression that always returns the same value.
- [NSEvaluatedObjectExpressionType](evaluatedobject.md) — An expression that always returns the parameter object itself.
- [NSVariableExpressionType](variable.md) — An expression that always returns whatever value is associated with the key specified by ‘variable’ in the bindings dictionary.
- [NSKeyPathExpressionType](keypath.md) — An expression that returns something that can be used as a key path.
- [NSFunctionExpressionType](function.md) — An expression that returns the result of evaluating a function.
- [NSIntersectSetExpressionType](intersectset.md) — An expression that creates an intersection of the results of two nested expressions.
- [NSMinusSetExpressionType](minusset.md) — An expression that combines two nested expression results by set subtraction.
- [NSSubqueryExpressionType](subquery.md) — An expression that filters a collection using a subpredicate.
- [NSAggregateExpressionType](aggregate.md) — An expression that defines an aggregate of `NSExpression` objects.
- [NSAnyKeyExpressionType](anykey.md) — An expression that represents any key.
- [NSBlockExpressionType](block.md) — An expression that uses a Block.
- [NSConditionalExpressionType](conditional.md) — A conditional expression that evaluates a predicate to determine which expression to return.
