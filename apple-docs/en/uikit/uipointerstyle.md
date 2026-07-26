---
title: UIPointerStyle
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerstyle
source_url: 'https://developer.apple.com/documentation/uikit/uipointerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerstyle.json'
content_hash: 'sha256:2745c3e125af78b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerStyle

<sub>Class</sub>

An object that defines the pointer shape and effect.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPointerStyle
```

## Overview

Whenever possible, match pointer styles to UIKit styles and make them consistent with the visual intent of similar views.

> [!note] Note
> When supporting the use of Apple Pencil, effect-based styles, such as a pointer style created using [init(effect:shape:)](<uipointerstyle/init(effect_shape_).md>) are fully supported, but shape-based pointer styles created using [init(shape:constrainedAxes:)](<uipointerstyle/init(shape_constrainedaxes_).md>) aren’t.

For more information, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices/).

## Relationships

- **Inherits From**: [UIHoverStyle](uihoverstyle.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a pointer style

- [init(effect:shape:)](<uipointerstyle/init(effect_shape_).md>) — Applies the provided content effect and pointer shape to the current region.
- [init(shape:constrainedAxes:)](<uipointerstyle/init(shape_constrainedaxes_).md>) — Morphs the pointer into the provided shape when hovering over the current region.
- [+ hiddenPointerStyle](<uipointerstyle/hidden().md>) — Hides the pointer when it moves over the current region.
- [+ systemPointerStyle](<uipointerstyle/system().md>) — Morphs the pointer into a default system-style pointer.

### Specifying pointer accessories

- [accessories](uipointerstyle/accessories.md) — Accessories to display alongside the pointer.
- [UIPointerAccessory](uipointeraccessory.md) — Constants that describe accessories to display alongside the primary pointer.

## See Also

### Pointer styles

- [UIPointerShape](uipointershape-swift.enum.md) — An object that defines the shape of custom pointers.
- [UIPointerEffect](uipointereffect-swift.enum.md) — An effect that alters a view’s appearance when a pointer enters the current region.
- [UIPointerAccessory](uipointeraccessory.md) — Constants that describe accessories to display alongside the primary pointer.
