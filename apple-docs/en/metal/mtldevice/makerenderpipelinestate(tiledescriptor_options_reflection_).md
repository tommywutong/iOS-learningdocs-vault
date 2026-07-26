---
title: 'makeRenderPipelineState(tileDescriptor:options:reflection:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:reflection:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:reflection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makerenderpipelinestate%28tiledescriptor%3Aoptions%3Areflection%3A%29.json'
content_hash: 'sha256:14d46c73ca3dbc78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeRenderPipelineState(tileDescriptor:options:reflection:)

<sub>Instance Method</sub>

Synchronously creates a tile shader’s render pipeline state and reflection information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(tileDescriptor descriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState
```

## Parameters

- `descriptor` — An [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

- `reflection` — In Swift, an optional pointer to an [MTLAutoreleasedRenderPipelineReflection](../mtlautoreleasedrenderpipelinereflection.md) optional. In Objective-C, a pointer to an [MTLAutoreleasedRenderPipelineReflection](../mtlautoreleasedrenderpipelinereflection.md) instance. Pass `nil` in either language when you don’t need reflection data. Otherwise on return, if the method completes successfully, it assigns an [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md) instance to the pointee, which contains the details about the function arguments.

## Return Value

A new [MTLRenderPipelineState](../mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## See Also

### Creating tile render pipeline states

- [makeRenderPipelineState(tileDescriptor:options:)](<makerenderpipelinestate(tiledescriptor_options_).md>) — Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.
- [- newRenderPipelineStateWithTileDescriptor:options:completionHandler:](<makerenderpipelinestate(tiledescriptor_options_completionhandler_).md>) — Asynchronously creates a tile shader’s render pipeline state and reflection information.
