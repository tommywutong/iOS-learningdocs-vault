---
title: 'kernelNames(fromMetalLibraryData:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cikernel/kernelnames(frommetallibrarydata:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cikernel/kernelnames(frommetallibrarydata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernel/kernelnames%28frommetallibrarydata%3A%29.json'
content_hash: 'sha256:46d32a27b81e6e21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIKernel](../cikernel.md)

# kernelNames(fromMetalLibraryData:)

<sub>Type Method</sub>

Return an array of strings containing the names of all of the kernels contained in the Metal library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func kernelNames(fromMetalLibraryData data: Data) -> [String]
```

## Parameters

- `data` — Contents of the Metal library.

## Return Value

An Array of strings containing the names of the kernels.

## See Also

### Creating a Kernel Using Metal Shading Language

- [+ kernelWithFunctionName:fromMetalLibraryData:error:](<init(functionname_frommetallibrarydata_).md>) — Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [+ kernelWithFunctionName:fromMetalLibraryData:outputPixelFormat:error:](<init(functionname_frommetallibrarydata_outputpixelformat_).md>) — Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [+ kernelsWithMetalString:error:](<kernels(withmetalstring_).md>) — Load kernels from a Metal language string.
