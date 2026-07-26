---
title: 'makeCompiler(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makecompiler(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecompiler(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecompiler%28descriptor%3A%29.json'
content_hash: 'sha256:bdff619b87358c57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeCompiler(descriptor:)

<sub>Instance Method</sub>

Creates a new compiler from a compiler descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCompiler(descriptor: MTL4CompilerDescriptor) throws -> any MTL4Compiler
```

## Parameters

- `descriptor` — A [MTL4CompilerDescriptor](../mtl4compilerdescriptor.md) instance that configures the [MTL4Compiler](../mtl4compiler.md) instance.

## Return Value

A [MTL4Compiler](../mtl4compiler.md) instance, or `nil` if the function failed.
