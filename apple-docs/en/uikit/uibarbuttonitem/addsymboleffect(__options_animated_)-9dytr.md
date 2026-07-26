---
title: 'addSymbolEffect(_:options:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/addsymboleffect(_:options:animated:)-9dytr'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/addsymboleffect(_:options:animated:)-9dytr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/addsymboleffect%28_%3Aoptions%3Aanimated%3A%29-9dytr.json'
content_hash: 'sha256:91b66c92f3503053'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# addSymbolEffect(_:options:animated:)

<sub>Instance Method</sub>

Adds a discrete symbol effect to the bar button item with the specified options and animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func addSymbolEffect(_ effect: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default, animated: Bool = true)
```

## Parameters

- `effect` — The symbol effect to add.

- `options` — The options for the symbol effect.

- `animated` — A Boolean value that indicates whether to animate the addition of a scale, appear, or disappear effect.

## See Also

### Configuring symbol effects

- [symbolAnimationEnabled](issymbolanimationenabled.md) — A Boolean value that indicates whether symbol effects animate.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-3iew0.md>) — Adds an indefinite symbol effect to the bar button item with the specified options and animation.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-6jx3e.md>) — Adds a discrete, indefinite symbol effect to the bar button item with the specified options and animation.
- [setSymbolImage(_:contentTransition:options:)](<setsymbolimage(__contenttransition_options_).md>) — Sets a symbol image using the specified content-transition effect and options.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-214pl.md>) — Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-7m567.md>) — Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-8zc4d.md>) — Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [removeAllSymbolEffects(options:animated:)](<removeallsymboleffects(options_animated_).md>) — Removes all symbol effects from the bar button item, using the specified options and animation setting.
