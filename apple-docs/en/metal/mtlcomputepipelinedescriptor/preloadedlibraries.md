---
title: preloadedLibraries
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinedescriptor/preloadedlibraries
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/preloadedlibraries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinedescriptor/preloadedlibraries.json'
content_hash: 'sha256:826f7b0bfc71ee9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md)

# preloadedLibraries

<sub>Instance Property</sub>

The dynamic libraries that contain precompiled shader functions you want to link.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preloadedLibraries: [any MTLDynamicLibrary] { get set }
```

## See Also

### Loading dynamic libraries to link at runtime

- [insertLibraries](insertlibraries.md) — The dynamic libraries that contain precompiled shader functions you want to link. _(deprecated)_
