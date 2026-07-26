---
title: effect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisymboleffectcompletioncontext-swift.struct/effect
source_url: 'https://developer.apple.com/documentation/uikit/uisymboleffectcompletioncontext-swift.struct/effect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisymboleffectcompletioncontext-swift.struct/effect.json'
content_hash: 'sha256:d051f3fe783f4120'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISymbolEffectCompletionContext](../uisymboleffectcompletioncontext-swift.struct.md)

# effect

<sub>Instance Property</sub>

The symbol effect that completed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor var effect: any SymbolEffect { get }
```

## Discussion

For a symbol effect completion, this property may not be the same instance as the original effect.

For a content transition completion, this property is `nil.`

## See Also

### Determining completion status

- [isFinished](isfinished.md) — A Boolean value that indicates whether the symbol effect finished completely.
- [sender](sender.md) — The object, an image view or bar button item, that received the symbol effect.
