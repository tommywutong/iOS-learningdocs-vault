---
title: MTLVisibilityResultMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvisibilityresultmode
source_url: 'https://developer.apple.com/documentation/metal/mtlvisibilityresultmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvisibilityresultmode.json'
content_hash: 'sha256:a377dea6b0bee05c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVisibilityResultMode

<sub>Enumeration</sub>

The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLVisibilityResultMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Result modes

- [MTLVisibilityResultModeDisabled](mtlvisibilityresultmode/disabled.md) — The result doesn’t contain any data because visibility testing was disabled.
- [MTLVisibilityResultModeBoolean](mtlvisibilityresultmode/boolean.md) — The result records whether any samples passed depth and stencil tests.
- [MTLVisibilityResultModeCounting](mtlvisibilityresultmode/counting.md) — The result records how many samples passed depth and stencil tests.

### Initializers

- [init(rawValue:)](<mtlvisibilityresultmode/init(rawvalue_).md>)

## See Also

### Related Documentation

- [- setVisibilityResultMode:offset:](<mtlrendercommandencoder/setvisibilityresultmode(__offset_).md>) — Configures which visibility test the GPU runs and the destination for any results it generates.

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
- [MTLVisibilityResultType](mtlvisibilityresulttype.md) — This enumeration controls if Metal accumulates visibility results between render encoders or resets them.
