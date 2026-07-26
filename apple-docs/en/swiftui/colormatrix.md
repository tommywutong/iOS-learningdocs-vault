---
title: ColorMatrix
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/colormatrix
source_url: 'https://developer.apple.com/documentation/swiftui/colormatrix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/colormatrix.json'
content_hash: 'sha256:6fad639d6c823cd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ColorMatrix

<sub>Structure</sub>

A matrix to use in an RGBA color transformation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ColorMatrix
```

## Overview

The matrix has five columns, each with a red, green, blue, and alpha component. You can use the matrix for tasks like creating a color transformation [Filter](graphicscontext/filter.md) for a [GraphicsContext](graphicscontext.md) using the [colorMatrix(_:)](<graphicscontext/filter/colormatrix(__).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an identity matrix

- [init()](<colormatrix/init().md>) — Creates the identity matrix.

### First column

- [r1](colormatrix/r1.md)
- [g1](colormatrix/g1.md)
- [b1](colormatrix/b1.md)
- [a1](colormatrix/a1.md)

### Second column

- [r2](colormatrix/r2.md)
- [g2](colormatrix/g2.md)
- [b2](colormatrix/b2.md)
- [a2](colormatrix/a2.md)

### Third column

- [r3](colormatrix/r3.md)
- [g3](colormatrix/g3.md)
- [b3](colormatrix/b3.md)
- [a3](colormatrix/a3.md)

### Fourth column

- [r4](colormatrix/r4.md)
- [g4](colormatrix/g4.md)
- [b4](colormatrix/b4.md)
- [a4](colormatrix/a4.md)

### Fifth column

- [r5](colormatrix/r5.md)
- [g5](colormatrix/g5.md)
- [b5](colormatrix/b5.md)
- [a5](colormatrix/a5.md)

## See Also

### Applying blur and shadows

- [blur(radius:opaque:)](<view/blur(radius_opaque_).md>) — Applies a Gaussian blur to this view.
- [shadow(color:radius:x:y:)](<view/shadow(color_radius_x_y_).md>) — Adds a shadow to this view.
