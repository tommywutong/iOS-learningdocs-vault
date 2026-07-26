---
title: MTLDrawPrimitivesIndirectArguments
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldrawprimitivesindirectarguments
source_url: 'https://developer.apple.com/documentation/metal/mtldrawprimitivesindirectarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawprimitivesindirectarguments.json'
content_hash: 'sha256:0c49ef2381789a51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDrawPrimitivesIndirectArguments

<sub>Structure</sub>

The data layout required for drawing primitives via indirect buffer calls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLDrawPrimitivesIndirectArguments
```

## Overview

See also the [- drawPrimitives:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawprimitives(type_indirectbuffer_indirectbufferoffset_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtldrawprimitivesindirectarguments/init().md>) — Returns a new data layout for drawing primitives via indirect buffer calls.
- [init(vertexCount:instanceCount:vertexStart:baseInstance:)](<mtldrawprimitivesindirectarguments/init(vertexcount_instancecount_vertexstart_baseinstance_).md>) — Returns a new data layout for drawing primitives via indirect buffer calls, with specified parameters.

### Instance Properties

- [baseInstance](mtldrawprimitivesindirectarguments/baseinstance.md) — The first instance to draw.
- [instanceCount](mtldrawprimitivesindirectarguments/instancecount.md) — The number of instances to draw.
- [vertexCount](mtldrawprimitivesindirectarguments/vertexcount.md) — The number of vertices to draw.
- [vertexStart](mtldrawprimitivesindirectarguments/vertexstart.md) — The first vertex to draw.

## See Also

### Render compute commands

- [MTLIndirectRenderCommand](mtlindirectrendercommand.md) — A render command in an indirect command buffer.
- [MTLDrawPatchIndirectArguments](mtldrawpatchindirectarguments.md) — The data layout required for drawing patches via indirect buffer calls.
- [MTLDrawIndexedPrimitivesIndirectArguments](mtldrawindexedprimitivesindirectarguments.md) — The data layout required for drawing indexed primitives via indirect buffer calls.
