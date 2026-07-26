---
title: 'updateFence(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/updatefence(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/updatefence(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/updatefence%28_%3A%29.json'
content_hash: 'sha256:f90d29cefa6aef56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# updateFence(_:)

<sub>Instance Method</sub>

Encodes a command that instructs the GPU to update a fence after the compute pass completes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func updateFence(_ fence: any MTLFence)
```

## Parameters

- `fence` — A fence the pass updates after it completes.

## Discussion

You can synchronize memory operations of a compute pass that access resources with an [MTLFence](../mtlfence.md). This method instructs the pass to update `fence` after it runs all its memory store operations to the resources it accesses. The fence indicates when other passes can access those resources without a race condition.

For more information about synchronization with fences, see:

- [Resource synchronization](../resource-synchronization.md)
- [Synchronizing passes with a fence](../synchronizing-passes-with-a-fence.md)

### Reuse a fence by waiting first and updating second

When encoding a compute pass that reuses a fence, wait for other passes to update the fence before repurposing that fence to notify subsequent passes with an update:

1. Call the [- waitForFence:](<waitforfence(__).md>) method before encoding commands that need to wait for other passes.
2. Call the [- updateFence:](<updatefence(__).md>) method after encoding commands that later passes depend on.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [MTLCommandBuffer](../mtlcommandbuffer.md).

> [!warning] Warning
> Don’t update a fence and then wait for the same fence within a pass because it can create a GPU deadlock.

## See Also

### Preventing resource access conflicts

- [- waitForFence:](<waitforfence(__).md>) — Encodes a command that instructs the GPU to pause the compute pass until another pass updates a fence.
- [- memoryBarrierWithScope:](<memorybarrier(scope_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resource types.
- [memoryBarrier(resources:)](<memorybarrier(resources_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resources.
