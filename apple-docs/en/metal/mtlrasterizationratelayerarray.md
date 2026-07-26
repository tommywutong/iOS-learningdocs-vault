---
title: MTLRasterizationRateLayerArray
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratelayerarray
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerarray.json'
content_hash: 'sha256:b928c5c016098610'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRasterizationRateLayerArray

<sub>Class</sub>

Descriptions for the rasterization rates to apply to the set of layers in a rate map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLRasterizationRateLayerArray
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing members of the array

- [- objectAtIndexedSubscript:](<mtlrasterizationratelayerarray/subscript(__).md>) — Retrieves the sample value at the specified index.
- [MTLRasterizationRateLayerDescriptor](mtlrasterizationratelayerdescriptor.md) — The minimum rasterization rates to apply to sections of a layer in the render target.

## See Also

### Configuring the rate map layers

- [layerCount](mtlrasterizationratemapdescriptor/layercount.md) — The number of layers in the rate map.
- [- layerAtIndex:](<mtlrasterizationratemapdescriptor/layer(at_).md>) — Returns the layer description for a layer in the rate map.
- [- setLayer:atIndex:](<mtlrasterizationratemapdescriptor/setlayer(__at_).md>) — Sets a configuration for a layer rate map.
- [layers](mtlrasterizationratemapdescriptor/layers.md) — The rasterization rates for one or more layers in the rate map.
