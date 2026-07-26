---
title: UIFocusHaloEffect
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocushaloeffect
source_url: 'https://developer.apple.com/documentation/uikit/uifocushaloeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocushaloeffect.json'
content_hash: 'sha256:e40db6409b6f817d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusHaloEffect

<sub>Class</sub>

A visual focus effect that draws a halo around the focus item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIFocusHaloEffect
```

## Relationships

- **Inherits From**: [UIFocusEffect](uifocuseffect.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a halo effect

- [+ effectWithRoundedRect:cornerRadius:curve:](<uifocushaloeffect/init(roundedrect_cornerradius_curve_).md>) — Creates a rounded halo effect using the specified corner radius and corner curve.
- [+ effectWithRect:](<uifocushaloeffect/init(rect_).md>) — Creates a rectangular halo effect using the specified rectangle.
- [+ effectWithPath:](<uifocushaloeffect/init(path_).md>) — Creates a halo effect using the specified Bézier path.

### Configuring a halo effect

- [containerView](uifocushaloeffect/containerview.md) — The container view to place the halo effect into.
- [referenceView](uifocushaloeffect/referenceview.md) — The view to place the halo effect above.
- [position](uifocushaloeffect/position-swift.property.md) — The position of the halo effect relative to its shape.
- [Position](uifocushaloeffect/position-swift.enum.md) — Constants that describe positions for drawing the halo focus effect.

## See Also

### Focus effects

- [UIFocusEffect](uifocuseffect.md) — The base class for defining a visual focus effect.
- [Position](uifocushaloeffect/position-swift.enum.md) — Constants that describe positions for drawing the halo focus effect.
