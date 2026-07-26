---
title: insertLibraries
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（15.0 起废弃）, iPadOS 14.0+（15.0 起废弃）, Mac Catalyst 14.0+（15.0 起废弃）, macOS 11.0+（12.0 起废弃）, tvOS 14.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlcomputepipelinedescriptor/insertlibraries
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/insertlibraries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinedescriptor/insertlibraries.json'
content_hash: 'sha256:c4d91dca94544726'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md)

# insertLibraries

<sub>Instance Property</sub>

The dynamic libraries that contain precompiled shader functions you want to link.

> [!warning] Deprecated
> Use the [preloadedLibraries](preloadedlibraries.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var insertLibraries: [any MTLDynamicLibrary]? { get set }
```

## See Also

### Loading dynamic libraries to link at runtime

- [preloadedLibraries](preloadedlibraries.md) — The dynamic libraries that contain precompiled shader functions you want to link.
