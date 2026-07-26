---
title: 'InflectionRule.explicit(_:)'
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/inflectionrule/explicit(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/inflectionrule/explicit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inflectionrule/explicit%28_%3A%29.json'
content_hash: 'sha256:6a24f6a3688047e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InflectionRule](../inflectionrule.md)

# InflectionRule.explicit(_:)

<sub>Case</sub>

An inflection rule that uses a morphology instance to determine how to inflect attribued strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case explicit(Morphology)
```

## Parameters

- `Morphology` — The [Morphology](../morphology.md) instance to use when applying this rule.

## See Also

### Inflection Rule Behaviors

- [InflectionRule.automatic](automatic.md) — An inflection rule that performs automatic grammar agreement with default transformations.
