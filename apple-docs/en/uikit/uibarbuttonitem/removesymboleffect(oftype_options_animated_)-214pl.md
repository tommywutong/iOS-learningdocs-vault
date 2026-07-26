---
title: 'removeSymbolEffect(ofType:options:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/removesymboleffect(oftype:options:animated:)-214pl'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/removesymboleffect(oftype:options:animated:)-214pl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/removesymboleffect%28oftype%3Aoptions%3Aanimated%3A%29-214pl.json'
content_hash: 'sha256:6f23d2a826baac73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# removeSymbolEffect(ofType:options:animated:)

<sub>Instance Method</sub>

Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func removeSymbolEffect(ofType effect: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default, animated: Bool = true)
```

## Parameters

- `effect` — The symbol effect to match for removal.

- `options` — The options to use when removing the symbol effect.

- `animated` — A Boolean value that indicates whether to animate the removal of a scale, appear, or disappear effect.

## See Also

### Configuring symbol effects

- [symbolAnimationEnabled](issymbolanimationenabled.md) — A Boolean value that indicates whether symbol effects animate.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-3iew0.md>) — Adds an indefinite symbol effect to the bar button item with the specified options and animation.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-6jx3e.md>) — Adds a discrete, indefinite symbol effect to the bar button item with the specified options and animation.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-9dytr.md>) — Adds a discrete symbol effect to the bar button item with the specified options and animation.
- [setSymbolImage(_:contentTransition:options:)](<setsymbolimage(__contenttransition_options_).md>) — Sets a symbol image using the specified content-transition effect and options.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-7m567.md>) — Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-8zc4d.md>) — Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [removeAllSymbolEffects(options:animated:)](<removeallsymboleffects(options_animated_).md>) — Removes all symbol effects from the bar button item, using the specified options and animation setting.
