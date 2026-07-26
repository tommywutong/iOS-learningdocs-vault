---
title: PredicateExpressions
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions.json'
content_hash: 'sha256:e62cb20efe04a81f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PredicateExpressions

<sub>Enumeration</sub>

The expressions that make up a predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum PredicateExpressions
```

## Overview

Don’t use this type directly.  When you call the `Predicate(_:)` macro in your code, the  expansion of that macro produces these values.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md)

## Topics

### Structures

- [Arithmetic](predicateexpressions/arithmetic.md)
- [ClosedRange](predicateexpressions/closedrange.md)
- [CollectionContainsCollection](predicateexpressions/collectioncontainscollection.md)
- [CollectionIndexSubscript](predicateexpressions/collectionindexsubscript.md)
- [CollectionRangeSubscript](predicateexpressions/collectionrangesubscript.md)
- [Comparison](predicateexpressions/comparison.md)
- [Conditional](predicateexpressions/conditional.md)
- [ConditionalCast](predicateexpressions/conditionalcast.md)
- [Conjunction](predicateexpressions/conjunction.md)
- [DictionaryKeyDefaultValueSubscript](predicateexpressions/dictionarykeydefaultvaluesubscript.md)
- [DictionaryKeySubscript](predicateexpressions/dictionarykeysubscript.md)
- [Disjunction](predicateexpressions/disjunction.md)
- [Equal](predicateexpressions/equal.md)
- [ExpressionEvaluate](predicateexpressions/expressionevaluate.md)
- [Filter](predicateexpressions/filter.md)
- [FloatDivision](predicateexpressions/floatdivision.md)
- [ForceCast](predicateexpressions/forcecast.md)
- [ForcedUnwrap](predicateexpressions/forcedunwrap.md)
- [IntDivision](predicateexpressions/intdivision.md)
- [IntRemainder](predicateexpressions/intremainder.md)
- [KeyPath](predicateexpressions/keypath.md)
- [Negation](predicateexpressions/negation.md)
- [NilCoalesce](predicateexpressions/nilcoalesce.md)
- [NilLiteral](predicateexpressions/nilliteral.md)
- [NotEqual](predicateexpressions/notequal.md)
- [OptionalFlatMap](predicateexpressions/optionalflatmap.md)
- [PredicateEvaluate](predicateexpressions/predicateevaluate.md)
- [PredicateRegex](predicateexpressions/predicateregex.md)
- [Range](predicateexpressions/range.md)
- [RangeExpressionContains](predicateexpressions/rangeexpressioncontains.md)
- [SequenceAllSatisfy](predicateexpressions/sequenceallsatisfy.md)
- [SequenceContains](predicateexpressions/sequencecontains.md)
- [SequenceContainsWhere](predicateexpressions/sequencecontainswhere.md)
- [SequenceMaximum](predicateexpressions/sequencemaximum.md)
- [SequenceMinimum](predicateexpressions/sequenceminimum.md)
- [SequenceStartsWith](predicateexpressions/sequencestartswith.md)
- [StringCaseInsensitiveCompare](predicateexpressions/stringcaseinsensitivecompare.md)
- [StringContainsRegex](predicateexpressions/stringcontainsregex.md)
- [StringLocalizedCompare](predicateexpressions/stringlocalizedcompare.md)
- [StringLocalizedStandardContains](predicateexpressions/stringlocalizedstandardcontains.md)
- [TypeCheck](predicateexpressions/typecheck.md)
- [UnaryMinus](predicateexpressions/unaryminus.md)
- [Value](predicateexpressions/value.md)
- [Variable](predicateexpressions/variable.md)
- [VariableID](predicateexpressions/variableid.md)

### Type Methods

- [build_Arg(_:)](<predicateexpressions/build_arg(__)-2e8wt.md>)
- [build_Arg(_:)](<predicateexpressions/build_arg(__)-4nz6o.md>)
- [build_Arg(_:)](<predicateexpressions/build_arg(__)-8jd6q.md>)
- [build_Arithmetic(lhs:rhs:op:)](<predicateexpressions/build_arithmetic(lhs_rhs_op_).md>)
- [build_ClosedRange(lower:upper:)](<predicateexpressions/build_closedrange(lower_upper_).md>)
- [build_Comparison(lhs:rhs:op:)](<predicateexpressions/build_comparison(lhs_rhs_op_).md>)
- [build_Conditional(_:_:_:)](<predicateexpressions/build_conditional(______).md>)
- [build_Conjunction(lhs:rhs:)](<predicateexpressions/build_conjunction(lhs_rhs_).md>)
- [build_Disjunction(lhs:rhs:)](<predicateexpressions/build_disjunction(lhs_rhs_).md>)
- [build_Division(lhs:rhs:)](<predicateexpressions/build_division(lhs_rhs_)-5mg1h.md>)
- [build_Division(lhs:rhs:)](<predicateexpressions/build_division(lhs_rhs_)-958g1.md>)
- [build_Equal(lhs:rhs:)](<predicateexpressions/build_equal(lhs_rhs_).md>)
- [build_ForcedUnwrap(_:)](<predicateexpressions/build_forcedunwrap(__).md>)
- [build_KeyPath(root:keyPath:)](<predicateexpressions/build_keypath(root_keypath_).md>)
- [build_Negation(_:)](<predicateexpressions/build_negation(__).md>)
- [build_NilCoalesce(lhs:rhs:)](<predicateexpressions/build_nilcoalesce(lhs_rhs_).md>)
- [build_NilLiteral()](<predicateexpressions/build_nilliteral().md>)
- [build_NotEqual(lhs:rhs:)](<predicateexpressions/build_notequal(lhs_rhs_).md>)
- [build_Range(lower:upper:)](<predicateexpressions/build_range(lower_upper_).md>)
- [build_Remainder(lhs:rhs:)](<predicateexpressions/build_remainder(lhs_rhs_).md>)
- [build_UnaryMinus(_:)](<predicateexpressions/build_unaryminus(__).md>)
- [build_allSatisfy(_:_:)](<predicateexpressions/build_allsatisfy(____).md>)
- [build_caseInsensitiveCompare(_:_:)](<predicateexpressions/build_caseinsensitivecompare(____).md>)
- [build_contains(_:_:)](<predicateexpressions/build_contains(____)-18oc3.md>)
- [build_contains(_:_:)](<predicateexpressions/build_contains(____)-9bwzx.md>)
- [build_contains(_:_:)](<predicateexpressions/build_contains(____)-9ferb.md>)
- [build_contains(_:_:)](<predicateexpressions/build_contains(____)-9ulrw.md>)
- [build_contains(_:where:)](<predicateexpressions/build_contains(__where_).md>)
- [build_evaluate(_:_:)](<predicateexpressions/build_evaluate(____)-33oeu.md>)
- [build_evaluate(_:_:)](<predicateexpressions/build_evaluate(____)-6h1h.md>)
- [build_filter(_:_:)](<predicateexpressions/build_filter(____).md>)
- [build_flatMap(_:_:)](<predicateexpressions/build_flatmap(____)-7d3x7.md>)
- [build_flatMap(_:_:)](<predicateexpressions/build_flatmap(____)-kcbs.md>)
- [build_localizedCompare(_:_:)](<predicateexpressions/build_localizedcompare(____).md>)
- [build_localizedStandardContains(_:_:)](<predicateexpressions/build_localizedstandardcontains(____).md>)
- [build_max(_:)](<predicateexpressions/build_max(__).md>)
- [build_min(_:)](<predicateexpressions/build_min(__).md>)
- [build_starts(_:with:)](<predicateexpressions/build_starts(__with_).md>)
- [build_subscript(_:_:)](<predicateexpressions/build_subscript(____)-61z8t.md>)
- [build_subscript(_:_:)](<predicateexpressions/build_subscript(____)-8f5bl.md>)
- [build_subscript(_:_:)](<predicateexpressions/build_subscript(____)-are7.md>)
- [build_subscript(_:_:default:)](<predicateexpressions/build_subscript(____default_).md>)

### Enumerations

- [ArithmeticOperator](predicateexpressions/arithmeticoperator.md)
- [ComparisonOperator](predicateexpressions/comparisonoperator.md)

## See Also

### Filltering

- [Predicate](predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [PredicateError](predicateerror.md) — An error thrown while evaluating a predicate.
- [PredicateCodableConfiguration](predicatecodableconfiguration.md) — A specification of the expected types and key paths found in an archived predicate.
- [PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md) — A type that provides the expected key paths found in an archived predicate.
- [PredicateExpression](predicateexpression.md) — A component expression that makes up part of a predicate.
- [StandardPredicateExpression](standardpredicateexpression.md) — A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [PredicateBindings](predicatebindings.md) — A mapping from a predicates’s input variables to their values.
- [NSPredicate](nspredicate.md) — A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [NSExpression](nsexpression.md) — An expression for use in a comparison predicate.
- [NSComparisonPredicate](nscomparisonpredicate.md) — A specialized predicate for comparing expressions.
- [NSCompoundPredicate](nscompoundpredicate.md) — A specialized predicate that evaluates logical combinations of other predicates.
