---
title: 'MTKModelIOVertexFormatFromMetal(_:)'
framework: MetalKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metalkit/mtkmodeliovertexformatfrommetal(_:)'
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmodeliovertexformatfrommetal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmodeliovertexformatfrommetal%28_%3A%29.json'
content_hash: 'sha256:b7b63c169cc6d745'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKModelIOVertexFormatFromMetal(_:)

<sub>Function</sub>

Returns a converted Model I/O vertex format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTKModelIOVertexFormatFromMetal(_ vertexFormat: MTLVertexFormat) -> MDLVertexFormat
```

## Parameters

- `vertexFormat` — A Metal vertex format to convert from.

## Return Value

A Model I/O vertex format value.

## Discussion

This function returns [MDLVertexFormat.invalid](../modelio/mdlvertexformat/invalid.md) if no matching [MDLVertexFormat](../modelio/mdlvertexformat.md) exists.

## See Also

### Converting Between Model I/O and Metal Vertex Formats

- [MTKMetalVertexFormatFromModelIO](<mtkmetalvertexformatfrommodelio(__).md>) — Returns a converted Metal vertex format.
