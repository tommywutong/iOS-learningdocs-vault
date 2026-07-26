---
title: MTLDrawPatchIndirectArguments
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldrawpatchindirectarguments
source_url: 'https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawpatchindirectarguments.json'
content_hash: 'sha256:f56a93ccd153caa4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDrawPatchIndirectArguments

<sub>Structure</sub>

The data layout required for drawing patches via indirect buffer calls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLDrawPatchIndirectArguments
```

## Overview

See also the following methods:

- [- drawPatches:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints_patchindexbuffer_patchindexbufferoffset_indirectbuffer_indirectbufferoffset_).md>)
- [- drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:](<mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffset_indirectbuffer_indirectbufferoffset_).md>)

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtldrawpatchindirectarguments/init().md>) — Returns a new data layout for drawing patches via indirect buffer calls.
- [init(patchCount:instanceCount:patchStart:baseInstance:)](<mtldrawpatchindirectarguments/init(patchcount_instancecount_patchstart_baseinstance_).md>) — Returns a new data layout for drawing patches via indirect buffer calls, with specified parameters.

### Instance Properties

- [baseInstance](mtldrawpatchindirectarguments/baseinstance.md) — The first instance to draw.
- [instanceCount](mtldrawpatchindirectarguments/instancecount.md) — The number of instances to draw.
- [patchCount](mtldrawpatchindirectarguments/patchcount.md) — The number of patches in each instance.
- [patchStart](mtldrawpatchindirectarguments/patchstart.md) — The patch start index.

## See Also

### Render compute commands

- [MTLIndirectRenderCommand](mtlindirectrendercommand.md) — A render command in an indirect command buffer.
- [MTLDrawPrimitivesIndirectArguments](mtldrawprimitivesindirectarguments.md) — The data layout required for drawing primitives via indirect buffer calls.
- [MTLDrawIndexedPrimitivesIndirectArguments](mtldrawindexedprimitivesindirectarguments.md) — The data layout required for drawing indexed primitives via indirect buffer calls.
