---
title: 'makeDynamicLibrary(url:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/makedynamiclibrary(url:)-18tis'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makedynamiclibrary(url:)-18tis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makedynamiclibrary%28url%3A%29-18tis.json'
content_hash: 'sha256:e1e172df580ac7df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeDynamicLibrary(url:)

<sub>Instance Method</sub>

Creates a new dynamic library from the contents of a file at an URL location synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeDynamicLibrary(url: URL) async throws -> any MTLDynamicLibrary
```

## Parameters

- `url` — An URL referencing a file whose contents this compiler uses to build a dynamic library.

## Return Value

A dynamic metal library upon success, otherwise this function throws.
