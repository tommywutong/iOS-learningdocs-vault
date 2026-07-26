---
title: 'outputFormat(at:arguments:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessorkernel/outputformat(at:arguments:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/outputformat(at:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/outputformat%28at%3Aarguments%3A%29.json'
content_hash: 'sha256:521cb43f3ab80f8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# outputFormat(at:arguments:)

<sub>Type Method</sub>

Override this class method if your processor has more than one output and you want your processor’s output to be in a specific supported `CIPixelFormat`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func outputFormat(at outputIndex: Int32, arguments: [String : Any]?) -> CIFormat
```

## Parameters

- `outputIndex` — The index that tells you which processor output for which to return the desired `CIPixelFormat`

- `arguments` — The arguments dictionary that was passed to [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>).

## Return Value

Return the desired `CIPixelFormat`

## Discussion

The format must be one of `kCIFormatBGRA8`, `kCIFormatRGBAh`, `kCIFormatRGBAf` or `kCIFormatR8`. On iOS 12 and macOS 10.14, the formats `kCIFormatRh` and `kCIFormatRf` are also supported.

If the outputFormat is `0`, then the output will be a supported format that best matches the rendering context’s `/CIContext/workingFormat`.
