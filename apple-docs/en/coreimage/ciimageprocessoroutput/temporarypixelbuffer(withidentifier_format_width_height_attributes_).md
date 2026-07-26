---
title: 'temporaryPixelBuffer(withIdentifier:format:width:height:attributes:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessoroutput/temporarypixelbuffer(withidentifier:format:width:height:attributes:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/temporarypixelbuffer(withidentifier:format:width:height:attributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessoroutput/temporarypixelbuffer%28withidentifier%3Aformat%3Awidth%3Aheight%3Aattributes%3A%29.json'
content_hash: 'sha256:e5f4cea9e882f1fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorOutput](../ciimageprocessoroutput.md)

# temporaryPixelBuffer(withIdentifier:format:width:height:attributes:)

<sub>Instance Method</sub>

Returns a temporary CVPixelBuffer that your Core Image Processor Kernel can use as scratch storage during processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func temporaryPixelBuffer(withIdentifier identifier: String, format: OSType, width: Int, height: Int, attributes: [AnyHashable : Any]? = nil) -> Unmanaged<CVPixelBuffer>?
```

## Parameters

- `identifier` — A name that uniquely identifies this scratch buffer within the processor invocation.

- `format` — The pixel format for the buffer. Must be a non-zero `OSType` pixel format constant.

- `width` — The width of the buffer in pixels. Must be greater than zero.

- `height` — The height of the buffer in pixels. Must be greater than zero.

- `attributes` — An optional dictionary of `CVPixelBuffer` creation attributes.

## Return Value

A non-retained `CVPixelBuffer` of the requested size and format, or `nil` if the buffer could not be created.

## Discussion

Use this method when your processor needs an intermediate `CVPixelBuffer` to stash data between stages of its work. Core Image manages the lifetime of the returned buffer and reuses the underlying allocation across multiple invocations when possible. This is more efficient than allocating a fresh `CVPixelBuffer` on each invocation of your processor.

The returned pixel buffer is valid only for the duration of the [+ processWithInputs:arguments:output:error:](<../ciimageprocessorkernel/process(with_arguments_output_).md>) call that requested it. Don’t retain it beyond the scope of that method or use it after the method returns.

Calling this method multiple times within the same processor invocation with the same `identifier`, `format`, `width`, and `height` returns a pixel buffer backed by the same `IOSurface`. Otherwise it returns a distinct pixel buffer. This lets a processor request several independent pixel buffers by giving each one a unique name.
