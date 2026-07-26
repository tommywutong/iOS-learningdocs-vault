---
title: MTLRenderStages
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderstages
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderstages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderstages.json'
content_hash: 'sha256:b590463ea1b4f1d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRenderStages

<sub>Structure</sub>

The stages in a render pass that triggers a synchronization command.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLRenderStages
```

## Overview

Render stage boundaries provide synchronization opportunities within a render pass for specific resources and resource types. For example, you can designate render stage a synchronization point for a memory barrier or a fence (see [memoryBarrier(resources:after:before:)](<mtlrendercommandencoder/memorybarrier(resources_after_before_).md>) and [MTLFence](mtlfence.md), respectively). This allows a GPU to overlap its execution of two adjacent stages, which can shorten its overall runtime for the render pass.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Render pass stages

- [MTLRenderStageObject](mtlrenderstages/object.md) — The object rendering stage.
- [MTLRenderStageMesh](mtlrenderstages/mesh.md) — The mesh rendering stage.
- [MTLRenderStageVertex](mtlrenderstages/vertex.md) — The vertex rendering stage.
- [MTLRenderStageFragment](mtlrenderstages/fragment.md) — The fragment rendering stage.
- [MTLRenderStageTile](mtlrenderstages/tile.md) — The tile rendering stage.

### Swift support

- [init(rawValue:)](<mtlrenderstages/init(rawvalue_).md>) — Creates a render stage from a raw value.

## See Also

### Synchronizing with barriers and fences

- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md) — Block GPU stages in the a pass from running until other stages in the same pass finish.
- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md) — Block GPU stages in a pass until another pass unblocks it by signaling a fence.
- [Synchronizing passes with consumer barriers](synchronizing-passes-with-consumer-barriers.md) — Block GPU stages in a pass, and all subsequent passes, from running until stages from earlier passes finish.
- [Synchronizing passes with producer barriers](synchronizing-passes-with-producer-barriers.md) — Block GPU stages in subsequent passes from running until stages in a pass, and earlier passes, finish.
- [Synchronizing CPU and GPU work](synchronizing-cpu-and-gpu-work.md) — Avoid stalls between CPU and GPU work by using multiple instances of a resource.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — Use fences to synchronize access to resources allocated on a heap.
- [MTLStages](mtlstages.md) — The segments of command execution within the Metal pass types.
- [MTLFence](mtlfence.md) — A synchronization mechanism that orders memory operations between GPU passes.
- [MTLBarrierScope](mtlbarrierscope.md) — Describes the types of resources that a barrier operates on.
- [MTL4VisibilityOptions](mtl4visibilityoptions.md) — Memory consistency options for synchronization commands.
