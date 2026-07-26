---
title: failOnBinaryArchiveMiss
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpipelineoption/failonbinaryarchivemiss
source_url: 'https://developer.apple.com/documentation/metal/mtlpipelineoption/failonbinaryarchivemiss'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpipelineoption/failonbinaryarchivemiss.json'
content_hash: 'sha256:5c1333ed4ebd9524'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPipelineOption](../mtlpipelineoption.md)

# failOnBinaryArchiveMiss

<sub>Type Property</sub>

An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var failOnBinaryArchiveMiss: MTLPipelineOption { get }
```

## Discussion

By default, Metal compiles the functions for a pipeline state if they aren’t in a binary archive. When you set this option, Metal returns an error instead of compiling a missing function.

## See Also

### Retrieving argument information

- [MTLPipelineOptionBufferTypeInfo](buffertypeinfo.md) — An option instance that provides detailed buffer type information for buffer arguments.
- [MTLPipelineOptionArgumentInfo](argumentinfo.md) — An option instance that provides argument information for textures and threadgroup memory. _(deprecated)_
