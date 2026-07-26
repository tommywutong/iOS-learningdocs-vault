---
title: GraphicsContext.Filter
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/filter
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter.json'
content_hash: 'sha256:c79d9b300312acea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.Filter

<sub>Structure</sub>

A type that applies image processing operations to rendered content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Filter
```

## Overview

Create and configure a filter that produces an image processing effect, like adding a drop shadow or a blur effect, by calling one of the factory methods defined by the `Filter` structure. Call the [addFilter(_:options:)](<addfilter(__options_).md>) method to add the filter to a [GraphicsContext](../graphicscontext.md). The filter only affects content that you draw into the context after adding the filter.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Changing brightness and contrast

- [brightness(_:)](<filter/brightness(__).md>) — Returns a filter that applies a brightness adjustment.
- [contrast(_:)](<filter/contrast(__).md>) — Returns a filter that applies a contrast adjustment.

### Manipulating color

- [saturation(_:)](<filter/saturation(__).md>) — Returns a filter that applies a saturation adjustment.
- [colorInvert(_:)](<filter/colorinvert(__).md>) — Returns a filter that inverts the color of their results.
- [colorMultiply(_:)](<filter/colormultiply(__).md>) — Returns a filter that multiplies each color component by the matching component of a given color.
- [hueRotation(_:)](<filter/huerotation(__).md>) — Returns a filter that applies a hue rotation adjustment.
- [grayscale(_:)](<filter/grayscale(__).md>) — Returns a filter that applies a grayscale adjustment.
- [colorMatrix(_:)](<filter/colormatrix(__).md>) — Returns a filter that multiplies by a given color matrix.

### Adding blur

- [blur(radius:options:)](<filter/blur(radius_options_).md>) — Returns a filter that applies a Gaussian blur.

### Adding a shadow

- [shadow(color:radius:x:y:blendMode:options:)](<filter/shadow(color_radius_x_y_blendmode_options_).md>) — Returns a filter that adds a shadow.

### Adjusting opacity

- [luminanceToAlpha](filter/luminancetoalpha.md) — Returns a filter that sets the opacity of each pixel based on its luminance.
- [alphaThreshold(min:max:color:)](<filter/alphathreshold(min_max_color_).md>) — Returns a filter that replaces each pixel with alpha components within a range by a constant color, or transparency otherwise.

### Adding a transformation

- [projectionTransform(_:)](<filter/projectiontransform(__).md>) — Returns a filter that transforms the rasterized form of subsequent graphics primitives.

### Using a custom Metal shader

- [colorShader(_:)](<filter/colorshader(__).md>) — Returns a filter that applies `shader` to the color of each source pixel.
- [distortionShader(_:maxSampleOffset:)](<filter/distortionshader(__maxsampleoffset_).md>) — Returns a filter that applies `shader` as a geometric distortion effect on the location of each pixel.
- [layerShader(_:maxSampleOffset:)](<filter/layershader(__maxsampleoffset_).md>) — Returns a filter that applies `shader` to the contents of the source layer.

### Type Methods

- [alphaMultiply(_:)](<filter/alphamultiply(__).md>) — Returns a filter that multiplies the alpha component by a given color.
- [colorMatrix(_:isPremultiplied:)](<filter/colormatrix(__ispremultiplied_).md>) — Returns a filter that multiplies by a given color matrix.

## See Also

### Filtering

- [addFilter(_:options:)](<addfilter(__options_).md>) — Adds a filter that applies to subsequent drawing operations.
- [FilterOptions](filteroptions.md) — Options that configure a filter that you add to a graphics context.
- [BlurOptions](bluroptions.md) — Options that configure the graphics context filter that creates blur.
- [ShadowOptions](shadowoptions.md) — Options that configure the graphics context filter that creates shadows.
