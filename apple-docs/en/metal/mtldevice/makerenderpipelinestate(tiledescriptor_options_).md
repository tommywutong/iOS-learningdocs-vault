---
title: 'makeRenderPipelineState(tileDescriptor:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makerenderpipelinestate%28tiledescriptor%3Aoptions%3A%29.json'
content_hash: 'sha256:ccfe573e44955217'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeRenderPipelineState(tileDescriptor:options:)

<sub>Instance Method</sub>

Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

## Parameters

- `tileDescriptor` — An [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

## Return Value

A tuple with a new [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md) instance and an [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md) optional instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## See Also

### Creating tile render pipeline states

- [- newRenderPipelineStateWithTileDescriptor:options:reflection:error:](<makerenderpipelinestate(tiledescriptor_options_reflection_).md>) — Synchronously creates a tile shader’s render pipeline state and reflection information.
- [- newRenderPipelineStateWithTileDescriptor:options:completionHandler:](<makerenderpipelinestate(tiledescriptor_options_completionhandler_).md>) — Asynchronously creates a tile shader’s render pipeline state and reflection information.
