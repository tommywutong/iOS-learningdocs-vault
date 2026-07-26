---
title: 'makeDynamicLibrary(library:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/makedynamiclibrary(library:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makedynamiclibrary(library:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makedynamiclibrary%28library%3A%29.json'
content_hash: 'sha256:b0b240b1a643e81d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeDynamicLibrary(library:)

<sub>Instance Method</sub>

Creates a new dynamic library from a library containing Metal IR code synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeDynamicLibrary(library: any MTLLibrary) throws -> any MTLDynamicLibrary
```

## Parameters

- `library` — A library from which this compiler creates the new a dynamic library

## Return Value

A new dynamic Metal library upon success, `nil` otherwise.

## Default Implementations

### MTL4Compiler Implementations

- [makeDynamicLibrary(library:)](<makedynamiclibrary(library_)-7f4yz.md>) — Creates a new Metal library instance asynchronously.
