---
title: 'addRenderPipelineFunctions(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlbinaryarchive/addrenderpipelinefunctions(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchive/addrenderpipelinefunctions(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchive/addrenderpipelinefunctions%28descriptor%3A%29.json'
content_hash: 'sha256:f2a2d3cff5da1f62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchive](../mtlbinaryarchive.md)

# addRenderPipelineFunctions(descriptor:)

<sub>Instance Method</sub>

Adds a description of a render pipeline to the archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addRenderPipelineFunctions(descriptor: MTLRenderPipelineDescriptor) throws
```

## Parameters

- `descriptor` — A description of the render pipeline to archive.

## See Also

### Adding pipeline descriptors

- [- addComputePipelineFunctionsWithDescriptor:error:](<addcomputepipelinefunctions(descriptor_).md>) — Adds a description of a compute pipeline to the archive.
- [- addTileRenderPipelineFunctionsWithDescriptor:error:](<addtilerenderpipelinefunctions(descriptor_).md>) — Adds a description of a tile renderer pipeline to the archive.
- [- addFunctionWithDescriptor:library:error:](<addfunction(descriptor_library_).md>) — Adds a description of a function to the archive.
