---
title: bufferTypeInfo
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpipelineoption/buffertypeinfo
source_url: 'https://developer.apple.com/documentation/metal/mtlpipelineoption/buffertypeinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpipelineoption/buffertypeinfo.json'
content_hash: 'sha256:ab3dcde33d96270a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPipelineOption](../mtlpipelineoption.md)

# bufferTypeInfo

<sub>Type Property</sub>

An option instance that provides detailed buffer type information for buffer arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var bufferTypeInfo: MTLPipelineOption { get }
```

## Discussion

This option provides the [bufferStructType](../mtlargument/bufferstructtype.md) and [bufferPointerType](../mtlargument/bufferpointertype.md) properties for the [MTLPipelineOption](../mtlpipelineoption.md) stored in [MTLPipelineOptionArgumentInfo](argumentinfo.md).

## See Also

### Retrieving argument information

- [MTLPipelineOptionFailOnBinaryArchiveMiss](failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [MTLPipelineOptionArgumentInfo](argumentinfo.md) — An option instance that provides argument information for textures and threadgroup memory. _(deprecated)_
