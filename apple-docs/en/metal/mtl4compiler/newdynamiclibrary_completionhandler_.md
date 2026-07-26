---
title: 'newDynamicLibrary:completionHandler:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newdynamiclibrary:completionhandler:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newdynamiclibrary:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newdynamiclibrary%3Acompletionhandler%3A.json'
content_hash: 'sha256:9c8e4afbf2062470'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newDynamicLibrary:completionHandler:

<sub>Instance Method</sub>

Creates a new dynamic Metal library instance asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4CompilerTask>) newDynamicLibrary:(id<MTLLibrary>) library completionHandler:(MTLNewDynamicLibraryCompletionHandler) completionHandler;
```

## Parameters

- `library` — A library from which this compiler creates the new a dynamic library

- `completionHandler` — A block Metal calls when it finishes the build task.

## Return Value

A compiler task representing the asynchronous compilation task.
