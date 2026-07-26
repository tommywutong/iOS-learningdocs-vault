---
title: 'makeLibrary(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/makelibrary(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makelibrary(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makelibrary%28descriptor%3A%29.json'
content_hash: 'sha256:45abf676fb9088ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeLibrary(descriptor:)

<sub>Instance Method</sub>

Creates a new Metal library synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeLibrary(descriptor: MTL4LibraryDescriptor) throws -> any MTLLibrary
```

## Parameters

- `descriptor` — A description of the library to create.

## Return Value

A Metal library instance upon success, `nil` otherwise.

## Default Implementations

### MTL4Compiler Implementations

- [makeLibrary(descriptor:)](<makelibrary(descriptor_)-6c46o.md>) — Creates a new Metal library asynchronously.
