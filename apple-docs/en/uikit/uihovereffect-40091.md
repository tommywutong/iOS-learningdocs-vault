---
title: UIHoverEffect
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihovereffect-40091
source_url: 'https://developer.apple.com/documentation/uikit/uihovereffect-40091'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovereffect-40091.json'
content_hash: 'sha256:09fe5ab0406f4106'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIHoverEffect

<sub>Protocol</sub>

A hover effect that can apply to a view through a hover style.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol UIHoverEffect
```

## Overview

You don’t conform to this protocol directly. Instead, you use a built-in [UIHoverEffect](uihovereffect-40091.md) like [UIHoverAutomaticEffect](uihoverautomaticeffect-swift.struct.md).

## Relationships

- **Conforming Types**: [UIHoverAutomaticEffect](uihoverautomaticeffect-swift.struct.md), [UIHoverHighlightEffect](uihoverhighlighteffect-swift.struct.md), [UIHoverLiftEffect](uihoverlifteffect-swift.struct.md), [UIPointerEffect](uipointereffect-swift.enum.md)

## Topics

### Choosing a hover effect

- [automatic](uihovereffect-40091/automatic.md) — A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [highlight](uihovereffect-40091/highlight.md) — An effect that applies a highlight to the view on hover.
- [lift](uihovereffect-40091/lift.md) — An effect that can visually lift the view on hover where appropriate.

## See Also

### Specifying a hover effect

- [effect](uihoverstyle/effect-4vdoj.md) — The effect to apply to the view with this style.
- [UIHoverAutomaticEffect](uihoverautomaticeffect-swift.struct.md) — A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [UIHoverHighlightEffect](uihoverhighlighteffect-swift.struct.md) — An effect that applies a highlight to the view on hover.
- [UIHoverLiftEffect](uihoverlifteffect-swift.struct.md) — An effect that can visually lift the view on hover where appropriate.
