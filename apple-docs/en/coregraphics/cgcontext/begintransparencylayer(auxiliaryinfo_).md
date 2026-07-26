---
title: 'beginTransparencyLayer(auxiliaryInfo:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/begintransparencylayer(auxiliaryinfo:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/begintransparencylayer(auxiliaryinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/begintransparencylayer%28auxiliaryinfo%3A%29.json'
content_hash: 'sha256:686a642d7863f606'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# beginTransparencyLayer(auxiliaryInfo:)

<sub>Instance Method</sub>

Begins a transparency layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginTransparencyLayer(auxiliaryInfo: CFDictionary?)
```

## Parameters

- `auxiliaryInfo` — A dictionary that specifies any additional information, or `NULL`.

## Discussion

Until a corresponding call to [CGContextEndTransparencyLayer](<endtransparencylayer().md>), all subsequent drawing operations in the specified context are composited into a fully transparent backdrop (which is treated as a separate destination buffer from the context).

After a call to `CGContextEndTransparencyLayer`, the result is composited into the context using the global alpha and shadow state of the context. This operation respects the clipping region of the context.

After a call to this function, all of the parameters in the graphics state remain unchanged with the exception of the following:

- The global alpha is set to `1`.
- The shadow is turned off.

Ending the transparency layer restores these parameters to their previous values. Core Graphics maintains a transparency layer stack for each context, and transparency layers may be nested.

> [!tip] Tip
> For best performance, make sure that you set the smallest possible clipping area for the objects in the transparency layer prior to calling `CGContextBeginTransparencyLayer`.

## See Also

### Working with Transparency Layers

- [CGContextBeginTransparencyLayerWithRect](<begintransparencylayer(in_auxiliaryinfo_).md>) — Begins a transparency layer whose contents are bounded by the specified rectangle.
- [CGContextEndTransparencyLayer](<endtransparencylayer().md>) — Ends a transparency layer.
