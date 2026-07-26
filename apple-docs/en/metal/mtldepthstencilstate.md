---
title: MTLDepthStencilState
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldepthstencilstate
source_url: 'https://developer.apple.com/documentation/metal/mtldepthstencilstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldepthstencilstate.json'
content_hash: 'sha256:8c3bb8491e837328'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDepthStencilState

<sub>Protocol</sub>

A depth and stencil state instance that specifies the depth and stencil configuration and operations used in a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLDepthStencilState : NSObjectProtocol, Sendable
```

## Overview

The [MTLDepthStencilState](mtldepthstencilstate.md) protocol defines the interface for a lightweight instance used to encode how a graphics rendering pass should perform depth and stencil operations. The [MTLRenderCommandEncoder](mtlrendercommandencoder.md) uses an [MTLDepthStencilState](mtldepthstencilstate.md) instance to set the depth and stencil state for a rendering pass.

The standard allocation and initialization techniques don’t apply when creating an [MTLDepthStencilState](mtldepthstencilstate.md) instance. Instead, you can apply the following steps:

1. Create an [MTLDepthStencilDescriptor](mtldepthstencildescriptor.md) instance that defines the operations you want the rendering pass to use.
2. Create an [MTLDepthStencilState](mtldepthstencilstate.md) instance by passing the descriptor to an [MTLDevice](mtldevice.md) instance’s [- newDepthStencilStateWithDescriptor:](<mtldevice/makedepthstencilstate(descriptor_).md>) method.

Typically, you create [MTLDepthStencilState](mtldepthstencilstate.md) instances when your app is first initialized and then reuse them throughout the lifetime of your app.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying properties

- [device](mtldepthstencilstate/device.md) — The device from which this state object was created.
- [label](mtldepthstencilstate/label.md) — A string that identifies this object.

### Instance Properties

- [gpuResourceID](mtldepthstencilstate/gpuresourceid.md)

## See Also

### Depth testing

- [Calculating primitive visibility using depth testing](calculating-primitive-visibility-using-depth-testing.md) — Determine which pixels are visible in a scene by using a depth texture.
- [MTLDepthStencilDescriptor](mtldepthstencildescriptor.md) — An instance that configures new [MTLDepthStencilState](mtldepthstencilstate.md) instances.
- [MTLStencilDescriptor](mtlstencildescriptor.md) — An object that defines the front-facing or back-facing stencil operations of a depth and stencil state object.
