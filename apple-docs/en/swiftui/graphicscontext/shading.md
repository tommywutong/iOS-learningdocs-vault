---
title: GraphicsContext.Shading
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/shading
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading.json'
content_hash: 'sha256:187576a5036eb5e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.Shading

<sub>Structure</sub>

A color or pattern that you can use to outline or fill a path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Shading
```

## Overview

Use a shading instance to describe the color or pattern of a path that you outline with a method like [stroke(_:with:style:)](<stroke(__with_style_).md>), or of the interior of a region that you fill with the [fill(_:with:style:)](<fill(__with_style_).md>) method. Get a shading instance by calling one of the `Shading` structure’s factory methods. You can base shading on:

- A [Color](../color.md).
- A [Gradient](../gradient.md).
- Any type that conforms to [ShapeStyle](../shapestyle.md).
- An [Image](../image.md).
- What you’ve already drawn into the context.
- A collection of other shading instances.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Colors

- [color(_:)](<shading/color(__).md>) — Returns a shading instance that fills with a color.
- [color(_:red:green:blue:opacity:)](<shading/color(__red_green_blue_opacity_).md>) — Returns a shading instance that fills with a color in the given color space.
- [color(_:white:opacity:)](<shading/color(__white_opacity_).md>) — Returns a shading instance that fills with a monochrome color in the given color space.

### Gradients

- [linearGradient(_:startPoint:endPoint:options:)](<shading/lineargradient(__startpoint_endpoint_options_).md>) — Returns a shading instance that fills a linear (axial) gradient.
- [radialGradient(_:center:startRadius:endRadius:options:)](<shading/radialgradient(__center_startradius_endradius_options_).md>) — Returns a shading instance that fills a radial gradient.
- [conicGradient(_:center:angle:options:)](<shading/conicgradient(__center_angle_options_).md>) — Returns a shading instance that fills a conic (angular) gradient.

### Other shape styles

- [style(_:)](<shading/style(__).md>) — Returns a shading instance that fills with the given shape style.
- [foreground](shading/foreground.md) — A shading instance that fills with the foreground style from the graphics context’s environment.

### Images

- [tiledImage(_:origin:sourceRect:scale:)](<shading/tiledimage(__origin_sourcerect_scale_).md>) — Returns a shading instance that tiles an image across the infinite plane.

### Composite shading types

- [palette(_:)](<shading/palette(__).md>) — Returns a multilevel shading instance constructed from an array of shading instances.
- [backdrop](shading/backdrop.md) — A shading instance that draws a copy of the current background.

### Using a custom Metal shader

- [shader(_:bounds:)](<shading/shader(__bounds_).md>) — Returns a shading instance that fills with the results of querying a shader for each pixel.

### Type Methods

- [meshGradient(_:)](<shading/meshgradient(__).md>) — Returns a shading instance that fills with a mesh gradient.
- [radialGradient(_:startCenter:startRadius:endCenter:endRadius:options:)](<shading/radialgradient(__startcenter_startradius_endcenter_endradius_options_).md>) — Returns a shading that fills a two-point radial gradient.

## See Also

### Drawing a path

- [stroke(_:with:lineWidth:)](<stroke(__with_linewidth_).md>) — Draws a path into the context with a specified line width.
- [stroke(_:with:style:)](<stroke(__with_style_).md>) — Draws a path into the context with a specified stroke style.
- [fill(_:with:style:)](<fill(__with_style_).md>) — Draws a path into the context and fills the outlined region.
- [GradientOptions](gradientoptions.md) — Options that affect the rendering of color gradients.
