---
title: UIHoverEffectLayer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihovereffectlayer
source_url: 'https://developer.apple.com/documentation/uikit/uihovereffectlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovereffectlayer.json'
content_hash: 'sha256:df1a2cbd7613ee1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIHoverEffectLayer

<sub>Class</sub>

A layer type that can be used to apply a hover effect to its sublayers.

<sub>visionOS</sub>

```swift
@MainActor class UIHoverEffectLayer
```

## Overview

This layer type is useful for adding hover effects to an existing `CALayer` hierarchy. Where possible, use `UIView.hoverStyle` instead.

A [UIHoverEffectLayer](uihovereffectlayer.md) is configured with:

1. A container [UIView](uiview.md), which is used to infer some properties of the hover effect from its trait collection and to allow some aspects of the hover effect to behave correctly. This view’s layer should be an ancestor layer of the [UIHoverEffectLayer](uihovereffectlayer.md).
2. A [UIHoverStyle](uihoverstyle.md), which describes the effect to use and the shape of that effect. You then add your content layers that should receive a hover effect as sublayers of this layer.

[UIHoverEffectLayer](uihovereffectlayer.md) may add its own internal sublayers as background or overlay layers relative to your content sublayers. To preserve the correct appearance of the effect, these internal sublayers are automatically sorted accordingly within the layer’s layout pass. As such, do not assume that the indices of your content sublayers will remain stable throughout the lifetime of the layer.

> [!note] Note
> Not all [UIHoverStyle](uihoverstyle.md)s may be supported by [UIHoverEffectLayer](uihovereffectlayer.md). If the provided style is not supported, a fallback style will be selected instead.

## Relationships

- **Inherits From**: [CALayer](../quartzcore/calayer.md)

- **Conforms To**: [CAMediaTiming](../quartzcore/camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [- initWithContainerView:style:](<uihovereffectlayer/init(containerview_style_).md>) — Creates a [UIHoverEffectLayer](uihovereffectlayer.md) with the provided `containerView` and `style`. If a `nil` `style` is provided, the automatic style will be used instead.

### Instance Properties

- [containerView](uihovereffectlayer/containerview.md) — The [UIView](uiview.md) in which this layer is contained. This view is used to derive traits and other properties for applying the correct hover effect to the layer. It may also be used to assist with applying some kinds of hover effects to the layer.
- [hoverStyle](uihovereffectlayer/hoverstyle.md) — The hover style to apply to the sublayers of this layer when this layer is hovered (e.g., when the user looks at this layer). Defaults to the automatic style.

## See Also

### Managing the hover appearance

- [hoverStyle](uiview/hoverstyle.md) — The hover style for the view.
- [UIHoverStyle](uihoverstyle.md) — The hover style to apply to a view, including an effect and a shape to use for displaying that effect.
