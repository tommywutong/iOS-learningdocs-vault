---
title: GraphicsContext.GradientOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/gradientoptions
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/gradientoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/gradientoptions.json'
content_hash: 'sha256:50ca24c9cb82d52a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.GradientOptions

<sub>Structure</sub>

Options that affect the rendering of color gradients.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct GradientOptions
```

## Overview

Use these options to affect how SwiftUI manages a gradient that you create for a [Shading](shading.md) instance for use in a [GraphicsContext](../graphicscontext.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Getting gradient options

- [linearColor](gradientoptions/linearcolor.md) — An option that interpolates between colors in a linear color space.
- [mirror](gradientoptions/mirror.md) — An option that repeats the gradient outside its nominal range, reflecting every other instance.
- [repeat](gradientoptions/repeat.md) — An option that repeats the gradient outside its nominal range.

## See Also

### Drawing a path

- [stroke(_:with:lineWidth:)](<stroke(__with_linewidth_).md>) — Draws a path into the context with a specified line width.
- [stroke(_:with:style:)](<stroke(__with_style_).md>) — Draws a path into the context with a specified stroke style.
- [fill(_:with:style:)](<fill(__with_style_).md>) — Draws a path into the context and fills the outlined region.
- [Shading](shading.md) — A color or pattern that you can use to outline or fill a path.
