---
title: 'newRenderPipelineStateWithMeshDescriptor:options:reflection:error:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/newrenderpipelinestatewithmeshdescriptor:options:reflection:error:'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/newrenderpipelinestatewithmeshdescriptor:options:reflection:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/newrenderpipelinestatewithmeshdescriptor%3Aoptions%3Areflection%3Aerror%3A.json'
content_hash: 'sha256:4a7b3ac218ceb9a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# newRenderPipelineStateWithMeshDescriptor:options:reflection:error:

<sub>Instance Method</sub>

Synchronously creates a mesh render pipeline state and reflection information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTLRenderPipelineState>) newRenderPipelineStateWithMeshDescriptor:(MTLMeshRenderPipelineDescriptor *) descriptor options:(MTLPipelineOption) options reflection:(MTLAutoreleasedRenderPipelineReflection*) reflection error:(NSError **) error;
```

## Parameters

- `descriptor` — An [MTLMeshRenderPipelineDescriptor](../mtlmeshrenderpipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

- `reflection` — In Swift, an optional pointer to an [MTLAutoreleasedRenderPipelineReflection](../mtlautoreleasedrenderpipelinereflection.md) optional. In Objective-C, a pointer to an [MTLAutoreleasedRenderPipelineReflection](../mtlautoreleasedrenderpipelinereflection.md) instance. Pass `nil` in either language when you don’t need reflection data. Otherwise on return, if the method completes successfully, it assigns an [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md) instance to the pointee, which contains the details about the function arguments.

- `error` — On return, if an error occurs, a pointer to an error information instance; otherwise, `nil`.

## Return Value

A new [MTLRenderPipelineState](../mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise, `nil`.

## Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [- setRenderPipelineState:](<../mtlrendercommandencoder/setrenderpipelinestate(__).md>) method of an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instance.

## See Also

### Creating render pipeline states with mesh shaders

- [- newRenderPipelineStateWithMeshDescriptor:options:completionHandler:](<makerenderpipelinestate(descriptor_options_completionhandler_)-1wvya.md>) — Asynchronously creates a mesh render pipeline state and reflection information.
