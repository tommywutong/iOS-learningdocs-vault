---
title: parameterDataSizeAndAlign
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemap/parameterdatasizeandalign
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap/parameterdatasizeandalign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap/parameterdatasizeandalign.json'
content_hash: 'sha256:2548b78d573bb8e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMap](../mtlrasterizationratemap.md)

# parameterDataSizeAndAlign

<sub>Instance Property</sub>

The size and alignment requirements to contain the coordinate transformation information in this rate map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var parameterDataSizeAndAlign: MTLSizeAndAlign { get }
```

## Discussion

To convert coordinate values inside your shader, pass the rate map data into the shader in an [MTLBuffer](../mtlbuffer.md) instance. The buffer location where you store the parameter information needs at least the size and alignment this property provides.

You can convert between screen space and physical fragment space by binding the buffer to the shader with type `rasterization_rate_map_data`, then constructing `rasterization_rate_map_decoder` with the buffer data. For more details, see the “Variable Rasterization Rate” section of the [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## See Also

### Obtaining coordinate transformation data

- [- copyParameterDataToBuffer:offset:](<copyparameterdata(buffer_offset_).md>) — Copies the parameter data into the provided buffer.
