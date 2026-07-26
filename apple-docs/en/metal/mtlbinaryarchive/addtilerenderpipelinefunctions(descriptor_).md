---
title: 'addTileRenderPipelineFunctions(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlbinaryarchive/addtilerenderpipelinefunctions(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchive/addtilerenderpipelinefunctions(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchive/addtilerenderpipelinefunctions%28descriptor%3A%29.json'
content_hash: 'sha256:4156283d024fd8ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchive](../mtlbinaryarchive.md)

# addTileRenderPipelineFunctions(descriptor:)

<sub>Instance Method</sub>

Adds a description of a tile renderer pipeline to the archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addTileRenderPipelineFunctions(descriptor: MTLTileRenderPipelineDescriptor) throws
```

## Parameters

- `descriptor` — A description of the tile renderer pipeline to archive.

## See Also

### Adding pipeline descriptors

- [- addComputePipelineFunctionsWithDescriptor:error:](<addcomputepipelinefunctions(descriptor_).md>) — Adds a description of a compute pipeline to the archive.
- [- addRenderPipelineFunctionsWithDescriptor:error:](<addrenderpipelinefunctions(descriptor_).md>) — Adds a description of a render pipeline to the archive.
- [- addFunctionWithDescriptor:library:error:](<addfunction(descriptor_library_).md>) — Adds a description of a function to the archive.
