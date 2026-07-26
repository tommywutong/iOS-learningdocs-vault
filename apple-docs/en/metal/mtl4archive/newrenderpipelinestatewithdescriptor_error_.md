---
title: 'newRenderPipelineStateWithDescriptor:error:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4archive/newrenderpipelinestatewithdescriptor:error:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4archive/newrenderpipelinestatewithdescriptor:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4archive/newrenderpipelinestatewithdescriptor%3Aerror%3A.json'
content_hash: 'sha256:101820327d38deb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Archive](../mtl4archive.md)

# newRenderPipelineStateWithDescriptor:error:

<sub>Instance Method</sub>

Creates a render pipeline state from the archive with a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTLRenderPipelineState>) newRenderPipelineStateWithDescriptor:(MTL4PipelineDescriptor *) descriptor error:(NSError **) error;
```

## Parameters

- `descriptor` — A render pipeline descriptor.

- `error` — On return, if the method fails, a pointer to an error information instance; otherwise `nil`.

## Return Value

A render pipeline state if the method succeeds, otherwise `nil`.

## Discussion

You create any kind of render pipeline states with this method, including:

- Traditional render pipelines
- Mesh render pipelines
- Tile render pipelines

## See Also

### Creating render pipeline states

- [newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:](newrenderpipelinestatewithdescriptor_dynamiclinkingdescriptor_error_.md) — Creates a render pipeline state from the archive with a render descriptor and a dynamic linking descriptor.
