---
title: 'makeBinaryFunction(descriptor:compilerTaskOptions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/makebinaryfunction(descriptor:compilertaskoptions:)-hkc4'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makebinaryfunction(descriptor:compilertaskoptions:)-hkc4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makebinaryfunction%28descriptor%3Acompilertaskoptions%3A%29-hkc4.json'
content_hash: 'sha256:bee178931408856d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeBinaryFunction(descriptor:compilerTaskOptions:)

<sub>Instance Method</sub>

Creates a new binary visible or intersection function asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBinaryFunction(descriptor: MTL4BinaryFunctionDescriptor, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) async throws -> any MTL4BinaryFunction
```

## Parameters

- `descriptor` — A binary function descriptor to use for creating the binary function.

- `compilerTaskOptions` — A descriptor of the compilation itself, providing parameters that influence execution of the compilation process.

## Return Value

A binary function upon success, otherwise this function throws.
