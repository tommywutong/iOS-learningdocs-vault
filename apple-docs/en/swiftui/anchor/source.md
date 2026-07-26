---
title: Anchor.Source
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anchor/source
source_url: 'https://developer.apple.com/documentation/swiftui/anchor/source'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anchor/source.json'
content_hash: 'sha256:cc7bb801b70a3880'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Anchor](../anchor.md)

# Anchor.Source

<sub>Structure</sub>

A type-erased geometry value that produces an anchored value of a given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Source
```

## Overview

SwiftUI passes anchored geometry values around the view tree via preference keys. It then converts them back into the local coordinate space using a [GeometryProxy](../geometryproxy.md) value.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting point anchor sources

- [point(_:)](<source/point(__).md>)
- [unitPoint(_:)](<source/unitpoint(__).md>)

### Getting rectangle anchor sources

- [rect(_:)](<source/rect(__).md>) — Returns an anchor source rect defined by `r` in the current view.
- [bounds](source/bounds.md) — An anchor source rect defined as the entire bounding rect of the current view.

### Getting top anchor sources

- [topLeading](source/topleading.md)
- [top](source/top.md)
- [topTrailing](source/toptrailing.md)

### Getting middle anchor sources

- [leading](source/leading.md)
- [center](source/center-869al.md)
- [trailing](source/trailing.md)

### Getting bottom anchor sources

- [bottomTrailing](source/bottomtrailing.md)
- [bottom](source/bottom.md)
- [bottomLeading](source/bottomleading.md)

### Creating an anchor source

- [init(_:)](<source/init(__).md>)

### Type Properties

- [bounds3D](source/bounds3d.md) — An anchor source rect defined as the entire bounding rect of the current element.
- [center](source/center-6w6ww.md) _(deprecated)_
- [center3D](source/center3d.md)

### Type Methods

- [point3D(_:)](<source/point3d(__).md>)
- [rect3D(_:)](<source/rect3d(__).md>) — Returns an anchor source rect defined by `r` in the current element.
- [unitPoint3D(_:)](<source/unitpoint3d(__).md>)
