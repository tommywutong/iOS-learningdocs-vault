---
title: UISymbolEffectCompletion
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisymboleffectcompletion-7qt7g
source_url: 'https://developer.apple.com/documentation/uikit/uisymboleffectcompletion-7qt7g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisymboleffectcompletion-7qt7g.json'
content_hash: 'sha256:fe303297be7007b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISymbolEffectCompletion

<sub>Type Alias</sub>

A completion handler for adding and removing symbol effects and transitions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias UISymbolEffectCompletion = (UISymbolEffectCompletionContext) -> Void
```

## See Also

### Configuring symbol effects

- [addSymbolEffect(_:options:animated:completion:)](<uiimageview/addsymboleffect(__options_animated_completion_)-18jqj.md>) — Adds a discrete symbol effect to the image view with the specified options and animation.
- [addSymbolEffect(_:options:animated:completion:)](<uiimageview/addsymboleffect(__options_animated_completion_)-2ixnm.md>) — Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [addSymbolEffect(_:options:animated:completion:)](<uiimageview/addsymboleffect(__options_animated_completion_)-896qd.md>) — Adds an indefinite symbol effect to the image view with the specified options and animation.
- [setSymbolImage(_:contentTransition:options:completion:)](<uiimageview/setsymbolimage(__contenttransition_options_completion_).md>) — Sets a symbol image using the specified content-transition effect, options, and completion handler.
- [removeSymbolEffect(ofType:options:animated:completion:)](<uiimageview/removesymboleffect(oftype_options_animated_completion_)-218lh.md>) — Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:completion:)](<uiimageview/removesymboleffect(oftype_options_animated_completion_)-31zec.md>) — Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:completion:)](<uiimageview/removesymboleffect(oftype_options_animated_completion_)-2boi2.md>) — Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [removeAllSymbolEffects(options:animated:)](<uiimageview/removeallsymboleffects(options_animated_).md>) — Removes all symbol effects from the image view, using the specified options and animation setting.
- [UISymbolEffectCompletionContext](uisymboleffectcompletioncontext-swift.struct.md) — Information about a symbol effect’s addition or removal.
