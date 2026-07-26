---
title: storeFunctionInMetalPipelinesScript
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionoptions/storefunctioninmetalpipelinesscript
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionoptions/storefunctioninmetalpipelinesscript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionoptions/storefunctioninmetalpipelinesscript.json'
content_hash: 'sha256:703d1a23e84ce239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionOptions](../mtlfunctionoptions.md)

# storeFunctionInMetalPipelinesScript

<sub>Type Property</sub>

An option that instructs the compiler to store function information for inspecting binary archives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var storeFunctionInMetalPipelinesScript: MTLFunctionOptions { get }
```

## Discussion

Set this option when you want to inspect or consume binary archives with the `metal-source` tool. You don’t need this option when you recompile functions or store them in binary archives.

## See Also

### Function compilation options

- [MTLFunctionOptionFailOnBinaryArchiveMiss](failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [MTLFunctionOptionCompileToBinary](compiletobinary.md) — An option that instructs the compiler to generate a binary format for dynamic linking.
- [MTLFunctionOptionPipelineIndependent](pipelineindependent.md) — An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [MTLFunctionOptionStoreFunctionInMetalScript](storefunctioninmetalscript.md) — An option that instructs the compiler to store function information for inspecting binary archives. _(deprecated)_
