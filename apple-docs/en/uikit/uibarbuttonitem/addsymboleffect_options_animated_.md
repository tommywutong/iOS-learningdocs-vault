---
title: 'addSymbolEffect:options:animated:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/addsymboleffect:options:animated:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/addsymboleffect:options:animated:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/addsymboleffect%3Aoptions%3Aanimated%3A.json'
content_hash: 'sha256:4eaab1d3ae2eb9b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# addSymbolEffect:options:animated:

<sub>Instance Method</sub>

Adds a symbol effect to the bar button item with the specified options and animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) addSymbolEffect:(NSSymbolEffect *) symbolEffect options:(NSSymbolEffectOptions *) options animated:(BOOL) animated;
```

## Parameters

- `symbolEffect` — The symbol effect to add.

- `options` — The options for the symbol effect.

- `animated` — A Boolean value that indicates whether to animate the addition of a scale, appear, or disappear effect.

## See Also

### Configuring symbol effects

- [symbolAnimationEnabled](issymbolanimationenabled.md) — A Boolean value that indicates whether symbol effects animate.
- [addSymbolEffect:](addsymboleffect_.md) — Adds a symbol effect to the bar button item with default options and animation.
- [addSymbolEffect:options:](addsymboleffect_options_.md) — Adds a symbol effect to the bar button item with the specified options and default animation.
- [setSymbolImage:withContentTransition:](setsymbolimage_withcontenttransition_.md) — Sets a symbol image using the specified content-transition effect.
- [setSymbolImage:withContentTransition:options:](setsymbolimage_withcontenttransition_options_.md) — Sets a symbol image using the specified content-transition effect and options.
- [removeSymbolEffectOfType:](removesymboleffectoftype_.md) — Removes the symbol effect that matches the specified effect type.
- [removeSymbolEffectOfType:options:](removesymboleffectoftype_options_.md) — Removes the symbol effect that matches the specified effect type, using the specified options.
- [removeSymbolEffectOfType:options:animated:](removesymboleffectoftype_options_animated_.md) — Removes the symbol effect that matches the specified effect type, using the specified options and animation setting.
- [removeAllSymbolEffects](removeallsymboleffects.md) — Removes all symbol effects from the bar button item.
- [removeAllSymbolEffectsWithOptions:](removeallsymboleffectswithoptions_.md) — Removes all symbol effects from the bar button item, using the specified options.
- [removeAllSymbolEffectsWithOptions:animated:](removeallsymboleffectswithoptions_animated_.md) — Removes all symbol effects from the bar button item, using the specified options and animation setting.
