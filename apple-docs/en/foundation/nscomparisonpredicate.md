---
title: NSComparisonPredicate
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonpredicate
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate.json'
content_hash: 'sha256:c40ce4cc5ac18ecf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSComparisonPredicate

<sub>Class</sub>

A specialized predicate for comparing expressions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSComparisonPredicate
```

## Overview

Use comparison predicates to compare the results of two expressions. You create a comparison predicate with an operator, a left expression, and a right expression, and use instances of the [NSExpression](nsexpression.md) class to represent those expressions. When you evaluate the predicate, it returns a `BOOL` value as the result of invoking the operator with the results of evaluating the expressions.

## Relationships

- **Inherits From**: [NSPredicate](nspredicate.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Comparison Predicates

- [Displaying searchable content by using a search controller](../uikit/displaying-searchable-content-by-using-a-search-controller.md) — Create a user interface with searchable content in a table view.
- [- initWithLeftExpression:rightExpression:customSelector:](<nscomparisonpredicate/init(leftexpression_rightexpression_customselector_).md>) — Creates a predicate that you form by combining specified left and right expressions using a specified selector.
- [- initWithLeftExpression:rightExpression:modifier:type:options:](<nscomparisonpredicate/init(leftexpression_rightexpression_modifier_type_options_).md>) — Creates a predicate to a specified type that you form by combining specified left and right expressions using a specified modifier and options.
- [- initWithCoder:](<nscomparisonpredicate/init(coder_).md>) — Creates a predicate by decoding from the coder you specify.

### Getting Information About a Comparison Predicate

- [comparisonPredicateModifier](nscomparisonpredicate/comparisonpredicatemodifier.md) — The comparison predicate modifier for the receiver.
- [Modifier](nscomparisonpredicate/modifier.md) — Constants that describe the possible types of modifier for a comparison predicate.
- [customSelector](nscomparisonpredicate/customselector.md) — The selector for the receiver.
- [rightExpression](nscomparisonpredicate/rightexpression.md) — The right expression for the receiver.
- [leftExpression](nscomparisonpredicate/leftexpression.md) — The left expression for the receiver.
- [options](nscomparisonpredicate/options-swift.property.md) — The options to use for the receiver.
- [Options](nscomparisonpredicate/options-swift.struct.md) — Constants that describe the possible types of string comparison for comparison predicates.
- [predicateOperatorType](nscomparisonpredicate/predicateoperatortype.md) — The predicate type for the receiver.
- [Operator](nscomparisonpredicate/operator.md) — Defines the type of comparison for a comparison predicate.

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
- [NSExpression](nsexpression.md) — An expression for use in a comparison predicate.
- [NSCompoundPredicate](nscompoundpredicate.md) — A specialized predicate that evaluates logical combinations of other predicates.
