---
title: effect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihoverstyle/effect-4vdoj
source_url: 'https://developer.apple.com/documentation/uikit/uihoverstyle/effect-4vdoj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihoverstyle/effect-4vdoj.json'
content_hash: 'sha256:e2c414f47999df43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIHoverStyle](../uihoverstyle.md)

# effect

<sub>Instance Property</sub>

The effect to apply to the view with this style.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency var effect: any UIHoverEffect { get set }
```

## Discussion

Use [UIHoverAutomaticEffect](../uihoverautomaticeffect-swift.struct.md) to apply a system-default effect to the view.

## See Also

### Specifying a hover effect

- [UIHoverAutomaticEffect](../uihoverautomaticeffect-swift.struct.md) — A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [UIHoverHighlightEffect](../uihoverhighlighteffect-swift.struct.md) — An effect that applies a highlight to the view on hover.
- [UIHoverLiftEffect](../uihoverlifteffect-swift.struct.md) — An effect that can visually lift the view on hover where appropriate.
- [UIHoverEffect](../uihovereffect-40091.md) — A hover effect that can apply to a view through a hover style.
