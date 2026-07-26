---
title: MTLDrawIndexedPrimitivesIndirectArguments
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldrawindexedprimitivesindirectarguments
source_url: 'https://developer.apple.com/documentation/metal/mtldrawindexedprimitivesindirectarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawindexedprimitivesindirectarguments.json'
content_hash: 'sha256:478a5f6c77d052bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDrawIndexedPrimitivesIndirectArguments

<sub>Structure</sub>

The data layout required for drawing indexed primitives via indirect buffer calls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLDrawIndexedPrimitivesIndirectArguments
```

## Overview

See also the [- drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawindexedprimitives(type_indextype_indexbuffer_indexbufferoffset_indirectbuffer_indirectbufferoffset_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtldrawindexedprimitivesindirectarguments/init().md>) — Returns a new data layout for drawing indexed primitives via indirect buffer calls.
- [init(indexCount:instanceCount:indexStart:baseVertex:baseInstance:)](<mtldrawindexedprimitivesindirectarguments/init(indexcount_instancecount_indexstart_basevertex_baseinstance_).md>) — Returns a new data layout for drawing indexed primitives via indirect buffer calls, with specified parameters.

### Instance Properties

- [baseInstance](mtldrawindexedprimitivesindirectarguments/baseinstance.md) — The first instance to draw.
- [baseVertex](mtldrawindexedprimitivesindirectarguments/basevertex.md) — The first vertex to draw.
- [indexCount](mtldrawindexedprimitivesindirectarguments/indexcount.md) — For each instance, the number of indices to read from the index buffer.
- [indexStart](mtldrawindexedprimitivesindirectarguments/indexstart.md) — The first index to draw.
- [instanceCount](mtldrawindexedprimitivesindirectarguments/instancecount.md) — The number of instances to draw.

## See Also

### Render compute commands

- [MTLIndirectRenderCommand](mtlindirectrendercommand.md) — A render command in an indirect command buffer.
- [MTLDrawPatchIndirectArguments](mtldrawpatchindirectarguments.md) — The data layout required for drawing patches via indirect buffer calls.
- [MTLDrawPrimitivesIndirectArguments](mtldrawprimitivesindirectarguments.md) — The data layout required for drawing primitives via indirect buffer calls.
