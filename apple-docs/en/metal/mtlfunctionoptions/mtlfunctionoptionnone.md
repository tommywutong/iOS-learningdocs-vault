---
title: MTLFunctionOptionNone
framework: Metal
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionoptions/mtlfunctionoptionnone
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionoptions/mtlfunctionoptionnone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionoptions/mtlfunctionoptionnone.json'
content_hash: 'sha256:fe3cc52936240678'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionOptions](../mtlfunctionoptions.md)

# MTLFunctionOptionNone

<sub>Enumeration Case</sub>

A sentinel value that represents an empty set of options, which is the default behavior for creating functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
MTLFunctionOptionNone
```

## See Also

### Function compilation options

- [MTLFunctionOptionFailOnBinaryArchiveMiss](failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [MTLFunctionOptionCompileToBinary](compiletobinary.md) — An option that instructs the compiler to generate a binary format for dynamic linking.
- [MTLFunctionOptionPipelineIndependent](pipelineindependent.md) — An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [MTLFunctionOptionStoreFunctionInMetalPipelinesScript](storefunctioninmetalpipelinesscript.md) — An option that instructs the compiler to store function information for inspecting binary archives.
- [MTLFunctionOptionStoreFunctionInMetalScript](storefunctioninmetalscript.md) — An option that instructs the compiler to store function information for inspecting binary archives. _(deprecated)_
