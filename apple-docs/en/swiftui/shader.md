---
title: Shader
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shader
source_url: 'https://developer.apple.com/documentation/swiftui/shader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shader.json'
content_hash: 'sha256:e34d7aa8a8c24544'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Shader

<sub>Structure</sub>

A reference to a function in a Metal shader library, along with its bound uniform argument values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Shader
```

## Overview

Shader values can be used as filter effects on views, see the [colorEffect(_:isEnabled:)](<view/coloreffect(__isenabled_).md>), [distortionEffect(_:maxSampleOffset:isEnabled:)](<view/distortioneffect(__maxsampleoffset_isenabled_).md>), and [layerEffect(_:maxSampleOffset:isEnabled:)](<view/layereffect(__maxsampleoffset_isenabled_).md>) functions.

Shaders also conform to the [ShapeStyle](shapestyle.md) protocol, letting their MSL shader function provide per-pixel color to fill any shape or text view. For a shader function to act as a fill pattern it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position, args...)
```

where `position` is the user-space coordinates of the pixel applied to the shader, and `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the premultiplied color value in the color space of the destination (typically extended sRGB).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ShapeStyle](shapestyle.md)

## Topics

### Creating a shader

- [init(function:arguments:)](<shader/init(function_arguments_).md>) — Creates a new shader from a function and the uniform argument values to bind to the function.
- [Argument](shader/argument.md) — A single uniform argument value to a shader function.

### Getting the shader function

- [function](shader/function.md) — The shader function called by the shader.
- [arguments](shader/arguments.md) — The uniform argument values passed to the shader function.

### Configuring the shader

- [dithersColor](shader/ditherscolor.md) — For shader functions that return color values, whether the returned color has dither noise added to it, or is simply rounded to the output bit-depth. For shaders generating smooth gradients, dithering is usually necessary to prevent visible banding in the result.

### Structures

- [UsageType](shader/usagetype.md) — The different ways in which a `Shader` may be used to render.

### Instance Methods

- [compile(as:)](<shader/compile(as_).md>) — Attempts to asynchronously compile a shader function, to minimize the chance of stalling when it is first used for rendering.

## See Also

### Accessing Metal shaders

- [colorEffect(_:isEnabled:)](<view/coloreffect(__isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [distortionEffect(_:maxSampleOffset:isEnabled:)](<view/distortioneffect(__maxsampleoffset_isenabled_).md>) — Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](<view/layereffect(__maxsampleoffset_isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [ShaderFunction](shaderfunction.md) — A reference to a function in a Metal shader library.
- [ShaderLibrary](shaderlibrary.md) — A Metal shader library.
