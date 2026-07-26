---
title: 'formatForInput(at:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessorkernel/formatforinput(at:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/formatforinput(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/formatforinput%28at%3A%29.json'
content_hash: 'sha256:cb16fc983ab55a20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# formatForInput(at:)

<sub>Type Method</sub>

Override this class method if you want your any of the inputs to be in a specific pixel format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func formatForInput(at inputIndex: Int32) -> CIFormat
```

## Discussion

The format must be one of `kCIFormatBGRA8`, `kCIFormatRGBAh`, `kCIFormatRGBAf` or `kCIFormatR8`. On iOS 12 and macOS 10.14, the formats `kCIFormatRh` and `kCIFormatRf` are also supported.

If the requested inputFormat is `0`, then the input will be a supported format that best matches the rendering context’s `/CIContext/workingFormat`.

If a processor wants data in a colorspace other than the context’s working color space, then call `/CIImage/imageByColorMatchingWorkingSpaceToColorSpace:` on the processor input. If a processor wants it input as alpha-unpremultiplied RGBA data, then call `/CIImage/imageByUnpremultiplyingAlpha` on the processor input.

## See Also

### Type Methods

- [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>) — Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.
- [+ processWithInputs:arguments:output:error:](<process(with_arguments_output_).md>) — Override this class method to implement your Core Image Processor Kernel subclass.
- [+ roiForInput:arguments:outputRect:](<roi(forinput_arguments_outputrect_).md>) — Override this class method to implement your processor’s ROI callback.
- [+ roiTileArrayForInput:arguments:outputRect:](<roitilearray(forinput_arguments_outputrect_).md>) — Override this class method to implement your processor’s tiled ROI callback.
