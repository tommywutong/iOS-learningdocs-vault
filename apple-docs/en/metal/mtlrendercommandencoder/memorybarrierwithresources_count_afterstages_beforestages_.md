---
title: 'memoryBarrierWithResources:count:afterStages:beforeStages:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/memorybarrierwithresources:count:afterstages:beforestages:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/memorybarrierwithresources:count:afterstages:beforestages:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/memorybarrierwithresources%3Acount%3Aafterstages%3Abeforestages%3A.json'
content_hash: 'sha256:b64198ba81410d69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# memoryBarrierWithResources:count:afterStages:beforeStages:

<sub>Instance Method</sub>

Creates a memory barrier that enforces the order of write and read operations for specific resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) memoryBarrierWithResources:(id<MTLResource> const[]) resources count:(NSUInteger) count afterStages:(MTLRenderStages) after beforeStages:(MTLRenderStages) before;
```

## Parameters

- `resources` — A C array of [MTLResource](../mtlresource.md) instances the barrier applies to.

- `count` — The number of elements in the resources array.

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
