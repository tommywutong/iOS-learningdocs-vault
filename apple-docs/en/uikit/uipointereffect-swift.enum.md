---
title: UIPointerEffect
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointereffect-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uipointereffect-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointereffect-swift.enum.json'
content_hash: 'sha256:87664130faeb24b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerEffect

<sub>Enumeration</sub>

An effect that alters a view’s appearance when a pointer enters the current region.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIPointerEffect
```

## Overview

`UIPointerEffect` automatically attempts to determine the appropriate effect for the given preview. Use one of its enumeration cases to request a specific system-provided effect.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIHoverEffect](uihovereffect-40091.md)

## Topics

### Accessing the preview

- [preview](uipointereffect-swift.enum/preview.md) — A preview of the view used during an interaction’s animations.

### Creating a default effect

- [UIPointerEffect.automatic(_:)](<uipointereffect-swift.enum/automatic(__).md>) — A pointer content effect with the given preview’s view.

### Creating a specific effect

- [UIPointerEffect.highlight(_:)](<uipointereffect-swift.enum/highlight(__).md>) — An effect where the pointer slides under the given view and morphs into the view’s shape.
- [UIPointerEffect.hover(_:preferredTintMode:prefersShadow:prefersScaledContent:)](<uipointereffect-swift.enum/hover(__preferredtintmode_prefersshadow_prefersscaledcontent_).md>) — An effect where visual changes apply to the view and the pointer retains its default shape.
- [UIPointerEffect.lift(_:)](<uipointereffect-swift.enum/lift(__).md>) — An effect where the pointer slides under the given view and disappears as the view scales up and gains a shadow.

### Enumerations

- [TintMode](uipointereffect-swift.enum/tintmode.md) — An effect that defines how to apply a tint to a view during a pointer interaction.

## See Also

### Pointer styles

- [UIPointerStyle](uipointerstyle.md) — An object that defines the pointer shape and effect.
- [UIPointerShape](uipointershape-swift.enum.md) — An object that defines the shape of custom pointers.
- [UIPointerAccessory](uipointeraccessory.md) — Constants that describe accessories to display alongside the primary pointer.
