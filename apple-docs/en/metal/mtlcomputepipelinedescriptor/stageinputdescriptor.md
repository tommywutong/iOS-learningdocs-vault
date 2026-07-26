---
title: stageInputDescriptor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinedescriptor/stageinputdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/stageinputdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinedescriptor/stageinputdescriptor.json'
content_hash: 'sha256:62f815dbe8adaea9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md)

# stageInputDescriptor

<sub>Instance Property</sub>

The organization of input and output data for the next kernel call.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var stageInputDescriptor: MTLStageInputOutputDescriptor? { get set }
```

## See Also

### Configuring compute pass inputs

- [MTLAttributeDescriptor](../mtlattributedescriptor.md) — A descriptor of an argument’s format and where its data is in memory.
- [MTLAttributeDescriptorArray](../mtlattributedescriptorarray.md) — An array of attribute descriptor objects.
- [MTLBufferLayoutDescriptor](../mtlbufferlayoutdescriptor.md) — A description of how a compute function fetches input data for an attribute.
- [MTLBufferLayoutDescriptorArray](../mtlbufferlayoutdescriptorarray.md) — An array of buffer layout descriptor objects.
