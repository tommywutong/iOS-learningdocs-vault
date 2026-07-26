---
title: UIPointerHoverEffect
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerhovereffect
source_url: 'https://developer.apple.com/documentation/uikit/uipointerhovereffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerhovereffect.json'
content_hash: 'sha256:151cf9b29ac07782'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerHoverEffect

<sub>Class</sub>

An effect where visual changes apply to the view and the pointer retains its default shape.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIPointerHoverEffect : UIPointerEffect
```

## Overview

Use the properties of [UIPointerHoverEffect](uipointerhovereffect.md) to define the visual changes to apply to the view.

## Relationships

- **Inherits From**: [UIPointerEffect](uipointereffect-c.class.md)

## Topics

### Specifying the tint mode

- [preferredTintMode](uipointerhovereffect/preferredtintmode.md) — The preferred tint mode for the effect.
- [UIPointerEffectTintMode](uipointereffecttintmode.md) — An effect that defines how to apply a tint to a view during a pointer interaction.

### Customizing the effect

- [prefersShadow](uipointerhovereffect/prefersshadow.md) — A Boolean value that determines whether to add a shadow.
- [prefersScaledContent](uipointerhovereffect/prefersscaledcontent.md) — A Boolean value that determines whether to scale the content.

## See Also

### Creating a specific effect

- [UIPointerHighlightEffect](uipointerhighlighteffect.md) — An effect where the pointer slides under the given view and morphs into the view’s shape.
- [UIPointerLiftEffect](uipointerlifteffect.md) — An effect where the pointer slides under the given view and disappears as the view scales up and gains a shadow.
