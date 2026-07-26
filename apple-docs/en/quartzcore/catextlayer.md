---
title: CATextLayer
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catextlayer
source_url: 'https://developer.apple.com/documentation/quartzcore/catextlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catextlayer.json'
content_hash: 'sha256:47602f84c851341a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATextLayer

<sub>Class</sub>

A layer that provides simple text layout and rendering of plain or attributed strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CATextLayer
```

## Overview

The first line is aligned to the top of the layer.

> [!note] Note
> `CATextLayer` disables sub-pixel antialiasing when rendering text. Text can only be drawn using sub-pixel antialiasing when it is composited into an existing opaque background at the same time that it’s rasterized. There is no way to draw text with sub-pixel antialiasing by itself, whether into an image or a layer, in advance of having the background pixels to weave the text pixels into. Setting the `opacity` property of the layer to [true](../swift/true.md) does not change the rendering mode.

> [!note] Note
> In macOS, when a `CATextLayer` instance is positioned using the [CAConstraintLayoutManager](caconstraintlayoutmanager.md) class the bounds of the layer is resized to fit the text content.

## Relationships

- **Inherits From**: [CALayer](calayer.md)

- **Conforms To**: [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting and Setting the Text

- [string](catextlayer/string.md) — The text to be rendered by the receiver.

### Text Visual Properties

- [font](catextlayer/font.md) — The font used to render the receiver’s text.
- [fontSize](catextlayer/fontsize.md) — The font size used to render the receiver’s text. Animatable.
- [foregroundColor](catextlayer/foregroundcolor.md) — The color used to render the receiver’s text. Animatable.
- [allowsFontSubpixelQuantization](catextlayer/allowsfontsubpixelquantization.md) — Determines whether to allow subpixel quantization for the graphics context used for text rendering.

### Text Alignment and Truncation

- [wrapped](catextlayer/iswrapped.md) — Determines whether the text is wrapped to fit within the receiver’s bounds.
- [alignmentMode](catextlayer/alignmentmode.md) — Determines how individual lines of text are horizontally aligned within the receiver’s bounds.
- [truncationMode](catextlayer/truncationmode.md) — Determines how the text is truncated to fit within the receiver’s bounds.

### Constants

- [Truncation modes](truncation-modes.md) — These constants are used by the [truncationMode](catextlayer/truncationmode.md) property.
- [Horizontal alignment modes](horizontal-alignment-modes.md) — These constants are used by the [alignmentMode](catextlayer/alignmentmode.md) property.

## See Also

### Text, Shapes, and Gradients

- [CAShapeLayer](cashapelayer.md) — A layer that draws a cubic Bezier spline in its coordinate space.
- [CAGradientLayer](cagradientlayer.md) — A layer that draws a color gradient over its background color, filling the shape of the layer.
