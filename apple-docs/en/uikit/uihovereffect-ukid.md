---
title: UIHoverEffect
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihovereffect-ukid
source_url: 'https://developer.apple.com/documentation/uikit/uihovereffect-ukid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovereffect-ukid.json'
content_hash: 'sha256:563c1bdb28683390'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIHoverEffect

<sub>Protocol</sub>

A hover effect that can apply to a view through a hover style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UIHoverEffect <NSObject, NSCopying>
```

## Overview

You don’t conform to this protocol directly. Instead, you use a built-in [UIHoverEffect](uihovereffect-40091.md) like [UIHoverAutomaticEffect](uihoverautomaticeffect-swift.struct.md).

## Relationships

- **Inherits From**: [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIHoverAutomaticEffect](uihoverautomaticeffect-c.class.md), [UIHoverHighlightEffect](uihoverhighlighteffect-c.class.md), [UIHoverLiftEffect](uihoverlifteffect-c.class.md), [UIPointerEffect](uipointereffect-c.class.md)

## See Also

### Specifying a hover effect

- [effect](uihoverstyle/effect-12r83.md) — The effect to apply to the view with this style.
- [UIHoverAutomaticEffect](uihoverautomaticeffect-c.class.md) — A system-default hover effect that automatically selects the appropriate effect based on the view to which it applies.
- [UIHoverHighlightEffect](uihoverhighlighteffect-c.class.md) — An effect that applies a highlight to the view on hover.
- [UIHoverLiftEffect](uihoverlifteffect-c.class.md) — An effect that can visually lift the view on hover where appropriate.
