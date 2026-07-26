---
title: libraryType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcompileoptions/librarytype
source_url: 'https://developer.apple.com/documentation/metal/mtlcompileoptions/librarytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcompileoptions/librarytype.json'
content_hash: 'sha256:41af5644b78294b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCompileOptions](../mtlcompileoptions.md)

# libraryType

<sub>Instance Property</sub>

The kind of library to create.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var libraryType: MTLLibraryType { get set }
```

## Discussion

The default value is [MTLLibraryTypeExecutable](../mtllibrarytype/executable.md).

## See Also

### Configuring the library output options

- [installName](installname.md) — For a dynamic library, the name to use when installing the library.
