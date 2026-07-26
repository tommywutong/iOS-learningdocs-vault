---
title: 'evaluate(with:substitutionVariables:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/evaluate(with:substitutionvariables:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/evaluate(with:substitutionvariables:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/evaluate%28with%3Asubstitutionvariables%3A%29.json'
content_hash: 'sha256:a48830d712d9ddce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# evaluate(with:substitutionVariables:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies after substituting in the values from a specified variables dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func evaluate(with object: Any?, substitutionVariables bindings: [String : Any]?) -> Bool
```

## Parameters

- `object` — The object against which to evaluate the predicate.

- `bindings` — The substitution variables dictionary. The dictionary must contain key-value pairs for all variables in the predicate.

## Return Value

[true](../../swift/true.md) if `object` matches the conditions specified by the predicate after substituting in the values in `bindings` for any replacement tokens, otherwise [false](../../swift/false.md).

## Discussion

This method returns the same result as the two step process of first invoking [- predicateWithSubstitutionVariables:](<withsubstitutionvariables(__).md>) on the predicate and then invoking [- evaluateWithObject:](<evaluate(with_).md>) on the returned value. This method is optimized for situations which require repeatedly evaluating a predicate with substitution variables with different variable substitutions.

## See Also

### Evaluating a Predicate

- [- evaluateWithObject:](<evaluate(with_).md>) — Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies.
- [- allowEvaluation](<allowevaluation().md>) — Forces a securely decoded predicate to allow evaluation.
