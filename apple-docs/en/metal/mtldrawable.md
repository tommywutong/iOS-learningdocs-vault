---
title: MTLDrawable
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldrawable
source_url: 'https://developer.apple.com/documentation/metal/mtldrawable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawable.json'
content_hash: 'sha256:f075ee233aad48c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDrawable

<sub>Protocol</sub>

A displayable resource that can be rendered or written to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLDrawable : NSObjectProtocol
```

## Overview

Objects that implement this protocol are connected both to the Metal framework and an underlying display system (such as Core Animation) that’s capable of showing content onscreen. You use drawable objects when you want to render images using Metal and present them onscreen.

Don’t implement this protocol yourself; instead, see [CAMetalLayer](../quartzcore/cametallayer.md), for a class that can create and manage drawable objects for you.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Identifying the drawable

- [drawableID](mtldrawable/drawableid.md) — A positive integer that identifies the drawable.

### Presenting the drawable

- [- present](<mtldrawable/present().md>) — Presents the drawable onscreen as soon as possible.
- [- presentAfterMinimumDuration:](<mtldrawable/present(afterminimumduration_).md>) — Presents the drawable onscreen as soon as possible after a previous drawable is visible for the specified duration.
- [- presentAtTime:](<mtldrawable/present(at_).md>) — Presents the drawable onscreen at a specific host time.

### Getting presentation information

- [- addPresentedHandler:](<mtldrawable/addpresentedhandler(__).md>) — Registers a block of code to be called immediately after the drawable is presented.
- [presentedTime](mtldrawable/presentedtime.md) — The host time, in seconds, when the drawable was displayed onscreen.

## See Also

### Render pass outputs

- [MTLDrawablePresentedHandler](mtldrawablepresentedhandler.md) — A block of code invoked after a drawable is presented.
