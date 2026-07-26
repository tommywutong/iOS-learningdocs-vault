---
title: 'setAccelerationStructure(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setaccelerationstructure(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setaccelerationstructure(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setaccelerationstructure%28_%3Aindex%3A%29.json'
content_hash: 'sha256:fea988f557fabc44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setAccelerationStructure(_:index:)

<sub>Instance Method</sub>

Encodes a reference to an acceleration structure into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setAccelerationStructure(_ accelerationStructure: (any MTLAccelerationStructure)?, index: Int)
```

## Parameters

- `accelerationStructure` — An acceleration structure the method encodes.

- `index` — The index of an acceleration structure within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.
