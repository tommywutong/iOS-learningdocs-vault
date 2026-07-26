---
title: format
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlattributedescriptor/format
source_url: 'https://developer.apple.com/documentation/metal/mtlattributedescriptor/format'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattributedescriptor/format.json'
content_hash: 'sha256:b6c9d840b84a4ea5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAttributeDescriptor](../mtlattributedescriptor.md)

# format

<sub>Instance Property</sub>

The format of the attribute’s data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var format: MTLAttributeFormat { get set }
```

## See Also

### Defining attribute location

- [bufferIndex](bufferindex.md) — The index in the buffer argument table for the buffer that contains the data for this attribute.
- [offset](offset.md) — The offset, in bytes, from the start of the buffer that contains the attribute data to the start of the data itself.
- [MTLAttributeFormat](../mtlattributeformat.md) — The data format options for acceleration structures.
