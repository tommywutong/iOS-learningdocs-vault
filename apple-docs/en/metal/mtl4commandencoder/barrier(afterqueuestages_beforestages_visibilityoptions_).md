---
title: 'barrier(afterQueueStages:beforeStages:visibilityOptions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandencoder/barrier(afterqueuestages:beforestages:visibilityoptions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandencoder/barrier(afterqueuestages:beforestages:visibilityoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandencoder/barrier%28afterqueuestages%3Abeforestages%3Avisibilityoptions%3A%29.json'
content_hash: 'sha256:272f3a7395821146'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandEncoder](../mtl4commandencoder.md)

# barrier(afterQueueStages:beforeStages:visibilityOptions:)

<sub>Instance Method</sub>

Encodes a consumer barrier on work you commit to the same command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func barrier(afterQueueStages: MTLStages, beforeStages: MTLStages, visibilityOptions: MTL4VisibilityOptions = [ .device ])
```

## Parameters

- `afterQueueStages` — [MTLStages](../mtlstages.md) mask that represents the stages of work to wait for. This argument applies to work corresponding to these stages you encode in prior command encoders, and not for the current encoder.

- `beforeStages` — [MTLStages](../mtlstages.md) mask that represents the stages of work that wait. This argument applies to work you encode in the current command encoder.

- `visibilityOptions` — [MTL4VisibilityOptions](../mtl4visibilityoptions.md) of the barrier.

## Discussion

Encode a barrier that guarantees that any subsequent work you encode in the current command encoder that corresponds to the `beforeStages` stages doesn’t proceed until Metal completes all work prior to the current command encoder corresponding to the `afterQueueStages` stages, completes.

Metal can reorder the exact point where it applies the barrier, so encode the barrier as close to the command that consumes the resource as possible. Don’t use this method for synchronizing resource access within the same pass.

If you need to synchronize work within a pass that you encode with an instance of a subclass of [MTLCommandEncoder](../mtlcommandencoder.md), use memory barriers instead. For subclasses of [MTL4CommandEncoder](../mtl4commandencoder.md), use encoder barriers.

You can specify `afterQueueStages` and `beforeStages` that contain [MTLStages](../mtlstages.md) unrelated to the current command encoder.
