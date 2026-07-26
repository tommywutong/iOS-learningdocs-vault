---
title: MTKModelIOVertexDescriptorFromMetalWithError
framework: MetalKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtkmodeliovertexdescriptorfrommetalwitherror
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmodeliovertexdescriptorfrommetalwitherror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmodeliovertexdescriptorfrommetalwitherror.json'
content_hash: 'sha256:350323b71823c256'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKModelIOVertexDescriptorFromMetalWithError

<sub>Function</sub>

Returns a partially converted Model I/O vertex descriptor, reporting any error that occurs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern MDLVertexDescriptor *MTKModelIOVertexDescriptorFromMetalWithError(MTLVertexDescriptor *metalDescriptor, NSError **error);
```

## Parameters

- `metalDescriptor` — A Metal vertex descriptor to convert from.

- `error` — A pointer to an [NSError](../foundation/nserror.md) object if an error occurred, or `nil` if conversion succeeded.

## Return Value

A Model I/O vertex descriptor object.

## Discussion

This function can only set vertex format, offset, buffer index, and stride information in the resulting MDLMutableVertexDescriptor object. It does not add any semantic information such as attribute names. Names must be set in the returned MDLMutableVertexDescriptor object before it can be applied to a Model I/O mesh.

## See Also

### Converting Between Model I/O and Metal Vertex Descriptors

- [MTKMetalVertexDescriptorFromModelIO](<mtkmetalvertexdescriptorfrommodelio(__).md>) — Returns a partially converted Metal vertex descriptor.
- [MTKMetalVertexDescriptorFromModelIOWithError](mtkmetalvertexdescriptorfrommodeliowitherror.md) — Returns a partially converted Metal vertex descriptor, reporting any error that occurs.
- [MTKModelIOVertexDescriptorFromMetal](<mtkmodeliovertexdescriptorfrommetal(__).md>) — Returns a partially converted Model I/O vertex descriptor.
