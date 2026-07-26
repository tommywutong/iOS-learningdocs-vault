---
title: 'newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newbinaryfunctionwithdescriptor:compilertaskoptions:completionhandler:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newbinaryfunctionwithdescriptor:compilertaskoptions:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newbinaryfunctionwithdescriptor%3Acompilertaskoptions%3Acompletionhandler%3A.json'
content_hash: 'sha256:d5292205f690aefd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:

<sub>Instance Method</sub>

Returns a new compiler task that asyncrhonously creates a binary version of a GPU visible function or GPU intersection function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4CompilerTask>) newBinaryFunctionWithDescriptor:(MTL4BinaryFunctionDescriptor *) descriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions completionHandler:(MTL4NewBinaryFunctionCompletionHandler) completionHandler;
```

## Parameters

- `descriptor` — A configuration that tells the method which GPU function to make into a binary function and which options to apply when compiling it.

- `compilerTaskOptions` — A configuration for the compiler task.

- `completionHandler` — A completetion handler that you provide, which the task calls when it finishes compiling the binary function.
