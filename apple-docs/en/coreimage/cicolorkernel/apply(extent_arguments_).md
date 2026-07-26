---
title: 'apply(extent:arguments:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicolorkernel/apply(extent:arguments:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorkernel/apply(extent:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorkernel/apply%28extent%3Aarguments%3A%29.json'
content_hash: 'sha256:b0347173e3a6f43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorKernel](../cicolorkernel.md)

# apply(extent:arguments:)

<sub>Instance Method</sub>

Creates a new image using the kernel and specified arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func apply(extent: CGRect, arguments args: [Any]) -> CIImage?
```

## Parameters

- `extent` — The extent of the output image.

- `args` — An array of arguments to pass to the kernel routine. The type of each object in the array must be compatible with the corresponding parameter declared in the kernel routine source code. For details, see [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397).

## Return Value

A new image object describing the result of applying the kernel.

## Discussion

This method is analogous to the [CIFilter](../cifilter-swift.class.md) method [- apply:arguments:options:](<../cifilter-swift.class/apply(__arguments_options_).md>), but it does not require construction of a [CIFilter](../cifilter-swift.class.md) object, and it allows you to specify a callback for determining the kernel’s region of interest as a block or closure. As with the similar [CIFilter](../cifilter-swift.class.md) method, calling this method does not execute the kernel code—filters and their kernel code are evaluated only when rendering a final output image.
