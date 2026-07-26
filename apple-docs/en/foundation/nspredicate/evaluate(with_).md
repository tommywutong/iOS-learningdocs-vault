---
title: 'evaluate(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/evaluate(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/evaluate(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/evaluate%28with%3A%29.json'
content_hash: 'sha256:f23f6c09aceeaf76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# evaluate(with:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func evaluate(with object: Any?) -> Bool
```

## Parameters

- `object` — The object against which to evaluate the predicate.

## Return Value

[true](../../swift/true.md) if `object` matches the conditions specified by the predicate, otherwise [false](../../swift/false.md).

## See Also

### Evaluating a Predicate

- [- evaluateWithObject:substitutionVariables:](<evaluate(with_substitutionvariables_).md>) — Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies after substituting in the values from a specified variables dictionary.
- [- allowEvaluation](<allowevaluation().md>) — Forces a securely decoded predicate to allow evaluation.
