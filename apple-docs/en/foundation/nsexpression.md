---
title: NSExpression
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression.json'
content_hash: 'sha256:3031d8cf3a1ec3f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSExpression

<sub>Class</sub>

An expression for use in a comparison predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSExpression
```

## Overview

Comparison operations in an [NSPredicate](nspredicate.md) derive from two expressions as instances of the [NSExpression](nsexpression.md) class. You create expressions for constant values, key paths, and so on.

Generally, anywhere in the [NSExpression](nsexpression.md) class hierarchy where there’s a composite API and subtypes that may only reasonably respond to a subset of that API, invoking a method that doesn’t make sense for that subtype throws an exception.

### Aggregate Expressions

[NSAggregateExpressionType](nsexpression/expressiontype-swift.enum/aggregate.md) allows you to create predicates containing expressions that evaluate to collections that contain further expressions. The collection may be an [NSArray](nsarray.md), [NSSet](nsset.md), or [NSDictionary](nsdictionary.md) object.

Core Data doesn’t support aggregate expressions.

### Subquery Expressions

The [NSSubqueryExpressionType](nsexpression/expressiontype-swift.enum/subquery.md) creates a subexpression that returns a subset of a collection of objects. This allows you to create sophisticated queries across relationships, such as a search for multiple correlated values on the destination object of a relationship.

### Set Expressions

The set expressions ([NSUnionSetExpressionType](nsexpression/expressiontype-swift.enum/unionset.md), [NSIntersectSetExpressionType](nsexpression/expressiontype-swift.enum/intersectset.md), and [NSMinusSetExpressionType](nsexpression/expressiontype-swift.enum/minusset.md)) combine results in a manner similar to the [NSSet](nsset.md) methods.

Both sides of these expressions must evaluate to a collection; the left side must evaluate to an `NSSet` object, and the right side can be any other collection type.

```objc
(expression UNION expression)
(expression INTERSECT expression)
(expression MINUS expression)
```

Core Data doesn’t support set expressions.

### Function Expressions

In macOS 10.4, [NSExpression](nsexpression.md) only supports a predefined set of functions: `sum`, `count`, `min`, `max`, and `average`. You access these predefined functions in the predicate syntax using custom keywords (for example, `MAX(1, 5, 10)`).

In macOS 10.5 and later, function expressions also support arbitrary method invocations. To implement this extended functionality, use the syntax `FUNCTION(receiver, selectorName, arguments, ...),` as in the following example:

```objc
FUNCTION(@"/Developer/Tools/otest", @"lastPathComponent") => @"otest"
```

All methods must take one or more `id` arguments and return an `id` value, although you can use the `CAST` expression to convert datatypes with lossy string representations (for example, `CAST(####, "NSDate")`). macOS 10.5 extends the `CAST` expression to provide support for casting to classes for use in creating receivers for function expressions.

Although Core Data supports evaluation of the predefined functions, it doesn’t support the evaluation of custom predicate functions in the persistent stores (during a fetch).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating an Expression

- [- initWithExpressionType:](<nsexpression/init(expressiontype_).md>) — Creates the expression with the specified expression type.
- [+ expressionWithFormat:argumentArray:](<nsexpression/init(format_argumentarray_).md>) — Creates the expression with the specified expression format and array of arguments.
- [+ expressionWithFormat:arguments:](<nsexpression/init(format_arguments_).md>) — Creates the expression with the specified expression format and arguments list.
- [init(format:_:)](<nsexpression/init(format___).md>) — Creates the expression with the expression format and arguments list you specify.
- [- initWithCoder:](<nsexpression/init(coder_).md>) — Creates an expression by decoding from the coder you specify.

### Creating an Expression for a Value

- [+ expressionForConstantValue:](<nsexpression/init(forconstantvalue_).md>) — Creates an expression that represents a specified constant value.
- [+ expressionForEvaluatedObject](<nsexpression/expressionforevaluatedobject().md>) — Creates an expression that represents the object you’re evaluating.
- [+ expressionForKeyPath:](<nsexpression/init(forkeypath_)-1aqf5.md>) — Creates an expression that invokes the value function with a specified key path.
- [+ expressionForVariable:](<nsexpression/init(forvariable_).md>) — Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [init(forKeyPath:)](<nsexpression/init(forkeypath_)-98by.md>) — Creates an expression using a key path you specify.
- [+ expressionForAnyKey](<nsexpression/expressionforanykey().md>) — Creates an expression that represents any key for a Spotlight query.

### Creating a Collection Expression

- [+ expressionForAggregate:](<nsexpression/init(foraggregate_).md>) — Creates an aggregate expression for a specified collection.
- [+ expressionForUnionSet:with:](<nsexpression/init(forunionset_with_).md>) — Creates an expression object that represents the union of a specified set and collection.
- [+ expressionForIntersectSet:with:](<nsexpression/init(forintersectset_with_).md>) — Creates an expression object that represents the intersection of a specified set and collection.
- [+ expressionForMinusSet:with:](<nsexpression/init(forminusset_with_).md>) — Creates an expression object that represents the subtraction of a specified collection from a specified set.

### Creating a Subquery

- [+ expressionForSubquery:usingIteratorVariable:predicate:](<nsexpression/init(forsubquery_usingiteratorvariable_predicate_).md>) — Creates an expression that filters a collection by storing elements in the collection in a specified variable and keeping the elements that the qualifier returns as true.

### Creating a Conditional Expression

- [+ expressionForConditional:trueExpression:falseExpression:](<nsexpression/init(forconditional_trueexpression_falseexpression_).md>) — Creates an expression that returns a result, depending on the value of predicate.

### Creating an Expression Using Blocks

- [+ expressionForBlock:arguments:](<nsexpression/init(block_arguments_).md>) — Creates an expression object that uses the block for evaluating objects.

### Creating an Expression for a Function

- [+ expressionForFunction:arguments:](<nsexpression/init(forfunction_arguments_).md>) — Creates an expression that invokes one of the predefined functions.
- [+ expressionForFunction:selectorName:arguments:](<nsexpression/init(forfunction_selectorname_arguments_).md>) — Creates an expression that returns the result of invoking a selector with a specified name using specified arguments.

### Getting Information About an Expression

- [arguments](nsexpression/arguments.md) — The arguments for the expression.
- [collection](nsexpression/collection.md) — The collection of expressions in an aggregate expression, or the collection element of a subquery expression.
- [constantValue](nsexpression/constantvalue.md) — The constant value of the expression.
- [expressionType](nsexpression/expressiontype-swift.property.md) — The expression type for the expression.
- [ExpressionType](nsexpression/expressiontype-swift.enum.md) — Defines the possible types of an expression.
- [function](nsexpression/function.md) — The function for the expression.
- [keyPath](nsexpression/keypath.md) — The key path for the expression.
- [operand](nsexpression/operand.md) — The operand for the expression.
- [predicate](nsexpression/predicate.md) — The predicate of a subquery expression.
- [leftExpression](nsexpression/left.md) — The left expression of an aggregate expression.
- [rightExpression](nsexpression/right.md) — The right expression of an aggregate expression.
- [variable](nsexpression/variable.md) — The variable for the expression.

### Evaluating an Expression

- [- expressionValueWithObject:context:](<nsexpression/expressionvalue(with_context_).md>) — Evaluates an expression using a specified object and context.
- [- allowEvaluation](<nsexpression/allowevaluation().md>) — Forces a securely decoded expression to allow evaluation.
- [falseExpression](nsexpression/false.md) — An expression to evalutate if a conditional expression’s predicate evaluates to false.
- [trueExpression](nsexpression/true.md) — An expression to evalutate if a conditional expression’s predicate evaluates to true.

### Accessing the Expression Block

- [expressionBlock](nsexpression/expressionblock.md) — The block that executes to evaluate the expression.

### Initializers

- [init(_:)](<nsexpression/init(__).md>)
- [init(forBlock:arguments:)](<nsexpression/init(forblock_arguments_).md>)

## See Also

### Filltering

- [Predicate](predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [PredicateError](predicateerror.md) — An error thrown while evaluating a predicate.
- [PredicateCodableConfiguration](predicatecodableconfiguration.md) — A specification of the expected types and key paths found in an archived predicate.
- [PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md) — A type that provides the expected key paths found in an archived predicate.
- [PredicateExpression](predicateexpression.md) — A component expression that makes up part of a predicate.
- [StandardPredicateExpression](standardpredicateexpression.md) — A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [PredicateExpressions](predicateexpressions.md) — The expressions that make up a predicate.
- [PredicateBindings](predicatebindings.md) — A mapping from a predicates’s input variables to their values.
- [NSPredicate](nspredicate.md) — A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [NSComparisonPredicate](nscomparisonpredicate.md) — A specialized predicate for comparing expressions.
- [NSCompoundPredicate](nscompoundpredicate.md) — A specialized predicate that evaluates logical combinations of other predicates.
