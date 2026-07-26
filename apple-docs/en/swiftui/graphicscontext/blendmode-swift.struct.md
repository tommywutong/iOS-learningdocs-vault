---
title: GraphicsContext.BlendMode
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/blendmode-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/blendmode-swift.struct.json'
content_hash: 'sha256:a5d2a3853086cfd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.BlendMode

<sub>Structure</sub>

The ways that a graphics context combines new content with background content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct BlendMode
```

## Overview

Use one of these values to set the [blendMode](blendmode-swift.property.md) property of a [GraphicsContext](../graphicscontext.md). The value that you set affects how content that you draw replaces or combines with content that you previously drew into the context.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the default

- [normal](blendmode-swift.struct/normal.md) — A mode that paints source image samples over the background image samples.

### Darkening

- [darken](blendmode-swift.struct/darken.md) — A mode that creates composite image samples by choosing the darker samples from either the source image or the background.
- [multiply](blendmode-swift.struct/multiply.md) — A mode that multiplies the source image samples with the background image samples.
- [colorBurn](blendmode-swift.struct/colorburn.md) — A mode that darkens background image samples to reflect the source image samples.
- [plusDarker](blendmode-swift.struct/plusdarker.md) — A mode that adds the inverse of the color components of the source and background images, and then inverts the result, producing a darkened composite.

### Lightening

- [lighten](blendmode-swift.struct/lighten.md) — A mode that creates composite image samples by choosing the lighter samples from either the source image or the background.
- [screen](blendmode-swift.struct/screen.md) — A mode that multiplies the inverse of the source image samples with the inverse of the background image samples.
- [colorDodge](blendmode-swift.struct/colordodge.md) — A mode that brightens the background image samples to reflect the source image samples.
- [plusLighter](blendmode-swift.struct/pluslighter.md) — A mode that adds the components of the source and background images, resulting in a lightened composite.

### Adding contrast

- [overlay](blendmode-swift.struct/overlay.md) — A mode that either multiplies or screens the source image samples with the background image samples, depending on the background color.
- [softLight](blendmode-swift.struct/softlight.md) — A mode that either darkens or lightens colors, depending on the source image sample color.
- [hardLight](blendmode-swift.struct/hardlight.md) — A mode that either multiplies or screens colors, depending on the source image sample color.

### Inverting

- [difference](blendmode-swift.struct/difference.md) — A mode that subtracts the brighter of the source image sample color or the background image sample color from the other.
- [exclusion](blendmode-swift.struct/exclusion.md) — A mode that produces an effect similar to that produced by the difference blend mode, but with lower contrast.

### Mixing color components

- [hue](blendmode-swift.struct/hue.md) — A mode that uses the luminance and saturation values of the background with the hue of the source image.
- [saturation](blendmode-swift.struct/saturation.md) — A mode that uses the luminance and hue values of the background with the saturation of the source image.
- [color](blendmode-swift.struct/color.md) — A mode that uses the luminance values of the background with the hue and saturation values of the source image.
- [luminosity](blendmode-swift.struct/luminosity.md) — A mode that uses the hue and saturation of the background with the luminance of the source image.

### Accessing Porter-Duff modes

- [clear](blendmode-swift.struct/clear.md) — A mode that clears any pixels that the source image overwrites.
- [copy](blendmode-swift.struct/copy.md) — A mode that replaces background image samples with source image samples.
- [sourceIn](blendmode-swift.struct/sourcein.md) — A mode that you use to paint the source image, including its transparency, onto the opaque parts of the background.
- [sourceOut](blendmode-swift.struct/sourceout.md) — A mode that you use to paint the source image onto the transparent parts of the background, while erasing the background.
- [sourceAtop](blendmode-swift.struct/sourceatop.md) — A mode that you use to paint the opaque parts of the source image onto the opaque parts of the background.
- [destinationOver](blendmode-swift.struct/destinationover.md) — A mode that you use to paint the source image under the background.
- [destinationIn](blendmode-swift.struct/destinationin.md) — A mode that you use to erase any of the background that isn’t covered by opaque source pixels.
- [destinationOut](blendmode-swift.struct/destinationout.md) — A mode that you use to erase any of the background that is covered by opaque source pixels.
- [destinationAtop](blendmode-swift.struct/destinationatop.md) — A mode that you use to paint the source image under the background, while erasing any of the background not matched by opaque pixels from the source image.
- [xor](blendmode-swift.struct/xor.md) — A mode that you use to clear pixels where both the source and background images are opaque.

## See Also

### Setting opacity and the blend mode

- [opacity](opacity.md) — The opacity of drawing operations in the context.
- [blendMode](blendmode-swift.property.md) — The blend mode used by drawing operations in the context.
