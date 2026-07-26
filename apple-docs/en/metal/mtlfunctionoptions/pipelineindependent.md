---
title: pipelineIndependent
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionoptions/pipelineindependent
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionoptions/pipelineindependent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionoptions/pipelineindependent.json'
content_hash: 'sha256:db59550f67920420'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionOptions](../mtlfunctionoptions.md)

# pipelineIndependent

<sub>Type Property</sub>

An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var pipelineIndependent: MTLFunctionOptions { get }
```

## Discussion

By default, when you link an [MTLFunction](../mtlfunction.md) into a pipeline state, Metal generates a function handle that points to that function’s location in the pipeline’s executable code. Because different pipeline states place functions at different memory addresses, Metal generates different function handles for the same function in each pipeline state. You insert function handles into an [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md) or [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) instance, which means you need separate function tables for each pipeline state by default.

When you compile a function with this option, Metal generates the same function handle for the function across all pipeline states that link it. This consistency lets you create a single function table and use it with multiple pipeline states, which reduces memory overhead and simplifies function table management.

> [!note] Note
> This option only works with functions that you compile with the [MTLFunctionOptionCompileToBinary](compiletobinary.md) option.

## See Also

### Function compilation options

- [MTLFunctionOptionFailOnBinaryArchiveMiss](failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [MTLFunctionOptionCompileToBinary](compiletobinary.md) — An option that instructs the compiler to generate a binary format for dynamic linking.
- [MTLFunctionOptionStoreFunctionInMetalPipelinesScript](storefunctioninmetalpipelinesscript.md) — An option that instructs the compiler to store function information for inspecting binary archives.
- [MTLFunctionOptionStoreFunctionInMetalScript](storefunctioninmetalscript.md) — An option that instructs the compiler to store function information for inspecting binary archives. _(deprecated)_
