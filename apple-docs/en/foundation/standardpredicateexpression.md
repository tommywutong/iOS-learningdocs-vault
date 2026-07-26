---
title: StandardPredicateExpression
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/standardpredicateexpression
source_url: 'https://developer.apple.com/documentation/foundation/standardpredicateexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/standardpredicateexpression.json'
content_hash: 'sha256:3ac765908a65c1c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# StandardPredicateExpression

<sub>Protocol</sub>

A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol StandardPredicateExpression<Output> : PredicateExpression, Decodable, Encodable, Sendable
```

## Overview

Don’t declare new types that conform to the `StandardPredicateExpression` protocol.  Only the types provided by Foundation are valid conforming types.

## Relationships

- **Inherits From**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [PredicateExpression](predicateexpression.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [Arithmetic](predicateexpressions/arithmetic.md), [ClosedRange](predicateexpressions/closedrange.md), [CollectionContainsCollection](predicateexpressions/collectioncontainscollection.md), [CollectionIndexSubscript](predicateexpressions/collectionindexsubscript.md), [CollectionRangeSubscript](predicateexpressions/collectionrangesubscript.md), [Comparison](predicateexpressions/comparison.md), [Conditional](predicateexpressions/conditional.md), [ConditionalCast](predicateexpressions/conditionalcast.md), [Conjunction](predicateexpressions/conjunction.md), [DictionaryKeyDefaultValueSubscript](predicateexpressions/dictionarykeydefaultvaluesubscript.md), [DictionaryKeySubscript](predicateexpressions/dictionarykeysubscript.md), [Disjunction](predicateexpressions/disjunction.md), [Equal](predicateexpressions/equal.md), [ExpressionEvaluate](predicateexpressions/expressionevaluate.md), [Filter](predicateexpressions/filter.md), [FloatDivision](predicateexpressions/floatdivision.md), [ForceCast](predicateexpressions/forcecast.md), [ForcedUnwrap](predicateexpressions/forcedunwrap.md), [IntDivision](predicateexpressions/intdivision.md), [IntRemainder](predicateexpressions/intremainder.md), [KeyPath](predicateexpressions/keypath.md), [Negation](predicateexpressions/negation.md), [NilCoalesce](predicateexpressions/nilcoalesce.md), [NilLiteral](predicateexpressions/nilliteral.md), [NotEqual](predicateexpressions/notequal.md), [OptionalFlatMap](predicateexpressions/optionalflatmap.md), [PredicateEvaluate](predicateexpressions/predicateevaluate.md), [Range](predicateexpressions/range.md), [RangeExpressionContains](predicateexpressions/rangeexpressioncontains.md), [SequenceAllSatisfy](predicateexpressions/sequenceallsatisfy.md), [SequenceContains](predicateexpressions/sequencecontains.md), [SequenceContainsWhere](predicateexpressions/sequencecontainswhere.md), [SequenceMaximum](predicateexpressions/sequencemaximum.md), [SequenceMinimum](predicateexpressions/sequenceminimum.md), [SequenceStartsWith](predicateexpressions/sequencestartswith.md), [StringCaseInsensitiveCompare](predicateexpressions/stringcaseinsensitivecompare.md), [StringContainsRegex](predicateexpressions/stringcontainsregex.md), [StringLocalizedCompare](predicateexpressions/stringlocalizedcompare.md), [StringLocalizedStandardContains](predicateexpressions/stringlocalizedstandardcontains.md), [TypeCheck](predicateexpressions/typecheck.md), [UnaryMinus](predicateexpressions/unaryminus.md), [Value](predicateexpressions/value.md), [Variable](predicateexpressions/variable.md)

## See Also

### Filltering

- [Predicate](predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [PredicateError](predicateerror.md) — An error thrown while evaluating a predicate.
- [PredicateCodableConfiguration](predicatecodableconfiguration.md) — A specification of the expected types and key paths found in an archived predicate.
- [PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md) — A type that provides the expected key paths found in an archived predicate.
- [PredicateExpression](predicateexpression.md) — A component expression that makes up part of a predicate.
- [PredicateExpressions](predicateexpressions.md) — The expressions that make up a predicate.
- [PredicateBindings](predicatebindings.md) — A mapping from a predicates’s input variables to their values.
- [NSPredicate](nspredicate.md) — A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [NSExpression](nsexpression.md) — An expression for use in a comparison predicate.
- [NSComparisonPredicate](nscomparisonpredicate.md) — A specialized predicate for comparing expressions.
- [NSCompoundPredicate](nscompoundpredicate.md) — A specialized predicate that evaluates logical combinations of other predicates.
