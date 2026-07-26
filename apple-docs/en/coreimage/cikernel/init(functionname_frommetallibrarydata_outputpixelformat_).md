---
title: 'init(functionName:fromMetalLibraryData:outputPixelFormat:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cikernel/init(functionname:frommetallibrarydata:outputpixelformat:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cikernel/init(functionname:frommetallibrarydata:outputpixelformat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernel/init%28functionname%3Afrommetallibrarydata%3Aoutputpixelformat%3A%29.json'
content_hash: 'sha256:1a2d4114e45edc42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIKernel](../cikernel.md)

# init(functionName:fromMetalLibraryData:outputPixelFormat:)

<sub>Initializer</sub>

Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(functionName name: String, fromMetalLibraryData data: Data, outputPixelFormat format: CIFormat) throws
```

## Parameters

- `name` — The name of the function in the Metal shading language.

- `data` — A metallib file compiled with the Core Image Standard Library.

- `format` — The pixel format of the output kernel.

## Discussion

This method allows you to use MSL as the shader language for a Core Image kernel. Since MSL based kernels are precompiled, initializing them is faster than their than Core Image Kernel Language (CIKL) counterparts and Xcode can provide error diagnostics during development rather than at runtime. MSL is a more modern language than CIKL, and you can write shader code that uses arrays, structs and matrices.

MSL based kernels still support concatenation and tiling and can work in the same filter graph as traditional CIKL kernels.

## See Also

### Creating a Kernel Using Metal Shading Language

- [+ kernelWithFunctionName:fromMetalLibraryData:error:](<init(functionname_frommetallibrarydata_).md>) — Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [+ kernelNamesFromMetalLibraryData:](<kernelnames(frommetallibrarydata_).md>) — Return an array of strings containing the names of all of the kernels contained in the Metal library.
- [+ kernelsWithMetalString:error:](<kernels(withmetalstring_).md>) — Load kernels from a Metal language string.
