---
title: 'init(source:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（12.0 起废弃）, iPadOS 8.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.14 起废弃）, tvOS（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cicolorkernel/init(source:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorkernel/init(source:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorkernel/init%28source%3A%29.json'
content_hash: 'sha256:1363d3e9cb20d1ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorKernel](../cicolorkernel.md)

# init(source:)

<sub>Initializer</sub>

Creates a color kernel object from the specified kernel source code.

> [!warning] Deprecated
> Core Image Kernel Language API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(source string: String)
```

## Parameters

- `string` — A program in the Core Image Kernel Language that contains a single routine marked using the `kernel` keyword.

## Return Value

A new color kernel object, or `nil` if the specified source code does not contain a valid color kernel routine.

## Discussion

This method is similar to the [+ kernelWithString:](<../cikernel/init(source_).md>) method of the superclass [CIKernel](../cikernel.md), but creates only color kernels. Use this method when you want to ensure that the type of kernel object returned (if any) is always [CIColorKernel](../cicolorkernel.md).
