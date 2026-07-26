---
title: MTL4VisibilityOptions
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4visibilityoptions
source_url: 'https://developer.apple.com/documentation/metal/mtl4visibilityoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4visibilityoptions.json'
content_hash: 'sha256:b14918aa95a6bb19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4VisibilityOptions

<sub>Structure</sub>

Memory consistency options for synchronization commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTL4VisibilityOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<mtl4visibilityoptions/init(rawvalue_).md>)

### Type Properties

- [MTL4VisibilityOptionDevice](mtl4visibilityoptions/device.md) — Flushes caches to the GPU (device) memory coherence point.
- [MTL4VisibilityOptionResourceAlias](mtl4visibilityoptions/resourcealias.md) — Flushes caches to ensure that aliased virtual addresses are memory consistent.

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
- [MTLRenderStages](mtlrenderstages.md) — The stages in a render pass that triggers a synchronization command.
- [MTLBarrierScope](mtlbarrierscope.md) — Describes the types of resources that a barrier operates on.
