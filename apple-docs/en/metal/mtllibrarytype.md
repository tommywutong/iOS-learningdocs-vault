---
title: MTLLibraryType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibrarytype
source_url: 'https://developer.apple.com/documentation/metal/mtllibrarytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrarytype.json'
content_hash: 'sha256:8efcf89c85c36aa2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLibraryType

<sub>Enumeration</sub>

A set of options for Metal library types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLLibraryType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Library options

- [MTLLibraryTypeExecutable](mtllibrarytype/executable.md) — A library that can create pipeline state objects.
- [MTLLibraryTypeDynamic](mtllibrarytype/dynamic.md) — A library that you can dynamically link to from other libraries.

### Initializers

- [init(rawValue:)](<mtllibrarytype/init(rawvalue_).md>)

## See Also

### Shader library management

- [MTLLibrary](mtllibrary.md) — A collection of Metal shader functions.
- [MTLDynamicLibrary](mtldynamiclibrary.md) — A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [MTLBinaryArchive](mtlbinaryarchive.md) — A container for pipeline state descriptors and their associated compiled shader code.
- [MTLCompileOptions](mtlcompileoptions.md) — Compilation settings for a Metal shader library.
- [MTLLanguageVersion](mtllanguageversion.md) — Metal shading language versions.
- [MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md) — The optimization options for the Metal compiler.
