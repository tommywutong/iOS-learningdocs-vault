---
title: CAScrollLayer
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cascrolllayer
source_url: 'https://developer.apple.com/documentation/quartzcore/cascrolllayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cascrolllayer.json'
content_hash: 'sha256:50e8e931001402a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAScrollLayer

<sub>Class</sub>

A layer that displays scrollable content larger than its own bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAScrollLayer
```

## Overview

The [CAScrollLayer](cascrolllayer.md) class is a subclass of [CALayer](calayer.md) that simplifies displaying a portion of a layer. The extent of the scrollable area of the [CAScrollLayer](cascrolllayer.md) is defined by the layout of its sublayers. The visible portion of the layer content is set by specifying the origin as a point or a rectangular area of the contents to be displayed. [CAScrollLayer](cascrolllayer.md) does not provide keyboard or mouse event-handling, nor does it provide visible scrollers.

## Relationships

- **Inherits From**: [CALayer](calayer.md)

- **Conforms To**: [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Scrolling constraints

- [scrollMode](cascrolllayer/scrollmode.md) — Defines the axes in which the layer may be scrolled.

### Scrolling the layer

- [- scrollToPoint:](<cascrolllayer/scroll(to_)-37q0p.md>) — Changes the origin of the receiver to the specified point.
- [- scrollToRect:](<cascrolllayer/scroll(to_)-782vd.md>) — Scroll the contents of the receiver to ensure that the rectangle is visible.

### Constants

- [Scroll Modes](scroll-modes.md) — These constants describe the supported scroll modes used by the [scrollMode](cascrolllayer/scrollmode.md) property.

## See Also

### Advanced Layer Options

- [CATiledLayer](catiledlayer.md) — A layer that provides a way to asynchronously provide tiles of the layer’s content, potentially cached at multiple levels of detail.
- [CATransformLayer](catransformlayer.md) — Objects used to create true 3D layer hierarchies, rather than the flattened hierarchy rendering model used by other layer types.
- [CAReplicatorLayer](careplicatorlayer.md) — A layer that creates a specified number of sublayer copies with varying geometric, temporal, and color transformations.
