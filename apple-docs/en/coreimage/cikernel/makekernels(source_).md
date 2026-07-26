---
title: 'makeKernels(source:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（12.0 起废弃）, iPadOS 8.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.14 起废弃）, tvOS（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cikernel/makekernels(source:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cikernel/makekernels(source:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernel/makekernels%28source%3A%29.json'
content_hash: 'sha256:5b5d9b57ae13e7dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIKernel](../cikernel.md)

# makeKernels(source:)

<sub>Type Method</sub>

Creates and returns and array of  `CIKernel` objects.

> [!warning] Deprecated
> Core Image Kernel Language API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func makeKernels(source string: String) -> [CIKernel]?
```

## Parameters

- `string` — A program in the Core Image Kernel Language that contains one or more routines, each of which is marked using the `kernel` keyword.

## Return Value

An array of  `CIKernel` objects. The array contains one `CIKernel` objects for each kernel routine in the supplied string. Each object in the array can be of class [CIKernel](../cikernel.md), [CIColorKernel](../cicolorkernel.md), or [CIWarpKernel](../ciwarpkernel.md) depending on the corresponding routine specified in the Core Image Kernel Language source code string.

## Discussion

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## See Also

### Deprecated

- [+ kernelWithString:](<init(source_).md>) — Creates a single kernel object. _(deprecated)_
