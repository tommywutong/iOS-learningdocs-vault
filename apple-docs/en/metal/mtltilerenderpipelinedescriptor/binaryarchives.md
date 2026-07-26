---
title: binaryArchives
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltilerenderpipelinedescriptor/binaryarchives
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/binaryarchives'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinedescriptor/binaryarchives.json'
content_hash: 'sha256:ecf0059efbeb6e03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md)

# binaryArchives

<sub>Instance Property</sub>

An array of binary archives to search for precompiled versions of the shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var binaryArchives: [any MTLBinaryArchive]? { get set }
```

## See Also

### Specifying precompiled shader binaries

- [supportAddingBinaryFunctions](supportaddingbinaryfunctions.md) — A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to its callable functions list.
