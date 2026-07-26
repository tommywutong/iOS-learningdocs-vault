---
title: 'removeAllSymbolEffects(options:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/removeallsymboleffects(options:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/removeallsymboleffects(options:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/removeallsymboleffects%28options%3Aanimated%3A%29.json'
content_hash: 'sha256:094277ea0d279bbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# removeAllSymbolEffects(options:animated:)

<sub>Instance Method</sub>

Removes all symbol effects from the bar button item, using the specified options and animation setting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func removeAllSymbolEffects(options: SymbolEffectOptions = .default, animated: Bool = true)
```

## Parameters

- `options` — The options to use when removing the symbol effects.

- `animated` — A Boolean value that indicates whether to animate the removal of a scale, appear, or disappear effects.

## See Also

### Configuring symbol effects

- [symbolAnimationEnabled](issymbolanimationenabled.md) — A Boolean value that indicates whether symbol effects animate.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-3iew0.md>) — Adds an indefinite symbol effect to the bar button item with the specified options and animation.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-6jx3e.md>) — Adds a discrete, indefinite symbol effect to the bar button item with the specified options and animation.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-9dytr.md>) — Adds a discrete symbol effect to the bar button item with the specified options and animation.
- [setSymbolImage(_:contentTransition:options:)](<setsymbolimage(__contenttransition_options_).md>) — Sets a symbol image using the specified content-transition effect and options.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-214pl.md>) — Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-7m567.md>) — Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-8zc4d.md>) — Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
