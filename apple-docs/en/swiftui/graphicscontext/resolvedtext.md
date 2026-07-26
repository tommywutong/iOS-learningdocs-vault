---
title: GraphicsContext.ResolvedText
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/resolvedtext
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedtext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/resolvedtext.json'
content_hash: 'sha256:bda43412856b44d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.ResolvedText

<sub>Structure</sub>

A text view resolved to a particular environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ResolvedText
```

## Overview

You resolve a [Text](../text.md) view in preparation for drawing it into a context, either manually by calling [resolve(_:)](<resolve(__)-4dx65.md>) or automatically when calling [draw(_:in:)](<draw(__in_)-5opqf.md>) or [draw(_:at:anchor:)](<draw(__at_anchor_)-5dgmd.md>). The resolved text view takes into account environment values like the display resolution and current color scheme.

## Topics

### Getting the text properties

- [firstBaseline(in:)](<resolvedtext/firstbaseline(in_).md>) — Gets the distance from the first line’s ascender to its baseline.
- [lastBaseline(in:)](<resolvedtext/lastbaseline(in_).md>) — Gets the distance from the first line’s ascender to the last line’s baseline.
- [measure(in:)](<resolvedtext/measure(in_).md>) — Measures the size of the resolved text for a given area into which the text should be placed.
- [shading](resolvedtext/shading.md) — The shading to fill uncolored text regions with.

## See Also

### Resolving a drawn entity

- [resolve(_:)](<resolve(__).md>) — Gets a version of an image that’s fixed with the current values of the graphics context’s environment.
- [resolveSymbol(id:)](<resolvesymbol(id_).md>) — Gets the identified child view as a resolved symbol, if the view exists.
- [ResolvedSymbol](resolvedsymbol.md) — A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.
- [ResolvedImage](resolvedimage.md) — An image resolved to a particular environment.
