---
title: EmptyVisualEffect
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/emptyvisualeffect
source_url: 'https://developer.apple.com/documentation/swiftui/emptyvisualeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/emptyvisualeffect.json'
content_hash: 'sha256:a931c1a30141b404'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EmptyVisualEffect

<sub>Structure</sub>

The base visual effect that you apply additional effect to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EmptyVisualEffect
```

## Overview

`EmptyVisualEffect` does not change the appearance of the view that it is applied to.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [VisualEffect](visualeffect.md)

## Topics

### Creating an empty visual effect

- [init()](<emptyvisualeffect/init().md>) — Creates a new empty visual effect.

## See Also

### Applying effects based on geometry

- [visualEffect(_:)](<view/visualeffect(__).md>) — Applies effects to this view, while providing access to layout information through a geometry proxy.
- [visualEffect3D(_:)](<view/visualeffect3d(__).md>) — Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [VisualEffect](visualeffect.md) — Visual Effects change the visual appearance of a view without changing its ancestors or descendents.
