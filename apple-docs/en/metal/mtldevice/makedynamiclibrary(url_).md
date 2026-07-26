---
title: 'makeDynamicLibrary(url:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makedynamiclibrary(url:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makedynamiclibrary(url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makedynamiclibrary%28url%3A%29.json'
content_hash: 'sha256:f7534e20198ea9e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeDynamicLibrary(url:)

<sub>Instance Method</sub>

Creates a Metal dynamic library instance that contains the functions in the Metal library file at a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeDynamicLibrary(url: URL) throws -> any MTLDynamicLibrary
```

## Parameters

- `url` — A URL to a Metal library file (ending in `.metallib`).

## Return Value

A new [MTLDynamicLibrary](../mtldynamiclibrary.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## See Also

### Creating dynamic shader libraries

- [supportsDynamicLibraries](supportsdynamiclibraries.md) — A Boolean value that indicates whether the GPU device can create and use dynamic libraries in compute pipelines.
- [supportsRenderDynamicLibraries](supportsrenderdynamiclibraries.md) — A Boolean value that indicates whether the GPU device can create and use dynamic libraries in render pipelines.
- [- newDynamicLibrary:error:](<makedynamiclibrary(library_).md>) — Creates a Metal dynamic library instance from a Metal library instance.
- [Code](../mtldynamiclibraryerror-swift.struct/code.md) — Error codes that Metal can generate when creating dynamic libraries.
- [MTLDynamicLibraryDomain](../mtldynamiclibrarydomain.md) — The domain for Metal dynamic library errors.
