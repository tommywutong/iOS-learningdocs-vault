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
doc_path: '/documentation/metal/mtl4compiler/makebinaryfunction(descriptor:compilertaskoptions:)-5o46e'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makebinaryfunction(descriptor:compilertaskoptions:)-5o46e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makebinaryfunction%28descriptor%3Acompilertaskoptions%3A%29-5o46e.json'
content_hash: 'sha256:fe4edfd7df3ec0dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeBinaryFunction(descriptor:compilerTaskOptions:)

<sub>Instance Method</sub>

Creates a new binary visible or intersection function synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBinaryFunction(descriptor: MTL4BinaryFunctionDescriptor, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) throws -> any MTL4BinaryFunction
```

## Parameters

- `descriptor` — A binary function descriptor to use for creating the binary function.

- `compilerTaskOptions` — A descriptor of the compilation itself, providing parameters that influence execution of the compilation process.

## Return Value

A binary function upon success, otherwise this function throws.
