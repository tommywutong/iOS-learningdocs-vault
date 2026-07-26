---
title: Capsule
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/capsule
source_url: 'https://developer.apple.com/documentation/swiftui/capsule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/capsule.json'
content_hash: 'sha256:4f1743d006922ce7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Capsule

<sub>Structure</sub>

A capsule shape aligned inside the frame of the view containing it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Capsule
```

## Overview

A capsule shape is equivalent to a rounded rectangle where the corner radius is chosen as half the length of the rectangle’s smallest edge.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [InsettableShape](insettableshape.md), [RoundedRectangularShape](roundedrectangularshape.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Creating a capsule

- [init(style:)](<capsule/init(style_).md>) — Creates a new capsule shape.

### Getting the shape’s characteristics

- [style](capsule/style.md)

## See Also

### Creating circular shapes

- [Circle](circle.md) — A circle centered on the frame of the view containing it.
- [Ellipse](ellipse.md) — An ellipse aligned inside the frame of the view containing it.
