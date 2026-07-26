---
title: contentTransition
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisymboleffectcompletioncontext-c.class/contenttransition
source_url: 'https://developer.apple.com/documentation/uikit/uisymboleffectcompletioncontext-c.class/contenttransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisymboleffectcompletioncontext-c.class/contenttransition.json'
content_hash: 'sha256:7530b5ed4825452f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISymbolEffectCompletionContext](../uisymboleffectcompletioncontext-c.class.md)

# contentTransition

<sub>Instance Property</sub>

The symbol content transition that completed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly, nullable) NSSymbolContentTransition * contentTransition;
```

## Discussion

For a content transition completion, this property may not be the same instance as the original content transition.

For a symbol effect completion, this property is `nil.`

## See Also

### Determining completion status

- [effect](effect.md) — The symbol effect that completed.
- [finished](finished.md) — A Boolean value that indicates whether the symbol effect finished completely.
- [sender](sender.md) — The object, an image view or bar button item, that received the symbol effect.
