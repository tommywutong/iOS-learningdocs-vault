---
title: MTLDepthClipMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldepthclipmode
source_url: 'https://developer.apple.com/documentation/metal/mtldepthclipmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldepthclipmode.json'
content_hash: 'sha256:7daad36b7c964898'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDepthClipMode

<sub>Enumeration</sub>

The mode that determines how to deal with fragments outside of the near or far planes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLDepthClipMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Clip modes

- [MTLDepthClipModeClip](mtldepthclipmode/clip.md) — Clip fragments outside the near or far planes.
- [MTLDepthClipModeClamp](mtldepthclipmode/clamp.md) — Clamp fragments outside the near or far planes.

### Initializers

- [init(rawValue:)](<mtldepthclipmode/init(rawvalue_).md>)

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
- [MTLVisibilityResultMode](mtlvisibilityresultmode.md) — The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.
- [MTLVisibilityResultType](mtlvisibilityresulttype.md) — This enumeration controls if Metal accumulates visibility results between render encoders or resets them.
