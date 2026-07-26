---
title: instanceDescriptorBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.json'
content_hash: 'sha256:eec346c6a118fd37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4IndirectInstanceAccelerationStructureDescriptor](../mtl4indirectinstanceaccelerationstructuredescriptor.md)

# instanceDescriptorBuffer

<sub>Instance Property</sub>

Assigns a reference to a buffer containing instance descriptors for acceleration structures to reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceDescriptorBuffer: MTL4BufferRange { get set }
```

## Discussion

This buffer conceptually represents an array of instance data. The specific format for the structs that comprise each entry depends on the value of the  [instanceDescriptorType](instancedescriptortype.md) property.

You are responsible for ensuring the buffer address the range contains is not zero.
