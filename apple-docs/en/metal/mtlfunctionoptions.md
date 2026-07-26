---
title: MTLFunctionOptions
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionoptions.json'
content_hash: 'sha256:9996ed79427de73d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionOptions

<sub>Structure</sub>

Options that define how Metal compiles a GPU function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLFunctionOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Function compilation options

- [MTLFunctionOptionFailOnBinaryArchiveMiss](mtlfunctionoptions/failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [MTLFunctionOptionCompileToBinary](mtlfunctionoptions/compiletobinary.md) — An option that instructs the compiler to generate a binary format for dynamic linking.
- [MTLFunctionOptionPipelineIndependent](mtlfunctionoptions/pipelineindependent.md) — An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [MTLFunctionOptionStoreFunctionInMetalPipelinesScript](mtlfunctionoptions/storefunctioninmetalpipelinesscript.md) — An option that instructs the compiler to store function information for inspecting binary archives.
- [MTLFunctionOptionStoreFunctionInMetalScript](mtlfunctionoptions/storefunctioninmetalscript.md) — An option that instructs the compiler to store function information for inspecting binary archives. _(deprecated)_

### Swift support

- [init(rawValue:)](<mtlfunctionoptions/init(rawvalue_).md>) — Creates a new function options structure from a raw value.

## See Also

### Identifying shader functions

- [device](mtlfunction/device.md) — The device object that created the shader function.
- [label](mtlfunction/label.md) — A string that identifies the shader function.
- [functionType](mtlfunction/functiontype.md) — The shader function’s type.
- [name](mtlfunction/name.md) — The function’s name.
- [MTLFunctionType](mtlfunctiontype.md) — The type of a top-level Metal Shading Language (MSL) function.
- [options](mtlfunction/options.md) — The options that Metal used to compile this function.
