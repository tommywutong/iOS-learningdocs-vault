---
title: storeFunctionInMetalScript
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+（18.0 起废弃）, iPadOS 17.0+（18.0 起废弃）, Mac Catalyst 17.0+（18.0 起废弃）, macOS 14.0+（15.0 起废弃）, tvOS 17.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlfunctionoptions/storefunctioninmetalscript
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionoptions/storefunctioninmetalscript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionoptions/storefunctioninmetalscript.json'
content_hash: 'sha256:0a5a9b14fa23b027'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionOptions](../mtlfunctionoptions.md)

# storeFunctionInMetalScript

<sub>Type Property</sub>

An option that instructs the compiler to store function information for inspecting binary archives.

> [!warning] Deprecated
> Use [MTLFunctionOptionStoreFunctionInMetalPipelinesScript](storefunctioninmetalpipelinesscript.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var storeFunctionInMetalScript: MTLFunctionOptions { get }
```

## See Also

### Function compilation options

- [MTLFunctionOptionFailOnBinaryArchiveMiss](failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [MTLFunctionOptionCompileToBinary](compiletobinary.md) — An option that instructs the compiler to generate a binary format for dynamic linking.
- [MTLFunctionOptionPipelineIndependent](pipelineindependent.md) — An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [MTLFunctionOptionStoreFunctionInMetalPipelinesScript](storefunctioninmetalpipelinesscript.md) — An option that instructs the compiler to store function information for inspecting binary archives.
