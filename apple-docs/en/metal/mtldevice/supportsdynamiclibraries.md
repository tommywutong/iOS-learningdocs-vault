---
title: supportsDynamicLibraries
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/supportsdynamiclibraries
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportsdynamiclibraries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportsdynamiclibraries.json'
content_hash: 'sha256:8eaa15fa95ef7994'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsDynamicLibraries

<sub>Instance Property</sub>

A Boolean value that indicates whether the GPU device can create and use dynamic libraries in compute pipelines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportsDynamicLibraries: Bool { get }
```

## See Also

### Creating dynamic shader libraries

- [supportsRenderDynamicLibraries](supportsrenderdynamiclibraries.md) — A Boolean value that indicates whether the GPU device can create and use dynamic libraries in render pipelines.
- [- newDynamicLibrary:error:](<makedynamiclibrary(library_).md>) — Creates a Metal dynamic library instance from a Metal library instance.
- [- newDynamicLibraryWithURL:error:](<makedynamiclibrary(url_).md>) — Creates a Metal dynamic library instance that contains the functions in the Metal library file at a URL.
- [Code](../mtldynamiclibraryerror-swift.struct/code.md) — Error codes that Metal can generate when creating dynamic libraries.
- [MTLDynamicLibraryDomain](../mtldynamiclibrarydomain.md) — The domain for Metal dynamic library errors.
