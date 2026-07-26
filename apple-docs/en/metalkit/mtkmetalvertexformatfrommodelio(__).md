---
title: 'MTKMetalVertexFormatFromModelIO(_:)'
framework: MetalKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metalkit/mtkmetalvertexformatfrommodelio(_:)'
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmetalvertexformatfrommodelio(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmetalvertexformatfrommodelio%28_%3A%29.json'
content_hash: 'sha256:e2c658da52085c96'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKMetalVertexFormatFromModelIO(_:)

<sub>Function</sub>

Returns a converted Metal vertex format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTKMetalVertexFormatFromModelIO(_ vertexFormat: MDLVertexFormat) -> MTLVertexFormat
```

## Parameters

- `vertexFormat` — A Model I/O vertex format to convert from.

## Return Value

A Metal vertex format value.

## Discussion

This function returns [MTLVertexFormat.invalid](../metal/mtlvertexformat/invalid.md) if no matching [MTLVertexFormat](../metal/mtlvertexformat.md) exists.

## See Also

### Converting Between Model I/O and Metal Vertex Formats

- [MTKModelIOVertexFormatFromMetal](<mtkmodeliovertexformatfrommetal(__).md>) — Returns a converted Model I/O vertex format.
