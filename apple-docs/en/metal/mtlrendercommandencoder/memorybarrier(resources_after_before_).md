---
title: 'memoryBarrier(resources:after:before:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/memorybarrier(resources:after:before:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/memorybarrier(resources:after:before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/memorybarrier%28resources%3Aafter%3Abefore%3A%29.json'
content_hash: 'sha256:15883f4562ac9ca7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# memoryBarrier(resources:after:before:)

<sub>Instance Method</sub>

Creates a memory barrier that enforces the order of write and read operations for specific resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func memoryBarrier(resources: [any MTLResource], after: MTLRenderStages, before: MTLRenderStages)
```

## Parameters

- `resources` — An array of [MTLResource](../mtlresource.md) instances the barrier applies to.

- `after` — The render stages of previous draw commands that modify `resources`.

- `before` — The render stages of subsequent draw commands that read or modify `resources`.

## Discussion

Memory barriers ensure the relevant stages of prior draw commands finish modifying resources before starting the stages of subsequent commands that depend on those resources.

To determine whether a GPU supports memory barriers, see the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

## See Also

### Preventing resource access conflicts

- [- waitForFence:beforeStages:](<waitforfence(__before_).md>) — Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.
- [- updateFence:afterStages:](<updatefence(__after_).md>) — Encodes a command that instructs the GPU to update a fence after one or more stages, which can unblock other passes waiting for the fence.
- [- memoryBarrierWithScope:afterStages:beforeStages:](<memorybarrier(scope_after_before_).md>) — Creates a memory barrier that enforces the order of write and read operations for specific resource types.
