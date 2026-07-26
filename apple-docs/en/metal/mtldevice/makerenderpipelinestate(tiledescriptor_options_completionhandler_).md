---
title: 'makeRenderPipelineState(tileDescriptor:options:completionHandler:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makerenderpipelinestate%28tiledescriptor%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:1e76a4c5c037241b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeRenderPipelineState(tileDescriptor:options:completionHandler:)

<sub>Instance Method</sub>

Asynchronously creates a tile shader’s render pipeline state and reflection information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(tileDescriptor descriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: @escaping @Sendable ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(tileDescriptor descriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) async throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

## Parameters

- `descriptor` — An [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

- `completionHandler` — A Swift closure or an Objective-C block the method calls when it finishes creating the render pipeline state.

## Default Implementations

### MTLDevice Implementations

- [makeRenderPipelineState(tileDescriptor:options:)](<makerenderpipelinestate(tiledescriptor_options_).md>) — Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.

## See Also

### Creating tile render pipeline states

- [makeRenderPipelineState(tileDescriptor:options:)](<makerenderpipelinestate(tiledescriptor_options_).md>) — Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.
- [- newRenderPipelineStateWithTileDescriptor:options:reflection:error:](<makerenderpipelinestate(tiledescriptor_options_reflection_).md>) — Synchronously creates a tile shader’s render pipeline state and reflection information.
