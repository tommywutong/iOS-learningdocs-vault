---
title: 'temporarySurface(withIdentifier:format:width:height:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessoroutput/temporarysurface(withidentifier:format:width:height:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/temporarysurface(withidentifier:format:width:height:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessoroutput/temporarysurface%28withidentifier%3Aformat%3Awidth%3Aheight%3A%29.json'
content_hash: 'sha256:a9932267475794bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorOutput](../ciimageprocessoroutput.md)

# temporarySurface(withIdentifier:format:width:height:)

<sub>Instance Method</sub>

Returns a temporary IOSurface that your Core Image Processor Kernel can use as scratch storage during processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func temporarySurface(withIdentifier identifier: String, format: OSType, width: Int, height: Int) -> IOSurface?
```

## Parameters

- `identifier` — A name that uniquely identifies this scratch surface within the processor invocation.

- `format` — The pixel format for the surface. Must be a non-zero `OSType` pixel format constant.

- `width` — The width of the surface in pixels. Must be greater than zero.

- `height` — The height of the surface in pixels. Must be greater than zero.

## Return Value

An autoreleased `IOSurface` of the requested size and format, or `nil` if the surface could not be created.

## Discussion

Use this method when your processor needs an intermediate `IOSurface` to stash data between stages of its work. Core Image manages the lifetime of the returned surface and reuses the underlying allocation across multiple invocations when possible. This is more efficient than allocating a fresh `IOSurface` on each invocation of your processor.

The returned surface is valid only for the duration of the [+ processWithInputs:arguments:output:error:](<../ciimageprocessorkernel/process(with_arguments_output_).md>) call that requested it. Don’t retain it beyond the scope of that method or use it after the method returns.

Calling this method multiple times within the same processor invocation with the same `identifier`, `format`, `width`, and `height` returns the same surface. Otherwise it returns a distinct surface. This lets a processor request several independent surfaces by giving each one a unique name.
