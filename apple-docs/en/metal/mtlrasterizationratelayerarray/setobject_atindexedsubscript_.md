---
title: 'setObject:atIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratelayerarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:467455010f71db66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateLayerArray](../mtlrasterizationratelayerarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Stores a sample value at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLRasterizationRateLayerDescriptor *) layer atIndexedSubscript:(NSUInteger) layerIndex;
```

## Parameters

- `layer` — The layer descriptor to set

- `layerIndex` — The index of the sample you want to set.

## Discussion

The method converts the value to a single precision floating point value.

## See Also

### Accessing members of the array

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Retrieves the sample value at the specified index.
- [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md) — The minimum rasterization rates to apply to sections of a layer in the render target.
