---
title: supportAttributeStrides
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4argumenttabledescriptor/supportattributestrides
source_url: 'https://developer.apple.com/documentation/metal/mtl4argumenttabledescriptor/supportattributestrides'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4argumenttabledescriptor/supportattributestrides.json'
content_hash: 'sha256:b7873ef6dc2a1baf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ArgumentTableDescriptor](../mtl4argumenttabledescriptor.md)

# supportAttributeStrides

<sub>Instance Property</sub>

Controls whether Metal should reserve memory for attribute strides in the argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportAttributeStrides: Bool { get set }
```

## Discussion

Set this value to true if you intend to provide dynamic attribute strides when binding vertex array buffers to the argument table by calling [- setAddress:attributeStride:atIndex:](<../mtl4argumenttable/setaddress(__attributestride_index_).md>)

The default value of this property is [false](../../swift/false.md).
