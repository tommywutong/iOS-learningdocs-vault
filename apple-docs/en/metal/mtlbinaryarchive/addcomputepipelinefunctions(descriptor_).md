---
title: 'addComputePipelineFunctions(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlbinaryarchive/addcomputepipelinefunctions(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchive/addcomputepipelinefunctions(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchive/addcomputepipelinefunctions%28descriptor%3A%29.json'
content_hash: 'sha256:75b3f2ae78d06a82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchive](../mtlbinaryarchive.md)

# addComputePipelineFunctions(descriptor:)

<sub>Instance Method</sub>

Adds a description of a compute pipeline to the archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addComputePipelineFunctions(descriptor: MTLComputePipelineDescriptor) throws
```

## Parameters

- `descriptor` — A description of the compute pipeline to archive.

## See Also

### Adding pipeline descriptors

- [- addRenderPipelineFunctionsWithDescriptor:error:](<addrenderpipelinefunctions(descriptor_).md>) — Adds a description of a render pipeline to the archive.
- [- addTileRenderPipelineFunctionsWithDescriptor:error:](<addtilerenderpipelinefunctions(descriptor_).md>) — Adds a description of a tile renderer pipeline to the archive.
- [- addFunctionWithDescriptor:library:error:](<addfunction(descriptor_library_).md>) — Adds a description of a function to the archive.
