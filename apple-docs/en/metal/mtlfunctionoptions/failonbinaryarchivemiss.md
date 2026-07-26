---
title: failOnBinaryArchiveMiss
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionoptions/failonbinaryarchivemiss
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionoptions/failonbinaryarchivemiss'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionoptions/failonbinaryarchivemiss.json'
content_hash: 'sha256:3e9398b18e6bb4b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionOptions](../mtlfunctionoptions.md)

# failOnBinaryArchiveMiss

<sub>Type Property</sub>

An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var failOnBinaryArchiveMiss: MTLFunctionOptions { get }
```

## Discussion

By default, Metal compiles a function if it isn’t in a binary archive. When you set this option, Metal returns an error instead of compiling a missing function.

Setting this option is a way to verify that binary archives contain all the functions your app needs, or to measure a binary archive’s hit rates.

## See Also

### Function compilation options

- [MTLFunctionOptionCompileToBinary](compiletobinary.md) — An option that instructs the compiler to generate a binary format for dynamic linking.
- [MTLFunctionOptionPipelineIndependent](pipelineindependent.md) — An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [MTLFunctionOptionStoreFunctionInMetalPipelinesScript](storefunctioninmetalpipelinesscript.md) — An option that instructs the compiler to store function information for inspecting binary archives.
- [MTLFunctionOptionStoreFunctionInMetalScript](storefunctioninmetalscript.md) — An option that instructs the compiler to store function information for inspecting binary archives. _(deprecated)_
