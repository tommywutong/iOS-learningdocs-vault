---
title: UIPointerShape
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointershape-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uipointershape-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointershape-swift.enum.json'
content_hash: 'sha256:3aba2f5d797ebb37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerShape

<sub>Enumeration</sub>

An object that defines the shape of custom pointers.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIPointerShape
```

## Overview

If the desired pointer shape can be expressed as a rounded rectangle, use [UIPointerShape.roundedRect(_:radius:)](<uipointershape-swift.enum/roundedrect(__radius_).md>) for best results.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md)

## Topics

### Specifying pointer shapes

- [UIPointerShape.horizontalBeam(length:)](<uipointershape-swift.enum/horizontalbeam(length_).md>) — The pointer morphs into a horizontal beam using the specified length.
- [UIPointerShape.verticalBeam(length:)](<uipointershape-swift.enum/verticalbeam(length_).md>) — The pointer morphs into a vertical beam using the specified length.
- [UIPointerShape.path(_:)](<uipointershape-swift.enum/path(__).md>) — The pointer morphs into the given Bézier path.
- [UIPointerShape.roundedRect(_:radius:)](<uipointershape-swift.enum/roundedrect(__radius_).md>) — The pointer morphs into a rounded rectangle using the provided corner radius.

### Accessing corner radius

- [defaultCornerRadius](uipointershape-swift.enum/defaultcornerradius.md) — The default corner radius for a pointer using a rounded rectangle.

## See Also

### Pointer styles

- [UIPointerStyle](uipointerstyle.md) — An object that defines the pointer shape and effect.
- [UIPointerEffect](uipointereffect-swift.enum.md) — An effect that alters a view’s appearance when a pointer enters the current region.
- [UIPointerAccessory](uipointeraccessory.md) — Constants that describe accessories to display alongside the primary pointer.
