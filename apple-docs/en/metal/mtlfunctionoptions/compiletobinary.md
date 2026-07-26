---
title: compileToBinary
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionoptions/compiletobinary
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionoptions/compiletobinary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionoptions/compiletobinary.json'
content_hash: 'sha256:258543538049fa91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionOptions](../mtlfunctionoptions.md)

# compileToBinary

<sub>Type Property</sub>

An option that instructs the compiler to generate a binary format for dynamic linking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var compileToBinary: MTLFunctionOptions { get }
```

## See Also

### Function compilation options

- [MTLFunctionOptionFailOnBinaryArchiveMiss](failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [MTLFunctionOptionPipelineIndependent](pipelineindependent.md) — An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [MTLFunctionOptionStoreFunctionInMetalPipelinesScript](storefunctioninmetalpipelinesscript.md) — An option that instructs the compiler to store function information for inspecting binary archives.
- [MTLFunctionOptionStoreFunctionInMetalScript](storefunctioninmetalscript.md) — An option that instructs the compiler to store function information for inspecting binary archives. _(deprecated)_
