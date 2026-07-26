---
title: offset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlattributedescriptor/offset
source_url: 'https://developer.apple.com/documentation/metal/mtlattributedescriptor/offset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattributedescriptor/offset.json'
content_hash: 'sha256:017575beeabbe7d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAttributeDescriptor](../mtlattributedescriptor.md)

# offset

<sub>Instance Property</sub>

The offset, in bytes, from the start of the buffer that contains the attribute data to the start of the data itself.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var offset: Int { get set }
```

## Discussion

Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Defining attribute location

- [bufferIndex](bufferindex.md) — The index in the buffer argument table for the buffer that contains the data for this attribute.
- [format](format.md) — The format of the attribute’s data.
- [MTLAttributeFormat](../mtlattributeformat.md) — The data format options for acceleration structures.
