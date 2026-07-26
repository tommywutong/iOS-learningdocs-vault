---
title: argumentInfo
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlpipelineoption/argumentinfo
source_url: 'https://developer.apple.com/documentation/metal/mtlpipelineoption/argumentinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpipelineoption/argumentinfo.json'
content_hash: 'sha256:40dd1a84c214099c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPipelineOption](../mtlpipelineoption.md)

# argumentInfo

<sub>Type Property</sub>

An option instance that provides argument information for textures and threadgroup memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var argumentInfo: MTLPipelineOption { get }
```

## Discussion

This option provides all properties of an [MTLArgument](../mtlargument.md) instance, except for [bufferStructType](../mtlargument/bufferstructtype.md) and [bufferPointerType](../mtlargument/bufferpointertype.md), which are `nil`. To obtain these detailed buffer type properties, retrieve the [MTLPipelineOptionBufferTypeInfo](buffertypeinfo.md) instance.

## See Also

### Retrieving argument information

- [MTLPipelineOptionBufferTypeInfo](buffertypeinfo.md) — An option instance that provides detailed buffer type information for buffer arguments.
- [MTLPipelineOptionFailOnBinaryArchiveMiss](failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
