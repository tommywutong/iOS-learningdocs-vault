---
title: MTKMetalVertexDescriptorFromModelIOWithError
framework: MetalKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtkmetalvertexdescriptorfrommodeliowitherror
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmetalvertexdescriptorfrommodeliowitherror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmetalvertexdescriptorfrommodeliowitherror.json'
content_hash: 'sha256:e9607b7596a55edc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKMetalVertexDescriptorFromModelIOWithError

<sub>Function</sub>

Returns a partially converted Metal vertex descriptor, reporting any error that occurs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern MTLVertexDescriptor *MTKMetalVertexDescriptorFromModelIOWithError(MDLVertexDescriptor *modelIODescriptor, NSError **error);
```

## Parameters

- `modelIODescriptor` — A Model I/O vertex descriptor to convert from.

- `error` — A pointer to an [NSError](../foundation/nserror.md) object if an error occurred, or `nil` if conversion succeeded.

## Return Value

A Metal vertex descriptor object.

## Discussion

This function can only set vertex format, offset, buffer index, and stride information in the resulting [MTLVertexDescriptor](../metal/mtlvertexdescriptor.md) object. The function copies attributes one-for-one, so it is up to you to properly arrange the MDLMutableVertexDescriptor attributes in the correct order so that the resulting [MTLVertexDescriptor](../metal/mtlvertexdescriptor.md) object can properly map mesh data to vertex shader inputs. Layout [stepFunction](../metal/mtlvertexbufferlayoutdescriptor/stepfunction.md) and [stepRate](../metal/mtlvertexbufferlayoutdescriptor/steprate.md) values for the resulting [MTLVertexDescriptor](../metal/mtlvertexdescriptor.md) object must also be set by your application.

## See Also

### Converting Between Model I/O and Metal Vertex Descriptors

- [MTKMetalVertexDescriptorFromModelIO](<mtkmetalvertexdescriptorfrommodelio(__).md>) — Returns a partially converted Metal vertex descriptor.
- [MTKModelIOVertexDescriptorFromMetal](<mtkmodeliovertexdescriptorfrommetal(__).md>) — Returns a partially converted Model I/O vertex descriptor.
- [MTKModelIOVertexDescriptorFromMetalWithError](mtkmodeliovertexdescriptorfrommetalwitherror.md) — Returns a partially converted Model I/O vertex descriptor, reporting any error that occurs.
