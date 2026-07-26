---
title: UISymbolEffectCompletionContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisymboleffectcompletioncontext-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uisymboleffectcompletioncontext-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisymboleffectcompletioncontext-c.class.json'
content_hash: 'sha256:e99afc9374acce3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISymbolEffectCompletionContext

<sub>Class</sub>

Information about a symbol effect’s addition or removal.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UISymbolEffectCompletionContext : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Determining completion status

- [contentTransition](uisymboleffectcompletioncontext-c.class/contenttransition.md) — The symbol content transition that completed.
- [effect](uisymboleffectcompletioncontext-c.class/effect.md) — The symbol effect that completed.
- [finished](uisymboleffectcompletioncontext-c.class/finished.md) — A Boolean value that indicates whether the symbol effect finished completely.
- [sender](uisymboleffectcompletioncontext-c.class/sender.md) — The object, an image view or bar button item, that received the symbol effect.

## See Also

### Configuring symbol effects

- [addSymbolEffect:](uiimageview/addsymboleffect_.md) — Adds a symbol effect to the image view with default options and animation.
- [addSymbolEffect:options:](uiimageview/addsymboleffect_options_.md) — Adds a symbol effect to the image view with the specified options and default animation.
- [addSymbolEffect:options:animated:](uiimageview/addsymboleffect_options_animated_.md) — Adds a symbol effect to the image view with the specified options and animation.
- [addSymbolEffect:options:animated:completion:](uiimageview/addsymboleffect_options_animated_completion_.md) — Adds a symbol effect to the image view with the specified options, animation, and completion handler.
- [setSymbolImage:withContentTransition:](uiimageview/setsymbolimage_withcontenttransition_.md) — Sets a symbol image using the specified content-transition effect.
- [setSymbolImage:withContentTransition:options:](uiimageview/setsymbolimage_withcontenttransition_options_.md) — Sets a symbol image using the specified content-transition effect and options.
- [setSymbolImage:withContentTransition:options:completion:](uiimageview/setsymbolimage_withcontenttransition_options_completion_.md) — Sets a symbol image using the specified content-transition effect, options, and completion handler.
- [removeSymbolEffectOfType:](uiimageview/removesymboleffectoftype_.md) — Removes the symbol effect that matches the specified effect type.
- [removeSymbolEffectOfType:options:](uiimageview/removesymboleffectoftype_options_.md) — Removes the symbol effect that matches the specified effect type, using the specified options.
- [removeSymbolEffectOfType:options:animated:](uiimageview/removesymboleffectoftype_options_animated_.md) — Removes the symbol effect that matches the specified effect type, using the specified options and animation setting.
- [removeSymbolEffectOfType:options:animated:completion:](uiimageview/removesymboleffectoftype_options_animated_completion_.md) — Removes the symbol effect that matches the specified effect type, using the specified options, animation setting, and completion handler.
- [removeAllSymbolEffects](uiimageview/removeallsymboleffects.md) — Removes all symbol effects from the image view.
- [removeAllSymbolEffectsWithOptions:](uiimageview/removeallsymboleffectswithoptions_.md) — Removes all symbol effects from the image view, using the specified options.
- [removeAllSymbolEffectsWithOptions:animated:](uiimageview/removeallsymboleffectswithoptions_animated_.md) — Removes all symbol effects from the image view, using the specified options and animation setting.
- [UISymbolEffectCompletion](uisymboleffectcompletion-6rxwa.md) — A completion handler for adding and removing symbol effects and transitions.
