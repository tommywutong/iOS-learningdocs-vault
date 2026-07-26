---
title: 'copyParameterData(buffer:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemap/copyparameterdata(buffer:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap/copyparameterdata(buffer:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap/copyparameterdata%28buffer%3Aoffset%3A%29.json'
content_hash: 'sha256:13266a4285917bf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMap](../mtlrasterizationratemap.md)

# copyParameterData(buffer:offset:)

<sub>Instance Method</sub>

Copies the parameter data into the provided buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyParameterData(buffer: any MTLBuffer, offset: Int)
```

## Parameters

- `buffer` — The buffer instance to copy the data into. It needs to have an [MTLStorageModeShared](../mtlstoragemode/shared.md) storage mode, and there needs to be enough room in the buffer to store the data.

- `offset` — The location in the buffer to copy the data to. The offset needs to be a multiple of the parameter alignment.

## Discussion

To convert coordinate values inside your shader, pass the rate map data into the shader in an [MTLBuffer](../mtlbuffer.md) instance. The [parameterBufferSizeAndAlign](parameterdatasizeandalign.md) property provides the size and alignment requirements for the buffer.

You can convert between screen space and physical fragment space by binding the buffer to the shader with type `rasterization_rate_map_data`, then constructing `rasterization_rate_map_decoder` with the buffer data. For more details, see the “Variable Rasterization Rate” section of the [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## See Also

### Obtaining coordinate transformation data

- [parameterBufferSizeAndAlign](parameterdatasizeandalign.md) — The size and alignment requirements to contain the coordinate transformation information in this rate map.
