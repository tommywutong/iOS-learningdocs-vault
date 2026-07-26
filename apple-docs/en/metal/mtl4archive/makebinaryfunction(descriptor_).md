---
title: 'makeBinaryFunction(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4archive/makebinaryfunction(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4archive/makebinaryfunction(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4archive/makebinaryfunction%28descriptor%3A%29.json'
content_hash: 'sha256:c6e3b2a97720905c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Archive](../mtl4archive.md)

# makeBinaryFunction(descriptor:)

<sub>Instance Method</sub>

Synchronously creates a binary version of a GPU visible function or GPU intersection function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBinaryFunction(descriptor: MTL4BinaryFunctionDescriptor) throws -> any MTL4BinaryFunction
```

## Parameters

- `descriptor` — A configuration that tells the method which GPU function to make into a binary function and which options to apply when compiling it.

## Return Value

A new GPU binary function instance if the method succeeds; otherwise `nil`.
