---
title: hoverStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihovereffectlayer/hoverstyle
source_url: 'https://developer.apple.com/documentation/uikit/uihovereffectlayer/hoverstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovereffectlayer/hoverstyle.json'
content_hash: 'sha256:c85c8dd2e9e9d88c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIHoverEffectLayer](../uihovereffectlayer.md)

# hoverStyle

<sub>Instance Property</sub>

The hover style to apply to the sublayers of this layer when this layer is hovered (e.g., when the user looks at this layer). Defaults to the automatic style.

<sub>visionOS</sub>

```swift
@NSCopying var hoverStyle: UIHoverStyle { get set }
```

## Discussion

> [!note] Note
> Not all [UIHoverStyle](../uihoverstyle.md)s may be supported by [UIHoverEffectLayer](../uihovereffectlayer.md). If the provided style is not supported, a fallback style will be selected instead.
