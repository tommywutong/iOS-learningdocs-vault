---
title: textureBarrier()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.11+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlrendercommandencoder/texturebarrier()
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/texturebarrier()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/texturebarrier%28%29.json'
content_hash: 'sha256:4c81c435cd25a4e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# textureBarrier()

<sub>Instance Method</sub>

Adds a barrier, which forces any texture read operations to wait until write operations to the same texture finish.

> [!warning] Deprecated
> Call [- memoryBarrierWithScope:afterStages:beforeStages:](<memorybarrier(scope_after_before_).md>) instead.

<sub>macOS</sub>

```swift
func textureBarrier()
```

## Discussion

Use a barrier if you use the same texture for both an input to a shader and as a rendering destination for the render pass.

A barrier let’s your app safely write to and then correctly read from the same texture. The barrier ensures that the draw calls before the barrier finish their write operations before any draw calls after the barrier read from the texture.

## See Also

### Deprecated methods

- [- useResource:usage:](<useresource(__usage_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to a resource. _(deprecated)_
- [use(_:usage:stages:)](<use(__usage_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to a resource. _(deprecated)_
- [useResources(_:usage:)](<useresources(__usage_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources. _(deprecated)_
- [use(_:count:usage:stages:)](<use(__count_usage_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources. _(deprecated)_
- [- useHeap:](<useheap(__).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap. _(deprecated)_
- [use(_:stages:)](<use(__stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap. _(deprecated)_
- [useHeaps(_:)](<useheaps(__).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps. _(deprecated)_
- [use(_:count:stages:)](<use(__count_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps. _(deprecated)_
