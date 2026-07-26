---
title: sender
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisymboleffectcompletioncontext-c.class/sender
source_url: 'https://developer.apple.com/documentation/uikit/uisymboleffectcompletioncontext-c.class/sender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisymboleffectcompletioncontext-c.class/sender.json'
content_hash: 'sha256:15ab6750c6e7ef9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISymbolEffectCompletionContext](../uisymboleffectcompletioncontext-c.class.md)

# sender

<sub>Instance Property</sub>

The object, an image view or bar button item, that received the symbol effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, weak, readonly, nullable) id sender;
```

## See Also

### Determining completion status

- [contentTransition](contenttransition.md) — The symbol content transition that completed.
- [effect](effect.md) — The symbol effect that completed.
- [finished](finished.md) — A Boolean value that indicates whether the symbol effect finished completely.
