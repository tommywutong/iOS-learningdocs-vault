---
title: 'initWithMorphology:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsinflectionruleexplicit/initwithmorphology:'
source_url: 'https://developer.apple.com/documentation/foundation/nsinflectionruleexplicit/initwithmorphology:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinflectionruleexplicit/initwithmorphology%3A.json'
content_hash: 'sha256:d6f40e07de6ca73c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInflectionRuleExplicit](../nsinflectionruleexplicit.md)

# initWithMorphology:

<sub>Instance Method</sub>

Creates an inflection rule with the given morphology.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithMorphology:(NSMorphology *) morphology;
```

## Parameters

- `morphology` — The morphology this rule applies when inflecting.

## Return Value

An inflection rule that uses the given morphology.

## See Also

### Creating an Explicit Inflection Rule

- [NSMorphology](../nsmorphology.md) — A description of the grammatical properties of a string.
