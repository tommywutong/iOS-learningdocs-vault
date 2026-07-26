---
title: 'setRenderPipelineState(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setrenderpipelinestate(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setrenderpipelinestate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setrenderpipelinestate%28_%3A%29.json'
content_hash: 'sha256:a653815eed5b39a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setRenderPipelineState(_:)

<sub>Instance Method</sub>

Configures this encoder with a render pipeline state that applies to your subsequent draw commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setRenderPipelineState(_ pipelineState: any MTLRenderPipelineState)
```

## Parameters

- `pipelineState` — A non-`nil` [MTLRenderPipelineState](../mtlrenderpipelinestate.md) instance.
