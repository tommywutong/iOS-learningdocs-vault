---
title: 'setSymbolImage(_:contentTransition:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/setsymbolimage(_:contenttransition:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/setsymbolimage(_:contenttransition:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/setsymbolimage%28_%3Acontenttransition%3Aoptions%3A%29.json'
content_hash: 'sha256:b09560348e95f10c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# setSymbolImage(_:contentTransition:options:)

<sub>Instance Method</sub>

Sets a symbol image using the specified content-transition effect and options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func setSymbolImage(_ image: UIImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default)
```

## Parameters

- `image` — The symbol image to set.

- `contentTransition` — The content transition to use when setting the symbol image.

- `options` — The options to use when setting the symbol image.

## See Also

### Configuring symbol effects

- [symbolAnimationEnabled](issymbolanimationenabled.md) — A Boolean value that indicates whether symbol effects animate.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-3iew0.md>) — Adds an indefinite symbol effect to the bar button item with the specified options and animation.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-6jx3e.md>) — Adds a discrete, indefinite symbol effect to the bar button item with the specified options and animation.
- [addSymbolEffect(_:options:animated:)](<addsymboleffect(__options_animated_)-9dytr.md>) — Adds a discrete symbol effect to the bar button item with the specified options and animation.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-214pl.md>) — Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-7m567.md>) — Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:)](<removesymboleffect(oftype_options_animated_)-8zc4d.md>) — Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [removeAllSymbolEffects(options:animated:)](<removeallsymboleffects(options_animated_).md>) — Removes all symbol effects from the bar button item, using the specified options and animation setting.
