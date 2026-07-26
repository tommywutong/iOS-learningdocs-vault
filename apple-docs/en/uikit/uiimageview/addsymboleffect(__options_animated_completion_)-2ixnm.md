---
title: 'addSymbolEffect(_:options:animated:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimageview/addsymboleffect(_:options:animated:completion:)-2ixnm'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/addsymboleffect(_:options:animated:completion:)-2ixnm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/addsymboleffect%28_%3Aoptions%3Aanimated%3Acompletion%3A%29-2ixnm.json'
content_hash: 'sha256:ed8a765d6276242f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# addSymbolEffect(_:options:animated:completion:)

<sub>Instance Method</sub>

Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func addSymbolEffect(_ effect: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default, animated: Bool = true, completion: UISymbolEffectCompletion? = nil)
```

## Parameters

- `effect` — The symbol effect to add.

- `options` — The options for the symbol effect.

- `animated` — A Boolean value that indicates whether to animate the addition of a scale, appear, or disappear effect.

- `completion` — A completion handler the system calls after the effect’s addition is complete.

## See Also

### Configuring symbol effects

- [addSymbolEffect(_:options:animated:completion:)](<addsymboleffect(__options_animated_completion_)-18jqj.md>) — Adds a discrete symbol effect to the image view with the specified options and animation.
- [addSymbolEffect(_:options:animated:completion:)](<addsymboleffect(__options_animated_completion_)-896qd.md>) — Adds an indefinite symbol effect to the image view with the specified options and animation.
- [setSymbolImage(_:contentTransition:options:completion:)](<setsymbolimage(__contenttransition_options_completion_).md>) — Sets a symbol image using the specified content-transition effect, options, and completion handler.
- [removeSymbolEffect(ofType:options:animated:completion:)](<removesymboleffect(oftype_options_animated_completion_)-218lh.md>) — Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:completion:)](<removesymboleffect(oftype_options_animated_completion_)-31zec.md>) — Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:completion:)](<removesymboleffect(oftype_options_animated_completion_)-2boi2.md>) — Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [removeAllSymbolEffects(options:animated:)](<removeallsymboleffects(options_animated_).md>) — Removes all symbol effects from the image view, using the specified options and animation setting.
- [UISymbolEffectCompletion](../uisymboleffectcompletion-7qt7g.md) — A completion handler for adding and removing symbol effects and transitions.
- [UISymbolEffectCompletionContext](../uisymboleffectcompletioncontext-swift.struct.md) — Information about a symbol effect’s addition or removal.
