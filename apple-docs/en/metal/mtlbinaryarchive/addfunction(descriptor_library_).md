---
title: 'addFunction(descriptor:library:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlbinaryarchive/addfunction(descriptor:library:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchive/addfunction(descriptor:library:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchive/addfunction%28descriptor%3Alibrary%3A%29.json'
content_hash: 'sha256:46f3b41fdc7e6cb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchive](../mtlbinaryarchive.md)

# addFunction(descriptor:library:)

<sub>Instance Method</sub>

Adds a description of a function to the archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addFunction(descriptor: MTLFunctionDescriptor, library: any MTLLibrary) throws
```

## Parameters

- `descriptor` — 

- `library` — 

## See Also

### Adding pipeline descriptors

- [- addComputePipelineFunctionsWithDescriptor:error:](<addcomputepipelinefunctions(descriptor_).md>) — Adds a description of a compute pipeline to the archive.
- [- addRenderPipelineFunctionsWithDescriptor:error:](<addrenderpipelinefunctions(descriptor_).md>) — Adds a description of a render pipeline to the archive.
- [- addTileRenderPipelineFunctionsWithDescriptor:error:](<addtilerenderpipelinefunctions(descriptor_).md>) — Adds a description of a tile renderer pipeline to the archive.
