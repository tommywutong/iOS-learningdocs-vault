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
doc_path: '/documentation/coreimage/cikernel/init(source:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cikernel/init(source:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernel/init%28source%3A%29.json'
content_hash: 'sha256:f88956cf854cdd1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIKernel](../cikernel.md)

# init(source:)

<sub>Initializer</sub>

Creates a single kernel object.

> [!warning] Deprecated
> Core Image Kernel Language API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(source string: String)
```

## Parameters

- `string` — A program in the Core Image Kernel Language that contains a single routine marked using the `kernel` keyword.

## Return Value

A new kernel object. The class of the returned object can be [CIKernel](../cikernel.md), [CIColorKernel](../cicolorkernel.md), or [CIWarpKernel](../ciwarpkernel.md) depending on the type of routine specified in the Core Image Kernel Language source code string.

## Discussion

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## See Also

### Related Documentation

- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397)

### Deprecated

- [+ kernelsWithString:](<makekernels(source_).md>) — Creates and returns and array of  `CIKernel` objects. _(deprecated)_
