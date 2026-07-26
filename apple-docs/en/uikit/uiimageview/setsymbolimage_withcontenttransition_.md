---
title: 'setSymbolImage:withContentTransition:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimageview/setsymbolimage:withcontenttransition:'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/setsymbolimage:withcontenttransition:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/setsymbolimage%3Awithcontenttransition%3A.json'
content_hash: 'sha256:38b5435f60cc4070'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# setSymbolImage:withContentTransition:

<sub>Instance Method</sub>

Sets a symbol image using the specified content-transition effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) setSymbolImage:(UIImage *) symbolImage withContentTransition:(NSSymbolContentTransition *) transition;
```

## Parameters

- `symbolImage` — The symbol image to set.

- `transition` — The content transition to use when setting the symbol image.

## See Also

### Configuring symbol effects

- [addSymbolEffect:](addsymboleffect_.md) — Adds a symbol effect to the image view with default options and animation.
- [addSymbolEffect:options:](addsymboleffect_options_.md) — Adds a symbol effect to the image view with the specified options and default animation.
- [addSymbolEffect:options:animated:](addsymboleffect_options_animated_.md) — Adds a symbol effect to the image view with the specified options and animation.
- [addSymbolEffect:options:animated:completion:](addsymboleffect_options_animated_completion_.md) — Adds a symbol effect to the image view with the specified options, animation, and completion handler.
- [setSymbolImage:withContentTransition:options:](setsymbolimage_withcontenttransition_options_.md) — Sets a symbol image using the specified content-transition effect and options.
- [setSymbolImage:withContentTransition:options:completion:](setsymbolimage_withcontenttransition_options_completion_.md) — Sets a symbol image using the specified content-transition effect, options, and completion handler.
- [removeSymbolEffectOfType:](removesymboleffectoftype_.md) — Removes the symbol effect that matches the specified effect type.
- [removeSymbolEffectOfType:options:](removesymboleffectoftype_options_.md) — Removes the symbol effect that matches the specified effect type, using the specified options.
- [removeSymbolEffectOfType:options:animated:](removesymboleffectoftype_options_animated_.md) — Removes the symbol effect that matches the specified effect type, using the specified options and animation setting.
- [removeSymbolEffectOfType:options:animated:completion:](removesymboleffectoftype_options_animated_completion_.md) — Removes the symbol effect that matches the specified effect type, using the specified options, animation setting, and completion handler.
- [removeAllSymbolEffects](removeallsymboleffects.md) — Removes all symbol effects from the image view.
- [removeAllSymbolEffectsWithOptions:](removeallsymboleffectswithoptions_.md) — Removes all symbol effects from the image view, using the specified options.
- [removeAllSymbolEffectsWithOptions:animated:](removeallsymboleffectswithoptions_animated_.md) — Removes all symbol effects from the image view, using the specified options and animation setting.
- [UISymbolEffectCompletion](../uisymboleffectcompletion-6rxwa.md) — A completion handler for adding and removing symbol effects and transitions.
- [UISymbolEffectCompletionContext](../uisymboleffectcompletioncontext-c.class.md) — Information about a symbol effect’s addition or removal.
