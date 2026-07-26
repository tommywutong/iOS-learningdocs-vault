---
title: GraphicsContext.ResolvedSymbol
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/resolvedsymbol
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedsymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/resolvedsymbol.json'
content_hash: 'sha256:35ce0ba649fcdf30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.ResolvedSymbol

<sub>Structure</sub>

A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ResolvedSymbol
```

## Overview

You resolve a child view in preparation for drawing it into a context by calling [resolveSymbol(id:)](<resolvesymbol(id_).md>). The resolved view takes into account environment values like the display resolution and current color scheme.

## Topics

### Getting the symbol properties

- [size](resolvedsymbol/size.md) — The dimensions of the resolved symbol.

## See Also

### Resolving a drawn entity

- [resolve(_:)](<resolve(__).md>) — Gets a version of an image that’s fixed with the current values of the graphics context’s environment.
- [resolveSymbol(id:)](<resolvesymbol(id_).md>) — Gets the identified child view as a resolved symbol, if the view exists.
- [ResolvedImage](resolvedimage.md) — An image resolved to a particular environment.
- [ResolvedText](resolvedtext.md) — A text view resolved to a particular environment.
