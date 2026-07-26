---
title: 'setSymbolImage(_:contentTransition:options:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimageview/setsymbolimage(_:contenttransition:options:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/setsymbolimage(_:contenttransition:options:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/setsymbolimage%28_%3Acontenttransition%3Aoptions%3Acompletion%3A%29.json'
content_hash: 'sha256:4cedbff9ffcf99de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# setSymbolImage(_:contentTransition:options:completion:)

<sub>Instance Method</sub>

Sets a symbol image using the specified content-transition effect, options, and completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func setSymbolImage(_ image: UIImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default, completion: UISymbolEffectCompletion? = nil)
```

## Parameters

- `image` — The symbol image to set.

- `contentTransition` — The content transition to use when setting the symbol image.

- `options` — The options to use when setting the symbol image.

- `completion` — A completion handler the system calls after setting the symbol image.

## See Also

### Configuring symbol effects

- [addSymbolEffect(_:options:animated:completion:)](<addsymboleffect(__options_animated_completion_)-18jqj.md>) — Adds a discrete symbol effect to the image view with the specified options and animation.
- [addSymbolEffect(_:options:animated:completion:)](<addsymboleffect(__options_animated_completion_)-2ixnm.md>) — Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [addSymbolEffect(_:options:animated:completion:)](<addsymboleffect(__options_animated_completion_)-896qd.md>) — Adds an indefinite symbol effect to the image view with the specified options and animation.
- [removeSymbolEffect(ofType:options:animated:completion:)](<removesymboleffect(oftype_options_animated_completion_)-218lh.md>) — Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:completion:)](<removesymboleffect(oftype_options_animated_completion_)-31zec.md>) — Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:completion:)](<removesymboleffect(oftype_options_animated_completion_)-2boi2.md>) — Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [removeAllSymbolEffects(options:animated:)](<removeallsymboleffects(options_animated_).md>) — Removes all symbol effects from the image view, using the specified options and animation setting.
- [UISymbolEffectCompletion](../uisymboleffectcompletion-7qt7g.md) — A completion handler for adding and removing symbol effects and transitions.
- [UISymbolEffectCompletionContext](../uisymboleffectcompletioncontext-swift.struct.md) — Information about a symbol effect’s addition or removal.
