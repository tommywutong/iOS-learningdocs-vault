---
title: outputFormat
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessorkernel/outputformat
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/outputformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/outputformat.json'
content_hash: 'sha256:764b0fdb12310893'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# outputFormat

<sub>Type Property</sub>

Override this class property if you want your processor’s output to be in a specific pixel format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class var outputFormat: CIFormat { get }
```

## Discussion

The format must be one of `kCIFormatBGRA8`, `kCIFormatRGBAh`, `kCIFormatRGBAf` or `kCIFormatR8`. On iOS 12 and macOS 10.14, the formats `kCIFormatRh` and `kCIFormatRf` are also supported.

If the outputFormat is `0`, then the output will be a supported format that best matches the rendering context’s `/CIContext/workingFormat`.

If a processor returns data in a color space other than the context working color space, then call `/CIImage/imageByColorMatchingColorSpaceToWorkingSpace:` on the processor output. If a processor returns data as alpha-unpremultiplied RGBA data, then call, `/CIImage/imageByPremultiplyingAlpha` on the processor output.

## See Also

### Type Properties

- [outputIsOpaque](outputisopaque.md) — Override this class property if your processor’s output stores 1.0 into the alpha channel of all pixels within the output extent.
- [synchronizeInputs](synchronizeinputs.md) — Override this class property to return false if you want your processor to be given input objects that have not been synchronized for CPU access.
