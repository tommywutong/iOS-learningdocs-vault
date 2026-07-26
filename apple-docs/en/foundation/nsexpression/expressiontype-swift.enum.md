---
title: NSExpression.ExpressionType
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression/expressiontype-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/expressiontype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/expressiontype-swift.enum.json'
content_hash: 'sha256:d9d7f91cd6efd61a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# NSExpression.ExpressionType

<sub>Enumeration</sub>

Defines the possible types of an expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ExpressionType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSConstantValueExpressionType](expressiontype-swift.enum/constantvalue.md) — An expression that always returns the same value.
- [NSEvaluatedObjectExpressionType](expressiontype-swift.enum/evaluatedobject.md) — An expression that always returns the parameter object itself.
- [NSVariableExpressionType](expressiontype-swift.enum/variable.md) — An expression that always returns whatever value is associated with the key specified by ‘variable’ in the bindings dictionary.
- [NSKeyPathExpressionType](expressiontype-swift.enum/keypath.md) — An expression that returns something that can be used as a key path.
- [NSFunctionExpressionType](expressiontype-swift.enum/function.md) — An expression that returns the result of evaluating a function.
- [NSUnionSetExpressionType](expressiontype-swift.enum/unionset.md) — An expression that creates a union of the results of two nested expressions.
- [NSIntersectSetExpressionType](expressiontype-swift.enum/intersectset.md) — An expression that creates an intersection of the results of two nested expressions.
- [NSMinusSetExpressionType](expressiontype-swift.enum/minusset.md) — An expression that combines two nested expression results by set subtraction.
- [NSSubqueryExpressionType](expressiontype-swift.enum/subquery.md) — An expression that filters a collection using a subpredicate.
- [NSAggregateExpressionType](expressiontype-swift.enum/aggregate.md) — An expression that defines an aggregate of `NSExpression` objects.
- [NSAnyKeyExpressionType](expressiontype-swift.enum/anykey.md) — An expression that represents any key.
- [NSBlockExpressionType](expressiontype-swift.enum/block.md) — An expression that uses a Block.
- [NSConditionalExpressionType](expressiontype-swift.enum/conditional.md) — A conditional expression that evaluates a predicate to determine which expression to return.

### Initializers

- [init(rawValue:)](<expressiontype-swift.enum/init(rawvalue_).md>)

## See Also

### Getting Information About an Expression

- [arguments](arguments.md) — The arguments for the expression.
- [collection](collection.md) — The collection of expressions in an aggregate expression, or the collection element of a subquery expression.
- [constantValue](constantvalue.md) — The constant value of the expression.
- [expressionType](expressiontype-swift.property.md) — The expression type for the expression.
- [function](function.md) — The function for the expression.
- [keyPath](keypath.md) — The key path for the expression.
- [operand](operand.md) — The operand for the expression.
- [predicate](predicate.md) — The predicate of a subquery expression.
- [leftExpression](left.md) — The left expression of an aggregate expression.
- [rightExpression](right.md) — The right expression of an aggregate expression.
- [variable](variable.md) — The variable for the expression.
