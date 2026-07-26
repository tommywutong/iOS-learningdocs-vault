---
title: 'newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4archive/newcomputepipelinestatewithdescriptor:dynamiclinkingdescriptor:error:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4archive/newcomputepipelinestatewithdescriptor:dynamiclinkingdescriptor:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4archive/newcomputepipelinestatewithdescriptor%3Adynamiclinkingdescriptor%3Aerror%3A.json'
content_hash: 'sha256:2e10aba562cce45d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Archive](../mtl4archive.md)

# newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:

<sub>Instance Method</sub>

Creates a compute pipeline state from the archive with a compute descriptor and a dynamic linking descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTLComputePipelineState>) newComputePipelineStateWithDescriptor:(MTL4ComputePipelineDescriptor *) descriptor dynamicLinkingDescriptor:(MTL4PipelineStageDynamicLinkingDescriptor *) dynamicLinkingDescriptor error:(NSError **) error;
```

## Parameters

- `descriptor` — A compute pipeline descriptor.

- `dynamicLinkingDescriptor` — A descriptor that provides additional properties to link other functions with the pipeline.

- `error` — On return, if the method fails, a pointer to an error information instance; otherwise `nil`.

## Return Value

A compute pipeline state if the method succeeds, otherwise `nil`.

## See Also

### Creating compute pipeline states

- [newComputePipelineStateWithDescriptor:error:](newcomputepipelinestatewithdescriptor_error_.md) — Creates a compute pipeline state from the archive with a descriptor.
