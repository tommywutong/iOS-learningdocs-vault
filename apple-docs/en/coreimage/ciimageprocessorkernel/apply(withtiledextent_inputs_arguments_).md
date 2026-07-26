---
title: 'apply(withTiledExtent:inputs:arguments:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessorkernel/apply(withtiledextent:inputs:arguments:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(withtiledextent:inputs:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/apply%28withtiledextent%3Ainputs%3Aarguments%3A%29.json'
content_hash: 'sha256:94e6a5461b267986'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# apply(withTiledExtent:inputs:arguments:)

<sub>Type Method</sub>

Call this method on your Core Image Processor Kernel subclass to create a new image based on an array of tile extents that together cover the output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func apply(withTiledExtent tileExtents: [CIVector], inputs: [CIImage]?, arguments args: [String : Any]?) throws -> CIImage
```

## Parameters

- `tileExtents` — The array of bounding rectangles that the `CIImageProcessorKernel` can produce. Each rectangle in the array is an object created using `/CIVector/vectorWithCGRect:` This method will return `CIImage.emptyImage` if the rectangles in the array have gaps or overlaps.

- `inputs` — An array of [CIImage](../ciimage.md) objects to use as input.

## Return Value

An autoreleased [CIImage](../ciimage.md)

## Discussion

Each tile is a CGRect encoded as a CIVector using +[CIVector vectorWithCGRect:]. The overall output extent is computed as the union of all tile extents.

This method will return `nil` and an error if:

- calling [outputFormat](outputformat.md) on your subclass returns an unsupported format.
- calling [+ formatForInputAtIndex:](<formatforinput(at_).md>) on your subclass returns an unsupported format.
- your subclass does not implement [+ processWithInputs:arguments:output:error:](<process(with_arguments_output_).md>)
