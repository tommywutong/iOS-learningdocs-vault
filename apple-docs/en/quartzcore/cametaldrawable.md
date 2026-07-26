---
title: CAMetalDrawable
framework: Core Animation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldrawable
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldrawable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldrawable.json'
content_hash: 'sha256:72aae25716b5eb75'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAMetalDrawable

<sub>Protocol</sub>

A Metal drawable associated with a Core Animation layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CAMetalDrawable : MTLDrawable
```

## Overview

A [CAMetalLayer](cametallayer.md) instance owns any instance that implements this protocol. Don’t implement this protocol yourself. See the [CAMetalLayer](cametallayer.md) reference for information on how to request drawable objects.

## Relationships

- **Inherits From**: [MTLDrawable](../metal/mtldrawable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the Drawable’s Texture

- [texture](cametaldrawable/texture.md) — A Metal texture object that contains the drawable’s contents.

### Getting the Owning Layer

- [layer](cametaldrawable/layer.md) — The layer that owns this drawable object.

## See Also

### Metal and OpenGL

- [CAMetalLayer](cametallayer.md) — A Core Animation layer that Metal can render into, typically displayed onscreen.
- [CAEAGLLayer](caeagllayer.md) — A layer that supports drawing OpenGL content in iOS and tvOS applications. _(deprecated)_
- [CAEDRMetadata](caedrmetadata.md) — Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [CAOpenGLLayer](caopengllayer.md) — A layer that provides a layer suitable for rendering OpenGL content. _(deprecated)_
- [CARenderer](carenderer.md) — A layer that allows an application to render a layer tree into a Core OpenGL context.
