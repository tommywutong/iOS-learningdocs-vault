---
title: 'newDynamicLibraryWithURL:completionHandler:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newdynamiclibrarywithurl:completionhandler:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newdynamiclibrarywithurl:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newdynamiclibrarywithurl%3Acompletionhandler%3A.json'
content_hash: 'sha256:cb67a4cd539e790b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newDynamicLibraryWithURL:completionHandler:

<sub>Instance Method</sub>

Creates a new dynamic library from the contents of a file at an URL location synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4CompilerTask>) newDynamicLibraryWithURL:(NSURL *) url completionHandler:(MTLNewDynamicLibraryCompletionHandler) completionHandler;
```

## Parameters

- `url` — An URL referencing a file whose contents this compiler uses to build a dynamic library.

- `completionHandler` — A block Metal calls when it finishes the build task.

## Return Value

A compiler task representing the asynchronous compilation task.
