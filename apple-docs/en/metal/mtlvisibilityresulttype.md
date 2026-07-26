---
title: MTLVisibilityResultType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvisibilityresulttype
source_url: 'https://developer.apple.com/documentation/metal/mtlvisibilityresulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvisibilityresulttype.json'
content_hash: 'sha256:57c8f6dd3f338966'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVisibilityResultType

<sub>Enumeration</sub>

This enumeration controls if Metal accumulates visibility results between render encoders or resets them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLVisibilityResultType
```

## Overview

You can specify this property for `MTLRenderCommandEncoders` and for `MTL4RenderCommandEncoders` through their descriptors’ `MTLRenderCommandEncoder/visibilityResultType` and `MTL4RenderCommandEncoder/visibilityResultType` methods.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTLVisibilityResultTypeAccumulate](mtlvisibilityresulttype/accumulate.md) — Accumulate visibility results data across multiple render passes.
- [MTLVisibilityResultTypeReset](mtlvisibilityresulttype/reset.md) — Reset visibility result data when you create a render command encoder.

### Initializers

- [init(rawValue:)](<mtlvisibilityresulttype/init(rawvalue_).md>)

## See Also

### Encoding a render pass

- [MTL4RenderCommandEncoder](mtl4rendercommandencoder.md) — Encodes configuration and draw commands for a single render pass into a command buffer.
- [MTLRenderCommandEncoder](mtlrendercommandencoder.md) — Encodes configuration and draw commands for a single render pass into a command buffer.
- [MTL4RenderEncoderOptions](mtl4renderencoderoptions.md) — Custom render pass options you specify at encoder creation time.
- [MTLTriangleFillMode](mtltrianglefillmode.md) — Specifies how to rasterize triangle and triangle strip primitives.
- [MTLWinding](mtlwinding.md) — The vertex winding rule that determines a front-facing primitive.
- [MTLCullMode](mtlcullmode.md) — The mode that determines whether to perform culling and which type of primitive to cull.
- [MTLPrimitiveType](mtlprimitivetype.md) — The geometric primitive type for drawing commands.
- [MTLIndexType](mtlindextype.md) — The index type for an index buffer that references vertices of geometric primitives.
- [MTLDepthClipMode](mtldepthclipmode.md) — The mode that determines how to deal with fragments outside of the near or far planes.
- [MTLVisibilityResultMode](mtlvisibilityresultmode.md) — The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.
