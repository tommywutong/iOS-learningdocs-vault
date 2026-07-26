---
title: PredicateBindings
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicatebindings
source_url: 'https://developer.apple.com/documentation/foundation/predicatebindings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicatebindings.json'
content_hash: 'sha256:0bdbd251ed88cd19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PredicateBindings

<sub>Structure</sub>

A mapping from a predicates’s input variables to their values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PredicateBindings
```

## Overview

If you define a custom predicate expression type, you must propagate the predicate’s bindings to its subexpressions.

If you define a custom predicate type, you must create an instance of this structure, populate it with the predicate’s variables, and propagate it throughout the expression tree.

## Topics

### Initializers

- [init(_:)](<predicatebindings/init(__).md>)

### Instance Methods

- [binding(_:to:)](<predicatebindings/binding(__to_).md>)

### Subscripts

- [subscript(_:)](<predicatebindings/subscript(__).md>)

## See Also

### Filltering

- [Predicate](predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [PredicateError](predicateerror.md) — An error thrown while evaluating a predicate.
- [PredicateCodableConfiguration](predicatecodableconfiguration.md) — A specification of the expected types and key paths found in an archived predicate.
- [PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md) — A type that provides the expected key paths found in an archived predicate.
- [PredicateExpression](predicateexpression.md) — A component expression that makes up part of a predicate.
- [StandardPredicateExpression](standardpredicateexpression.md) — A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [PredicateExpressions](predicateexpressions.md) — The expressions that make up a predicate.
- [NSPredicate](nspredicate.md) — A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [NSExpression](nsexpression.md) — An expression for use in a comparison predicate.
- [NSComparisonPredicate](nscomparisonpredicate.md) — A specialized predicate for comparing expressions.
- [NSCompoundPredicate](nscompoundpredicate.md) — A specialized predicate that evaluates logical combinations of other predicates.
