---
title: 'setVertexIntersectionFunctionTable(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertexintersectionfunctiontable(_:bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexintersectionfunctiontable(_:bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertexintersectionfunctiontable%28_%3Abufferindex%3A%29.json'
content_hash: 'sha256:224fc9aacc09b52a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexIntersectionFunctionTable(_:bufferIndex:)

<sub>Instance Method</sub>

Assigns an intersection function table to an entry in the vertex shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexIntersectionFunctionTable(_ intersectionFunctionTable: (any MTLIntersectionFunctionTable)?, bufferIndex: Int)
```

## Parameters

- `intersectionFunctionTable` — An [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md) instance the command assigns to an entry in the vertex shader argument table for intersection function tables.

- `bufferIndex` — An integer that represents the entry in the vertex shader argument table for intersection function tables that stores a record of `intersectionFunctionTable`.

## Discussion

By default, the intersection function table at each index is `nil`.

## See Also

### Assigning intersection function tables

- [setVertexIntersectionFunctionTables(_:bufferRange:)](<setvertexintersectionfunctiontables(__bufferrange_).md>) — Assigns multiple intersection function tables to a range of entries in the vertex shader argument table.
