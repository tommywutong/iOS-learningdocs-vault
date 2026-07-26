---
title: MTLDynamicLibrary
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldynamiclibrary
source_url: 'https://developer.apple.com/documentation/metal/mtldynamiclibrary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldynamiclibrary.json'
content_hash: 'sha256:1aa46d4f775628c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDynamicLibrary

<sub>Protocol</sub>

A dynamically linkable representation of compiled shader code for a specific Metal device object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLDynamicLibrary : NSObjectProtocol, Sendable
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the library

- [device](mtldynamiclibrary/device.md) — The Metal device object that created the dynamic library.
- [installName](mtldynamiclibrary/installname.md) — A file path for this dynamic library.
- [label](mtldynamiclibrary/label.md) — A string that identifies the library.

### Saving a dynamic library to a file

- [- serializeToURL:error:](<mtldynamiclibrary/serialize(to_).md>) — Writes the contents of the dynamic library to a file.

## See Also

### Shader library management

- [MTLLibrary](mtllibrary.md) — A collection of Metal shader functions.
- [MTLBinaryArchive](mtlbinaryarchive.md) — A container for pipeline state descriptors and their associated compiled shader code.
- [MTLCompileOptions](mtlcompileoptions.md) — Compilation settings for a Metal shader library.
- [MTLLibraryType](mtllibrarytype.md) — A set of options for Metal library types.
- [MTLLanguageVersion](mtllanguageversion.md) — Metal shading language versions.
- [MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md) — The optimization options for the Metal compiler.
