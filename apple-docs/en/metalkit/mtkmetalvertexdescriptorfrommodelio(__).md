---
title: 'MTKMetalVertexDescriptorFromModelIO(_:)'
framework: MetalKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metalkit/mtkmetalvertexdescriptorfrommodelio(_:)'
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmetalvertexdescriptorfrommodelio(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmetalvertexdescriptorfrommodelio%28_%3A%29.json'
content_hash: 'sha256:5aa9e4f522b3cf5b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKMetalVertexDescriptorFromModelIO(_:)

<sub>Function</sub>

Returns a partially converted Metal vertex descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTKMetalVertexDescriptorFromModelIO(_ modelIODescriptor: MDLVertexDescriptor) -> MTLVertexDescriptor?
```

## Return Value

A Metal vertex descriptor object.

## Discussion

This function is equivalent to the [MTKMetalVertexDescriptorFromModelIOWithError](mtkmetalvertexdescriptorfrommodeliowitherror.md) function, but does not report errors.

## See Also

### Converting Between Model I/O and Metal Vertex Descriptors

- [MTKModelIOVertexDescriptorFromMetal](<mtkmodeliovertexdescriptorfrommetal(__).md>) — Returns a partially converted Model I/O vertex descriptor.
