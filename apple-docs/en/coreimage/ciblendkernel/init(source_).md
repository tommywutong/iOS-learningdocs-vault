---
title: 'init(source:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（12.0 起废弃）, iPadOS 8.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.14 起废弃）, tvOS 11.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/ciblendkernel/init(source:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciblendkernel/init(source:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciblendkernel/init%28source%3A%29.json'
content_hash: 'sha256:62d54ec8077914ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIBlendKernel](../ciblendkernel.md)

# init(source:)

<sub>Initializer</sub>

Creates a custom blend kernel from a program string.

> [!warning] Deprecated
> Core Image Kernel Language API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(source string: String)
```

## Parameters

- `string` — A program in the Core Image Kernel Language that contains a single routine marked using the `kernel` keyword.

## Return Value

A new blend kernel object, or nil if the specified source code does not contain a valid blend kernel routine.

## Discussion

This method is similar to the [+ kernelWithString:](<../cikernel/init(source_).md>) method of the superclass [CIKernel](../cikernel.md), but creates only blend kernels. Use this method when you want to ensure that the type of kernel object returned (if any) is always [CIBlendKernel](../ciblendkernel.md).
