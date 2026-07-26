---
title: instanceDescriptorStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4instanceaccelerationstructuredescriptor/instancedescriptorstride
source_url: 'https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor/instancedescriptorstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4instanceaccelerationstructuredescriptor/instancedescriptorstride.json'
content_hash: 'sha256:5d14c361fdfa4aab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4InstanceAccelerationStructureDescriptor](../mtl4instanceaccelerationstructuredescriptor.md)

# instanceDescriptorStride

<sub>Instance Property</sub>

Sets the stride, in bytes, between instance descriptors the instance descriptor buffer references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceDescriptorStride: Int { get set }
```

## Discussion

You are responsible for ensuring this stride is at least the size of the structure type corresponding to the instance descriptor type and a multiple of 4 bytes.

Defaults to `0`, indicating the instance descriptors are tightly packed.
