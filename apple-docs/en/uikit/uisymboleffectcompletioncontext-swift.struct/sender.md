---
title: sender
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisymboleffectcompletioncontext-swift.struct/sender
source_url: 'https://developer.apple.com/documentation/uikit/uisymboleffectcompletioncontext-swift.struct/sender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisymboleffectcompletioncontext-swift.struct/sender.json'
content_hash: 'sha256:61d5877c5645448e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISymbolEffectCompletionContext](../uisymboleffectcompletioncontext-swift.struct.md)

# sender

<sub>Instance Property</sub>

The object, an image view or bar button item, that received the symbol effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor weak var sender: AnyObject? { get }
```

## See Also

### Determining completion status

- [effect](effect.md) — The symbol effect that completed.
- [isFinished](isfinished.md) — A Boolean value that indicates whether the symbol effect finished completely.
