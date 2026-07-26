---
title: instanceDescriptorType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptortype
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptortype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptortype.json'
content_hash: 'sha256:fb0d324b36d78e23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4IndirectInstanceAccelerationStructureDescriptor](../mtl4indirectinstanceaccelerationstructuredescriptor.md)

# instanceDescriptorType

<sub>Instance Property</sub>

Controls the type of instance descriptor that the instance descriptor buffer references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType { get set }
```

## Discussion

This value determines the layout Metal expects for the structs the instance descriptor buffer contains.

Defaults to `MTLAccelerationStructureInstanceDescriptorTypeIndirect`. Valid values for this property are `MTLAccelerationStructureInstanceDescriptorTypeIndirect` or `MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion`.
