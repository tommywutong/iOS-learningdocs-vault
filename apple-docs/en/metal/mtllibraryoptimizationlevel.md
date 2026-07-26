---
title: MTLLibraryOptimizationLevel
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibraryoptimizationlevel
source_url: 'https://developer.apple.com/documentation/metal/mtllibraryoptimizationlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibraryoptimizationlevel.json'
content_hash: 'sha256:3dac1db1f804a818'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLibraryOptimizationLevel

<sub>Enumeration</sub>

The optimization options for the Metal compiler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLLibraryOptimizationLevel
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Optimization options

- [MTLLibraryOptimizationLevelDefault](mtllibraryoptimizationlevel/default.md) — An optimization option for the Metal compiler that prioritizes runtime performance.
- [MTLLibraryOptimizationLevelSize](mtllibraryoptimizationlevel/size.md) — An optimization option for the Metal compiler that prioritizes minimizing the size of its output binaries, which may also reduce compile time.

### Initializers

- [init(rawValue:)](<mtllibraryoptimizationlevel/init(rawvalue_).md>)

## See Also

### Shader library management

- [MTLLibrary](mtllibrary.md) — A collection of Metal shader functions.
- [MTLDynamicLibrary](mtldynamiclibrary.md) — A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [MTLBinaryArchive](mtlbinaryarchive.md) — A container for pipeline state descriptors and their associated compiled shader code.
- [MTLCompileOptions](mtlcompileoptions.md) — Compilation settings for a Metal shader library.
- [MTLLibraryType](mtllibrarytype.md) — A set of options for Metal library types.
- [MTLLanguageVersion](mtllanguageversion.md) — Metal shading language versions.
- [MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
