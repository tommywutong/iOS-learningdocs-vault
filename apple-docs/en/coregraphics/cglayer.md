---
title: CGLayer
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglayer
source_url: 'https://developer.apple.com/documentation/coregraphics/cglayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglayer.json'
content_hash: 'sha256:bfc504ec094c0361'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGLayer

<sub>Class</sub>

An offscreen context for reusing content drawn with Core Graphics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGLayer
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Layer Objects

- [CGLayerCreateWithContext](<cglayer/init(__size_auxiliaryinfo_).md>) — Creates a layer object that is associated with a graphics context.

### Examining a Layer

- [CGLayerGetContext](cglayer/context.md) — Returns the graphics context associated with a layer object.
- [CGLayerGetSize](cglayer/size.md) — Returns the width and height of a layer object.

### Working with Core Foundation Types

- [CGLayerGetTypeID](cglayer/typeid.md) — Returns the unique type identifier used for [CGLayer](cglayer.md) objects.

## See Also

### 2D Drawing

- [CGContext](cgcontext.md) — A Quartz 2D drawing environment.
- [CGImage](cgimage.md) — A bitmap image or image mask.
- [CGPath](cgpath.md) — An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGMutablePath](cgmutablepath.md) — A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
