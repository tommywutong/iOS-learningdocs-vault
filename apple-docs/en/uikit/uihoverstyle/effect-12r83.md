---
title: effect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihoverstyle/effect-12r83
source_url: 'https://developer.apple.com/documentation/uikit/uihoverstyle/effect-12r83'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihoverstyle/effect-12r83.json'
content_hash: 'sha256:d73e258b0df10b46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIHoverStyle](../uihoverstyle.md)

# effect

<sub>Instance Property</sub>

The effect to apply to the view with this style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, strong) id<UIHoverEffect> effect;
```

## Discussion

Use [UIHoverAutomaticEffect](../uihoverautomaticeffect-swift.struct.md) to apply a system-default effect to the view.

## See Also

### Specifying a hover effect

- [UIHoverAutomaticEffect](../uihoverautomaticeffect-c.class.md) — A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [UIHoverHighlightEffect](../uihoverhighlighteffect-c.class.md) — An effect that applies a highlight to the view on hover.
- [UIHoverLiftEffect](../uihoverlifteffect-c.class.md) — An effect that can visually lift the view on hover where appropriate.
- [UIHoverEffect](../uihovereffect-ukid.md) — A hover effect that can apply to a view through a hover style.
