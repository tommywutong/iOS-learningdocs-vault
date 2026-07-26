---
title: GraphicsContext.ResolvedImage
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/resolvedimage
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/resolvedimage.json'
content_hash: 'sha256:25ce1c69c528f6e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.ResolvedImage

<sub>Structure</sub>

An image resolved to a particular environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ResolvedImage
```

## Overview

You resolve an [Image](../image.md) in preparation for drawing it into a context, either manually by calling [resolve(_:)](<resolve(__)-898z6.md>), or automatically when calling [draw(_:in:style:)](<draw(__in_style_)-blhz.md>) or [draw(_:at:anchor:)](<draw(__at_anchor_)-1z5wt.md>). The resolved image takes into account environment values like the display resolution and current color scheme.

## Topics

### Getting the image properties

- [size](resolvedimage/size.md) — The size of the image.
- [baseline](resolvedimage/baseline.md) — The distance from the top of the image to its baseline.
- [shading](resolvedimage/shading.md) — An optional shading to fill the image with.

## See Also

### Resolving a drawn entity

- [resolve(_:)](<resolve(__).md>) — Gets a version of an image that’s fixed with the current values of the graphics context’s environment.
- [resolveSymbol(id:)](<resolvesymbol(id_).md>) — Gets the identified child view as a resolved symbol, if the view exists.
- [ResolvedSymbol](resolvedsymbol.md) — A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.
- [ResolvedText](resolvedtext.md) — A text view resolved to a particular environment.
