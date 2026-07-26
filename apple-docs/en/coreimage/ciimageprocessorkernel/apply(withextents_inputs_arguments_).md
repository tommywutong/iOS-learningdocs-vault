---
title: 'apply(withExtents:inputs:arguments:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessorkernel/apply(withextents:inputs:arguments:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(withextents:inputs:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/apply%28withextents%3Ainputs%3Aarguments%3A%29.json'
content_hash: 'sha256:7d0d4ad3751a52cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# apply(withExtents:inputs:arguments:)

<sub>Type Method</sub>

Call this method on your multiple-output Core Image Processor Kernel subclass to create an array of new image objects given the specified array of extents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func apply(withExtents extents: [CIVector], inputs: [CIImage]?, arguments: [String : Any]?) throws -> [CIImage]
```

## Parameters

- `extents` — The array of bounding rectangles that the `CIImageProcessorKernel` can produce. Each rectangle in the array is an object created using `/CIVector/vectorWithCGRect:` This method will return `CIImage.emptyImage` if a rectangle in the array is empty.

- `inputs` — An array of [CIImage](../ciimage.md) objects to use as input.

- `arguments` — This dictionary contains any additional parameters that the processor needs to produce its output. The argument objects can be of any type but in order for CoreImage to cache intermediates, they must be of the following immutable types: `NSArray`, `NSDictionary`, `NSNumber`, `NSValue`, `NSData`, `NSString`, `NSNull`, [CIVector](../civector.md), [CIColor](../cicolor.md), `CGImage`, `CGColorSpace`, or `MLModel`.

## Return Value

An autoreleased [CIImage](../ciimage.md)

## Discussion

The inputs and arguments will be retained so that your subclass can be called when the image is drawn.

This method will return `nil` and an error if:

- calling [+ outputFormatAtIndex:arguments:](<outputformat(at_arguments_).md>) on your subclass returns an unsupported format.
- calling [+ formatForInputAtIndex:](<formatforinput(at_).md>) on your subclass returns an unsupported format.
- your subclass does not implement [+ processWithInputs:arguments:output:error:](<process(with_arguments_output_).md>)
