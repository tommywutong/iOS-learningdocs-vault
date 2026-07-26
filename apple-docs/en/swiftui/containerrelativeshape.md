---
title: ContainerRelativeShape
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/containerrelativeshape
source_url: 'https://developer.apple.com/documentation/swiftui/containerrelativeshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/containerrelativeshape.json'
content_hash: 'sha256:a233da8390e2da0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ContainerRelativeShape

<sub>Structure</sub>

A shape whose dimensions the system calculates from an inset version of the current container shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ContainerRelativeShape
```

## Overview

If there is not a current container shape, the system provides a rectangle.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [InsettableShape](insettableshape.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Creating the shape

- [init()](<containerrelativeshape/init().md>)

## See Also

### Setting a container shape

- [containerShape(_:)](<view/containershape(__).md>) — Sets the container shape to use for any container relative shape or concentric rectangle within this view.
- [InsettableShape](insettableshape.md) — A shape type that is able to inset itself to produce another shape.
