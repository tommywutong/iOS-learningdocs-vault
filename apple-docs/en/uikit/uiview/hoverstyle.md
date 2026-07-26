---
title: hoverStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/hoverstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiview/hoverstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/hoverstyle.json'
content_hash: 'sha256:e0609d431f8df593'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# hoverStyle

<sub>Instance Property</sub>

The hover style for the view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var hoverStyle: UIHoverStyle? { get set }
```

## Discussion

The value of this property defaults to `nil`, which indicates that the view doesn’t have any hover effect. Subclasses can configure this style to use a different default value.

## See Also

### Managing the hover appearance

- [UIHoverStyle](../uihoverstyle.md) — The hover style to apply to a view, including an effect and a shape to use for displaying that effect.
- [UIHoverEffectLayer](../uihovereffectlayer.md) — A layer type that can be used to apply a hover effect to its sublayers.
