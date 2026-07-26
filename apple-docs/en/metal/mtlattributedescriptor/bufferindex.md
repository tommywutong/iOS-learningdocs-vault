---
title: bufferIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlattributedescriptor/bufferindex
source_url: 'https://developer.apple.com/documentation/metal/mtlattributedescriptor/bufferindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattributedescriptor/bufferindex.json'
content_hash: 'sha256:13a8d929a235684c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAttributeDescriptor](../mtlattributedescriptor.md)

# bufferIndex

<sub>Instance Property</sub>

The index in the buffer argument table for the buffer that contains the data for this attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bufferIndex: Int { get set }
```

## See Also

### Defining attribute location

- [offset](offset.md) — The offset, in bytes, from the start of the buffer that contains the attribute data to the start of the data itself.
- [format](format.md) — The format of the attribute’s data.
- [MTLAttributeFormat](../mtlattributeformat.md) — The data format options for acceleration structures.
