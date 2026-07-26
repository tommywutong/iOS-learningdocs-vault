---
title: 'newBinaryFunctionWithDescriptor:compilerTaskOptions:error:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newbinaryfunctionwithdescriptor:compilertaskoptions:error:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newbinaryfunctionwithdescriptor:compilertaskoptions:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newbinaryfunctionwithdescriptor%3Acompilertaskoptions%3Aerror%3A.json'
content_hash: 'sha256:2fc527060dd95e24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newBinaryFunctionWithDescriptor:compilerTaskOptions:error:

<sub>Instance Method</sub>

Creates a new binary visible or intersection function synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4BinaryFunction>) newBinaryFunctionWithDescriptor:(MTL4BinaryFunctionDescriptor *) descriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions error:(NSError **) error;
```

## Parameters

- `descriptor` — A binary function descriptor to use for creating the binary function.

- `compilerTaskOptions` — A descriptor of the compilation itself, providing parameters that influence execution of the compilation process.

- `error` — An optional parameter into which Metal stores information in case of an error.

## Return Value

A new binary function upon success, `nil` otherwise.
