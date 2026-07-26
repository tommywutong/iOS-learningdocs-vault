---
title: 'makeDynamicLibrary(library:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/makedynamiclibrary(library:)-7f4yz'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makedynamiclibrary(library:)-7f4yz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makedynamiclibrary%28library%3A%29-7f4yz.json'
content_hash: 'sha256:a8046bc58ea146d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeDynamicLibrary(library:)

<sub>Instance Method</sub>

Creates a new Metal library instance asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeDynamicLibrary(library: any MTLLibrary) async throws -> any MTLDynamicLibrary
```

## Return Value

A dynamic metal library upon success, otherwise this function throws.
