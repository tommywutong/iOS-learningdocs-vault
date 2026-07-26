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
doc_path: /documentation/metal/mtlcomputepipelinedescriptor/binaryarchives
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/binaryarchives'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinedescriptor/binaryarchives.json'
content_hash: 'sha256:a278c4a734ef8816'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md)

# binaryArchives

<sub>Instance Property</sub>

The binary archives that contain any precompiled shader functions to link.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var binaryArchives: [any MTLBinaryArchive]? { get set }
```

## Discussion

The default value is `nil`.

When you create a Metal library, Metal compiles shader functions into an intermediate representation. When you create the pipeline state object, the GPU compiles this intermediate code.

By providing a set of binary archives, when Metal creates the pipeline state object, it first checks the archives to see if there’s already a compiled function. If so, Metal uses it instead.

## See Also

### Loading binary archives

- [supportAddingBinaryFunctions](supportaddingbinaryfunctions.md) — A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to its callable functions list.
