---
title: 'updateFence(_:after:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/updatefence(_:after:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/updatefence(_:after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/updatefence%28_%3Aafter%3A%29.json'
content_hash: 'sha256:4b42752cfe407b31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# updateFence(_:after:)

<sub>Instance Method</sub>

Encodes a command that instructs the GPU to update a fence after one or more stages, which can unblock other passes waiting for the fence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func updateFence(_ fence: any MTLFence, after stages: MTLRenderStages)
```

## Parameters

- `fence` — A fence the pass updates after the stages in `stages` complete.

- `stages` — The render stages that need to complete before the pass updates `fence`.

## Discussion

You can synchronize memory operations of a render pass that access resources with an [MTLFence](../mtlfence.md). This method instructs the pass to update `fence` after the stages you pass to the `stages` run all their memory store operations to the resources it accesses. The fence indicates when other passes can access those resources without a race condition.

For more information about synchronization with fences, see:

- [Resource synchronization](../resource-synchronization.md)
- [Synchronizing passes with a fence](../synchronizing-passes-with-a-fence.md)

### Reuse a fence by waiting first and updating second

When encoding a render pass that reuses a fence, wait for other passes to update the fence before repurposing that fence to notify subsequent passes with an update:

1. Call the [- waitForFence:beforeStages:](<waitforfence(__before_).md>) method before encoding commands that need to wait for other passes.
2. Call the [- updateFence:afterStages:](<updatefence(__after_).md>) method after encoding commands that later passes depend on.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [MTLCommandBuffer](../mtlcommandbuffer.md).

> [!warning] Warning
> Don’t update a fence and then wait for the same fence within a pass because it can create a GPU deadlock.

To synchronize different stages within a single pass, create an _intrapass barrier_ because a fence can only synchronize memory operations between different passes. For more information, see [Synchronizing stages within a pass](../synchronizing-stages-within-a-pass.md).

## See Also

### Preventing resource access conflicts

- [- waitForFence:beforeStages:](<waitforfence(__before_).md>) — Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.
- [memoryBarrier(resources:after:before:)](<memorybarrier(resources_after_before_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resources.
- [- memoryBarrierWithScope:afterStages:beforeStages:](<memorybarrier(scope_after_before_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resource types.
