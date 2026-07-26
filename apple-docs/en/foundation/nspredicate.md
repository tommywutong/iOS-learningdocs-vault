---
title: NSPredicate
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspredicate
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate.json'
content_hash: 'sha256:173f4efdccf58f5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPredicate

<sub>Class</sub>

A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPredicate
```

## Overview

Predicates represent logical conditions, which you can use to filter collections of objects. Although it’s common to create predicates directly from instances of [NSComparisonPredicate](nscomparisonpredicate.md), [NSCompoundPredicate](nscompoundpredicate.md), and [NSExpression](nsexpression.md), you often create predicates from a format string that the class methods parse on [NSPredicate](nspredicate.md). Examples of predicate format strings include:

- Simple comparisons, such as `grade == "7"` or `firstName like "Juan"`
- Case- and diacritic-insensitive lookups, such as `name contains[cd] "stein"`
- Logical operations, such as `(firstName like "Mei") OR (lastName like "Chen")`
- Temporal range constraints, such as `date between {$YESTERDAY, $TOMORROW}`
- Relational conditions, such as `group.name like "work*"`
- Aggregate operations, such as `@sum.items.price < 1000`

For a complete syntax reference, refer to the [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789).

You can also create predicates that include variables using the [- evaluateWithObject:substitutionVariables:](<nspredicate/evaluate(with_substitutionvariables_).md>) method so that you can predefine the predicate before substituting concrete values at runtime.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSComparisonPredicate](nscomparisonpredicate.md), [NSCompoundPredicate](nscompoundpredicate.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating a Predicate

- [+ predicateWithFormat:argumentArray:](<nspredicate/init(format_argumentarray_).md>) — Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [+ predicateWithFormat:arguments:](<nspredicate/init(format_arguments_).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(format:_:)](<nspredicate/init(format___).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(_:)](<nspredicate/init(__).md>) — Creates a predicate by converting an existing predicate.
- [- predicateWithSubstitutionVariables:](<nspredicate/withsubstitutionvariables(__).md>) — Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [+ predicateWithValue:](<nspredicate/init(value_).md>) — Creates and returns a predicate that always evaluates to a specified Boolean value.
- [+ predicateWithBlock:](<nspredicate/init(block_).md>) — Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [+ predicateFromMetadataQueryString:](<nspredicate/init(frommetadataquerystring_).md>) — Creates a predicate with a metadata query string.

### Evaluating a Predicate

- [- evaluateWithObject:](<nspredicate/evaluate(with_).md>) — Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies.
- [- evaluateWithObject:substitutionVariables:](<nspredicate/evaluate(with_substitutionvariables_).md>) — Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies after substituting in the values from a specified variables dictionary.
- [- allowEvaluation](<nspredicate/allowevaluation().md>) — Forces a securely decoded predicate to allow evaluation.

### Getting a String Representation

- [predicateFormat](nspredicate/predicateformat.md) — The predicate’s format string.

### Initializers

- [init(coder:)](<nspredicate/init(coder_).md>)

### Instance Methods

- [- allowEvaluationWithValidator:error:](<nspredicate/allowevaluation(validator_).md>)

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
- [NSExpression](nsexpression.md) — An expression for use in a comparison predicate.
- [NSComparisonPredicate](nscomparisonpredicate.md) — A specialized predicate for comparing expressions.
- [NSCompoundPredicate](nscompoundpredicate.md) — A specialized predicate that evaluates logical combinations of other predicates.
