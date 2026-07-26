---
title: PredicateExpression
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpression
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpression.json'
content_hash: 'sha256:6e14b950209d1480'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PredicateExpression

<sub>Protocol</sub>

A component expression that makes up part of a predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PredicateExpression<Output>
```

## Overview

To transform a predicate, define a protocol for the result and add conformance on each predicate expression type that you support. For example:

```swift
protocol ProsePredicateExpression {
    func proseQuery() -> String
}

// Repeated for each supported operator.
extension PredicateExpressions.Equal: ProsePredicateExpression 
        where LHS: ProsePredicateExpression,
        RHS: ProsePredicateExpression {
    func proseQuery() -> String {
        return lhs.proseQuery() + " is equal to " + rhs.proseQuery()
    }
}

extension Predicate  {
    func proseQuery() -> String? {
        guard let expression = expression as? ProsePredicateExpression else { return nil }
        return expression.proseQuery()
    }
}
```

## Relationships

- **Inherited By**: [StandardPredicateExpression](standardpredicateexpression.md)

- **Conforming Types**: [Arithmetic](predicateexpressions/arithmetic.md), [ClosedRange](predicateexpressions/closedrange.md), [CollectionContainsCollection](predicateexpressions/collectioncontainscollection.md), [CollectionIndexSubscript](predicateexpressions/collectionindexsubscript.md), [CollectionRangeSubscript](predicateexpressions/collectionrangesubscript.md), [Comparison](predicateexpressions/comparison.md), [Conditional](predicateexpressions/conditional.md), [ConditionalCast](predicateexpressions/conditionalcast.md), [Conjunction](predicateexpressions/conjunction.md), [DictionaryKeyDefaultValueSubscript](predicateexpressions/dictionarykeydefaultvaluesubscript.md), [DictionaryKeySubscript](predicateexpressions/dictionarykeysubscript.md), [Disjunction](predicateexpressions/disjunction.md), [Equal](predicateexpressions/equal.md), [ExpressionEvaluate](predicateexpressions/expressionevaluate.md), [Filter](predicateexpressions/filter.md), [FloatDivision](predicateexpressions/floatdivision.md), [ForceCast](predicateexpressions/forcecast.md), [ForcedUnwrap](predicateexpressions/forcedunwrap.md), [IntDivision](predicateexpressions/intdivision.md), [IntRemainder](predicateexpressions/intremainder.md), [KeyPath](predicateexpressions/keypath.md), [Negation](predicateexpressions/negation.md), [NilCoalesce](predicateexpressions/nilcoalesce.md), [NilLiteral](predicateexpressions/nilliteral.md), [NotEqual](predicateexpressions/notequal.md), [OptionalFlatMap](predicateexpressions/optionalflatmap.md), [PredicateEvaluate](predicateexpressions/predicateevaluate.md), [Range](predicateexpressions/range.md), [RangeExpressionContains](predicateexpressions/rangeexpressioncontains.md), [SequenceAllSatisfy](predicateexpressions/sequenceallsatisfy.md), [SequenceContains](predicateexpressions/sequencecontains.md), [SequenceContainsWhere](predicateexpressions/sequencecontainswhere.md), [SequenceMaximum](predicateexpressions/sequencemaximum.md), [SequenceMinimum](predicateexpressions/sequenceminimum.md), [SequenceStartsWith](predicateexpressions/sequencestartswith.md), [StringCaseInsensitiveCompare](predicateexpressions/stringcaseinsensitivecompare.md), [StringContainsRegex](predicateexpressions/stringcontainsregex.md), [StringLocalizedCompare](predicateexpressions/stringlocalizedcompare.md), [StringLocalizedStandardContains](predicateexpressions/stringlocalizedstandardcontains.md), [TypeCheck](predicateexpressions/typecheck.md), [UnaryMinus](predicateexpressions/unaryminus.md), [Value](predicateexpressions/value.md), [Variable](predicateexpressions/variable.md)

## Topics

### Evaluating a predicate expression

- [Output](predicateexpression/output.md)
- [evaluate(_:)](<predicateexpression/evaluate(__).md>)

## See Also

### Filltering

- [Predicate](predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [PredicateError](predicateerror.md) — An error thrown while evaluating a predicate.
- [PredicateCodableConfiguration](predicatecodableconfiguration.md) — A specification of the expected types and key paths found in an archived predicate.
- [PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md) — A type that provides the expected key paths found in an archived predicate.
- [StandardPredicateExpression](standardpredicateexpression.md) — A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [PredicateExpressions](predicateexpressions.md) — The expressions that make up a predicate.
- [PredicateBindings](predicatebindings.md) — A mapping from a predicates’s input variables to their values.
- [NSPredicate](nspredicate.md) — A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [NSExpression](nsexpression.md) — An expression for use in a comparison predicate.
- [NSComparisonPredicate](nscomparisonpredicate.md) — A specialized predicate for comparing expressions.
- [NSCompoundPredicate](nscompoundpredicate.md) — A specialized predicate that evaluates logical combinations of other predicates.
