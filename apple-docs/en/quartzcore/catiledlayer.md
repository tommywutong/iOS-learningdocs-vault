---
title: CATiledLayer
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catiledlayer
source_url: 'https://developer.apple.com/documentation/quartzcore/catiledlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catiledlayer.json'
content_hash: 'sha256:cd022166306f5d6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATiledLayer

<sub>Class</sub>

A layer that provides a way to asynchronously provide tiles of the layer’s content, potentially cached at multiple levels of detail.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CATiledLayer
```

## Overview

As more data is required by the renderer, the layer’s [- drawInContext:](<calayer/draw(in_).md>) method is called on one or more background threads to supply the drawing operations to fill in one tile of data. The clip bounds and current transformation matrix (CTM) of the drawing context can be used to determine the bounds and resolution of the tile being requested.

Regions of the layer may be invalidated using the [- setNeedsDisplayInRect:](<calayer/setneedsdisplay(__).md>) method however the update will be asynchronous. While the next display update will most likely not contain the updated content, a future update will.

> [!important] Important
> Do not attempt to directly modify the [contents](calayer/contents.md) property of a [CATiledLayer](catiledlayer.md) object. Doing so disables the ability of a tiled layer to asynchronously provide tiled content, effectively turning the layer into a regular [CALayer](calayer.md) object.

## Relationships

- **Inherits From**: [CALayer](calayer.md)

- **Conforms To**: [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Visual Fade

- [+ fadeDuration](<catiledlayer/fadeduration().md>) — The time, in seconds, that newly added images take to “fade-in” to the rendered representation of the tiled layer.

### Levels of detail

- [levelsOfDetail](catiledlayer/levelsofdetail.md) — The number of levels of detail maintained by this layer.
- [levelsOfDetailBias](catiledlayer/levelsofdetailbias.md) — The number of magnified levels of detail for this layer.

### Layer tile size

- [tileSize](catiledlayer/tilesize.md) — The maximum size of each tile used to create the layer’s content.

## See Also

### Advanced Layer Options

- [CAScrollLayer](cascrolllayer.md) — A layer that displays scrollable content larger than its own bounds.
- [CATransformLayer](catransformlayer.md) — Objects used to create true 3D layer hierarchies, rather than the flattened hierarchy rendering model used by other layer types.
- [CAReplicatorLayer](careplicatorlayer.md) — A layer that creates a specified number of sublayer copies with varying geometric, temporal, and color transformations.
