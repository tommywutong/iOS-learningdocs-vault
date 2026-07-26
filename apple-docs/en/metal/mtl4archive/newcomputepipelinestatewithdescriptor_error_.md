---
title: 'newComputePipelineStateWithDescriptor:error:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4archive/newcomputepipelinestatewithdescriptor:error:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4archive/newcomputepipelinestatewithdescriptor:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4archive/newcomputepipelinestatewithdescriptor%3Aerror%3A.json'
content_hash: 'sha256:9a25c0e47f5ef7dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Archive](../mtl4archive.md)

# newComputePipelineStateWithDescriptor:error:

<sub>Instance Method</sub>

Creates a compute pipeline state from the archive with a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTLComputePipelineState>) newComputePipelineStateWithDescriptor:(MTL4ComputePipelineDescriptor *) descriptor error:(NSError **) error;
```

## Parameters

- `descriptor` — A compute pipeline descriptor.

- `error` — On return, if the method fails, a pointer to an error information instance; otherwise `nil`.

## Return Value

A compute pipeline state if the method succeeds, otherwise `nil`.

## See Also

### Creating compute pipeline states

- [newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:](newcomputepipelinestatewithdescriptor_dynamiclinkingdescriptor_error_.md) — Creates a compute pipeline state from the archive with a compute descriptor and a dynamic linking descriptor.
