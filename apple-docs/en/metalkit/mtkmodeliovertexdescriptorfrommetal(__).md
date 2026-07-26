---
title: 'MTKModelIOVertexDescriptorFromMetal(_:)'
framework: MetalKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metalkit/mtkmodeliovertexdescriptorfrommetal(_:)'
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmodeliovertexdescriptorfrommetal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmodeliovertexdescriptorfrommetal%28_%3A%29.json'
content_hash: 'sha256:2f5f50095f8d83a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKModelIOVertexDescriptorFromMetal(_:)

<sub>Function</sub>

Returns a partially converted Model I/O vertex descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTKModelIOVertexDescriptorFromMetal(_ metalDescriptor: MTLVertexDescriptor) -> MDLVertexDescriptor
```

## Parameters

- `metalDescriptor` — A Metal vertex descriptor to convert from.

## Return Value

A Model I/O vertex descriptor object.

## Discussion

This function is equivalent to the [MTKModelIOVertexDescriptorFromMetalWithError](mtkmodeliovertexdescriptorfrommetalwitherror.md) function, but does not report errors.

## See Also

### Converting Between Model I/O and Metal Vertex Descriptors

- [MTKMetalVertexDescriptorFromModelIO](<mtkmetalvertexdescriptorfrommodelio(__).md>) — Returns a partially converted Metal vertex descriptor.
