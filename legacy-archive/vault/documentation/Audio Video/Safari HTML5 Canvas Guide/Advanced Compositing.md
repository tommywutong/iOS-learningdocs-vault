---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/Compositing/Compositing.html
archived_at: '2026-07-15T05:21:05.882695Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Creating%20Charts%20and%20Graphs.md)[Previous](Matrix%20Transforms.md)

# Advanced Compositing

By default, images are layered on the canvas in drawing order, with new images layered on top of older images. Also by default, images that have areas with alpha values less than 1 are partly or wholly transparent, letting lower layers show through to varying degrees.

The web page background is the lowest layer, followed by any HTML elements positioned beneath the canvas element. Any CSS background applied to the canvas element comes next, followed by anything drawn on the canvas, with the most recent image, line, or shape in the top layer.

The canvas element also supports a global alpha channel. The global alpha channel can be set to any value between 0 and 1, inclusive, and defaults to 1. All drawing operations have their alpha values multiplied by the global alpha value, and so can be attenuated to any degree, up to full transparency. This allows you to draw semitransparent images, even if the source image has no alpha channel.

The global alpha value, simple layering, and the default alpha-channel compositing mode provide sufficient compositing capabilities for most applications, but canvas has ten other built-in compositing modes in addition to the default mode, and supports vendor-specific extensions as well.

The global alpha value allows you to draw with varying degrees of transparency. Set the global alpha value by assigning it to the context’s `globalAlpha` property.

`ctx.globalAlpha = alpha`

The `alpha` value must be a number between 0 and 1, inclusive.

A value of 1 does not change the native alpha value of images, colors, gradients, or patterns. No transparency is added.

A value of less than 1 reduces the alpha values of all drawing operations proportionately.

A value of 0 causes all subsequent drawing operations to render transparently.

The canvas element has eleven built-in compositing modes, including the default mode, and support for vendor-specific extensions. You set a compositing mode by setting the context’s `globalCompositeOperation` property to one of these values:

- `"source-over"` (default)
- `"source-atop"`
- `"source-in"`
- `"source-out"`
- `"destination-over"`
- `"destination-atop"`
- `"destination-in"`
- `"destination-out"`
- `"lighter"`
- `"copy"`
- `"xor"`
- _“vendorName-operationName”_

Example: `ctx.globalCompositeOperation = "copy";`

Compositing deals with a source (the image being drawn), and a destination (the canvas and anything already on it).

Source and destination pixels can be opaque (`alpha = 1`), transparent (`alpha = 0`), or translucent (`0` < `alpha` < `1`).

The result of the composition can be to display the source pixel, the destination pixel, a transparent pixel (erase both source and destination to transparent), or a combination pixel, which uses values from the source and destination, combined using an algorithm.

A detailed description of the composition modes follows.

- __source-over__—The default value for compositing. Display the source image wherever the source image is opaque. Display the destination image wherever the source is transparent. Display a blend of source and destination wherever the source is translucent (`0` < `alpha` < `1`).
- __source-atop__—Display the source image wherever both images are opaque. Display a blend wherever the source is translucent and the destination is either translucent or opaque. Display the destination image wherever the source image is transparent. Display transparency where the destination is transparent.
- __source-in__—Display the source image wherever both the source image and destination image are opaque. Display a blend wherever the source and destination are both translucent. Display transparency wherever either the source or destination are transparent.
- __source-out__—Display the source image wherever the source image is opaque and the destination image is transparent. Display a blend wherever both the source and destination are translucent. Display transparency elsewhere.
- __destination-over__—Display the destination image wherever the destination image is opaque. Display the source image wherever the destination is transparent. Display a blend of source and destination wherever the destination is translucent.
- __destination-atop__—Display the destination image wherever both images are opaque. Display a blend wherever the destination is translucent and the source is either translucent or opaque. Display the source image wherever the destination image is transparent.
- __destination-in__—Display the destination image wherever both the destination image and source image are opaque. Display a blend wherever the destination and source are both translucent. Display transparency wherever either the destination or source are transparent.
- __destination-out__—Display the destination image wherever the destination image is opaque and the source image is transparent. Display a blend wherever both the destination and source are translucent. Display transparency elsewhere.
- __lighter__—Display an image in which the RGBa color values of source and destination are summed, with a maximum RGB value of 255 and a maximum alpha value of 1.
- __copy__—Display the source image wherever it is opaque or translucent. Display the destination image only where the source image is transparent.
- __xor__—Display the result of a bitwise exclusive-OR operation between the source and destination pixels. This operation is reversible—drawing the source a second time using xor composition restores the destination exactly.

[Next](Creating%20Charts%20and%20Graphs.md)[Previous](Matrix%20Transforms.md)

