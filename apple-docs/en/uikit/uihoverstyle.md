---
title: UIHoverStyle
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihoverstyle
source_url: 'https://developer.apple.com/documentation/uikit/uihoverstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihoverstyle.json'
content_hash: 'sha256:e6e0ebaf24da4f5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIHoverStyle

<sub>Class</sub>

The hover style to apply to a view, including an effect and a shape to use for displaying that effect.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIHoverStyle
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIPointerStyle](uipointerstyle.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a hover style

- [init(effect:shape:)](<uihoverstyle/init(effect_shape_).md>) — Creates a hover style with the provided effect and shape.
- [init(shape:)](<uihoverstyle/init(shape_).md>) — Creates a hover style with the provided shape and an automatic hover effect.

### Specifying a hover shape

- [shape](uihoverstyle/shape-21npk.md) — The shape to use for the hover effect.
- [UIShape](uishape-swift.struct.md) — An abstract representation of a shape.

### Specifying a hover effect

- [effect](uihoverstyle/effect-4vdoj.md) — The effect to apply to the view with this style.
- [UIHoverAutomaticEffect](uihoverautomaticeffect-swift.struct.md) — A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [UIHoverHighlightEffect](uihoverhighlighteffect-swift.struct.md) — An effect that applies a highlight to the view on hover.
- [UIHoverLiftEffect](uihoverlifteffect-swift.struct.md) — An effect that can visually lift the view on hover where appropriate.
- [UIHoverEffect](uihovereffect-40091.md) — A hover effect that can apply to a view through a hover style.

### Managing the state of the hover effect

- [enabled](uihoverstyle/isenabled.md) — A Boolean value that determines whether the hover effect is active.

## See Also

### Managing the hover appearance

- [hoverStyle](uiview/hoverstyle.md) — The hover style for the view.
- [UIHoverEffectLayer](uihovereffectlayer.md) — A layer type that can be used to apply a hover effect to its sublayers.
