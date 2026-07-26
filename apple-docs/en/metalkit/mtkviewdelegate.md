---
title: MTKViewDelegate
framework: MetalKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtkviewdelegate
source_url: 'https://developer.apple.com/documentation/metalkit/mtkviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkviewdelegate.json'
content_hash: 'sha256:ab385760207c8333'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKViewDelegate

<sub>Protocol</sub>

Methods for responding to a MetalKit view’s drawing and resizing events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTKViewDelegate : NSObjectProtocol
```

## Overview

You can set an object that implements the [MTKViewDelegate](mtkviewdelegate.md) protocol as a [MTKView](mtkview.md) object’s delegate. Use a delegate to provide a drawing method to a [MTKView](mtkview.md) object and respond to rendering events without subclassing the [MTKView](mtkview.md) class.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Changing the View’s Layout

- [- mtkView:drawableSizeWillChange:](<mtkviewdelegate/mtkview(__drawablesizewillchange_).md>) — Updates the view’s contents upon receiving a change in layout, resolution, or size.

### Drawing the View’s Contents

- [- drawInMTKView:](<mtkviewdelegate/draw(in_).md>) — Draws the view’s contents.

## See Also

### View Management

- [MTKView](mtkview.md) — A specialized view that creates, configures, and displays Metal objects.
