---
title: 'barrier(afterStages:beforeQueueStages:visibilityOptions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandencoder/barrier(afterstages:beforequeuestages:visibilityoptions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandencoder/barrier(afterstages:beforequeuestages:visibilityoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandencoder/barrier%28afterstages%3Abeforequeuestages%3Avisibilityoptions%3A%29.json'
content_hash: 'sha256:6f775a07ae57ca62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandEncoder](../mtl4commandencoder.md)

# barrier(afterStages:beforeQueueStages:visibilityOptions:)

<sub>Instance Method</sub>

Encodes a producer barrier on work committed to the same command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func barrier(afterStages: MTLStages, beforeQueueStages: MTLStages, visibilityOptions: MTL4VisibilityOptions = [ .device ])
```

## Parameters

- `afterStages` — [MTLStages](../mtlstages.md) mask that represents the stages of work to wait for. This argument applies to work corresponding to these stages you encode in the current command encoder prior to this barrier command.

- `beforeQueueStages` — [MTLStages](../mtlstages.md) mask that represents the stages of work that need to wait. This argument applies to subsequent encoders and not to work in the current command encoder.

- `visibilityOptions` — [MTL4VisibilityOptions](../mtl4visibilityoptions.md) of the barrier, controlling cache flush behavior.

## Discussion

This method encodes a barrier that guarantees that any work you encode using _subsequent command encoders_, corresponding to `beforeQueueStages`, don’t begin until all commands you previously encode in the current encoder (and prior encoders), corresponding to `afterStages`, complete.

When calling this method, you can pass any [MTLStages](../mtlstages.md) to parameters `afterStages` and `beforeQueueStages`, even stages that don’t relate to the current or prior command encoders.
