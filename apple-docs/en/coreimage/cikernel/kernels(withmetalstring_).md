---
title: 'kernels(withMetalString:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cikernel/kernels(withmetalstring:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cikernel/kernels(withmetalstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernel/kernels%28withmetalstring%3A%29.json'
content_hash: 'sha256:ee61165415d02d2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIKernel](../cikernel.md)

# kernels(withMetalString:)

<sub>Type Method</sub>

Load kernels from a Metal language string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func kernels(withMetalString source: String) throws -> [CIKernel]
```

## Parameters

- `source` — A string containing the progam in Metal language.

## Return Value

An array of [CIKernel](../cikernel.md) objects.

## See Also

### Creating a Kernel Using Metal Shading Language

- [+ kernelWithFunctionName:fromMetalLibraryData:error:](<init(functionname_frommetallibrarydata_).md>) — Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [+ kernelWithFunctionName:fromMetalLibraryData:outputPixelFormat:error:](<init(functionname_frommetallibrarydata_outputpixelformat_).md>) — Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [+ kernelNamesFromMetalLibraryData:](<kernelnames(frommetallibrarydata_).md>) — Return an array of strings containing the names of all of the kernels contained in the Metal library.
