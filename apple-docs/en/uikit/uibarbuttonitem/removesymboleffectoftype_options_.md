---
title: 'removeSymbolEffectOfType:options:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/removesymboleffectoftype:options:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/removesymboleffectoftype:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/removesymboleffectoftype%3Aoptions%3A.json'
content_hash: 'sha256:e881e7cdd0d6267e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# removeSymbolEffectOfType:options:

<sub>Instance Method</sub>

Removes the symbol effect that matches the specified effect type, using the specified options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) removeSymbolEffectOfType:(NSSymbolEffect *) symbolEffect options:(NSSymbolEffectOptions *) options;
```

## Parameters

- `symbolEffect` — The symbol effect to match for removal.

- `options` — The options to use when removing the symbol effect.

## See Also

### Configuring symbol effects

- [symbolAnimationEnabled](issymbolanimationenabled.md) — A Boolean value that indicates whether symbol effects animate.
- [addSymbolEffect:](addsymboleffect_.md) — Adds a symbol effect to the bar button item with default options and animation.
- [addSymbolEffect:options:](addsymboleffect_options_.md) — Adds a symbol effect to the bar button item with the specified options and default animation.
- [addSymbolEffect:options:animated:](addsymboleffect_options_animated_.md) — Adds a symbol effect to the bar button item with the specified options and animation.
- [setSymbolImage:withContentTransition:](setsymbolimage_withcontenttransition_.md) — Sets a symbol image using the specified content-transition effect.
- [setSymbolImage:withContentTransition:options:](setsymbolimage_withcontenttransition_options_.md) — Sets a symbol image using the specified content-transition effect and options.
- [removeSymbolEffectOfType:](removesymboleffectoftype_.md) — Removes the symbol effect that matches the specified effect type.
- [removeSymbolEffectOfType:options:animated:](removesymboleffectoftype_options_animated_.md) — Removes the symbol effect that matches the specified effect type, using the specified options and animation setting.
- [removeAllSymbolEffects](removeallsymboleffects.md) — Removes all symbol effects from the bar button item.
- [removeAllSymbolEffectsWithOptions:](removeallsymboleffectswithoptions_.md) — Removes all symbol effects from the bar button item, using the specified options.
- [removeAllSymbolEffectsWithOptions:animated:](removeallsymboleffectswithoptions_animated_.md) — Removes all symbol effects from the bar button item, using the specified options and animation setting.
