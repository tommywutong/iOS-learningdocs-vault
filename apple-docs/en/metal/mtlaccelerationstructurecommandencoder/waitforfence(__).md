---
title: 'waitForFence(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/waitforfence(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/waitforfence(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/waitforfence%28_%3A%29.json'
content_hash: 'sha256:43652bbc74ef3b5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# waitForFence(_:)

<sub>Instance Method</sub>

Encodes a command that instructs the GPU to pause the acceleration structure pass until another pass updates a fence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func waitForFence(_ fence: any MTLFence)
```

## Parameters

- `fence` — A fence that the pass waits for before it runs any of its commands.

## Discussion

You can synchronize memory operations of an acceleration structure pass that access resources with an [MTLFence](../mtlfence.md). This method instructs the GPU to wait until another pass updates `fence` before running the acceleration structure pass. The fence indicates when the pass can access those resources without a race condition.

For more information about synchronization with fences, see:

- [Resource synchronization](../resource-synchronization.md)
- [Synchronizing passes with a fence](../synchronizing-passes-with-a-fence.md)

### Reuse a fence by waiting first and updating second

When encoding an acceleration structure pass that reuses a fence, wait for other passes to update the fence before repurposing that fence to notify subsequent passes with an update:

1. Call the [- waitForFence:](<waitforfence(__).md>) method before encoding commands that need to wait for other passes.
2. Call the [- updateFence:](<updatefence(__).md>) method after encoding commands that later passes depend on.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [MTLCommandBuffer](../mtlcommandbuffer.md).

> [!warning] Warning
> Don’t update a fence and then wait for the same fence within a pass because it can create a GPU deadlock.

## See Also

### Preventing resource access conflicts

- [- updateFence:](<updatefence(__).md>) — Encodes a command that instructs the GPU to update a fence after the acceleration structure pass completes.
