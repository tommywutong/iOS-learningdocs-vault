---
title: MTLBinaryArchive
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbinaryarchive
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchive.json'
content_hash: 'sha256:de1ea6b40544f8b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBinaryArchive

<sub>Protocol</sub>

A container for pipeline state descriptors and their associated compiled shader code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLBinaryArchive : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Identifying the archive

- [device](mtlbinaryarchive/device.md) — The Metal device object that created the binary archive.
- [label](mtlbinaryarchive/label.md) — A string that identifies the library.

### Adding pipeline descriptors

- [- addComputePipelineFunctionsWithDescriptor:error:](<mtlbinaryarchive/addcomputepipelinefunctions(descriptor_).md>) — Adds a description of a compute pipeline to the archive.
- [- addRenderPipelineFunctionsWithDescriptor:error:](<mtlbinaryarchive/addrenderpipelinefunctions(descriptor_).md>) — Adds a description of a render pipeline to the archive.
- [- addTileRenderPipelineFunctionsWithDescriptor:error:](<mtlbinaryarchive/addtilerenderpipelinefunctions(descriptor_).md>) — Adds a description of a tile renderer pipeline to the archive.
- [- addFunctionWithDescriptor:library:error:](<mtlbinaryarchive/addfunction(descriptor_library_).md>) — Adds a description of a function to the archive.

### Serializing archives

- [- serializeToURL:error:](<mtlbinaryarchive/serialize(to_).md>) — Writes the contents of the archive to a file.

### Instance Methods

- [- addLibraryWithDescriptor:error:](<mtlbinaryarchive/addlibrary(descriptor_).md>)
- [- addMeshRenderPipelineFunctionsWithDescriptor:error:](<mtlbinaryarchive/addmeshrenderpipelinefunctions(descriptor_).md>)

## See Also

### Shader library management

- [MTLLibrary](mtllibrary.md) — A collection of Metal shader functions.
- [MTLDynamicLibrary](mtldynamiclibrary.md) — A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [MTLCompileOptions](mtlcompileoptions.md) — Compilation settings for a Metal shader library.
- [MTLLibraryType](mtllibrarytype.md) — A set of options for Metal library types.
- [MTLLanguageVersion](mtllanguageversion.md) — Metal shading language versions.
- [MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md) — The optimization options for the Metal compiler.
