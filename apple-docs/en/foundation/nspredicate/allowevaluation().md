---
title: allowEvaluation()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspredicate/allowevaluation()
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/allowevaluation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/allowevaluation%28%29.json'
content_hash: 'sha256:2420269b72f44882'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# allowEvaluation()

<sub>Instance Method</sub>

Forces a securely decoded predicate to allow evaluation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func allowEvaluation()
```

## Discussion

When securely decoding [NSPredicate](../nspredicate.md) objects that are encoded using [NSSecureCoding](../nssecurecoding.md), evaluation is disabled because it is potentially unsafe to evaluate predicates you get out of an archive.

Before you enable evaluation, you should validate key paths, selectors, and other details to ensure no erroneous or malicious code will be executed. Once you’ve verified the predicate, you can enable the receiver for evaluation by calling [- allowEvaluation](<allowevaluation().md>).

## See Also

### Evaluating a Predicate

- [- evaluateWithObject:](<evaluate(with_).md>) — Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies.
- [- evaluateWithObject:substitutionVariables:](<evaluate(with_substitutionvariables_).md>) — Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies after substituting in the values from a specified variables dictionary.
