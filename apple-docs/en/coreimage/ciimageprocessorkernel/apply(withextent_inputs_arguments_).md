---
title: 'apply(withExtent:inputs:arguments:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessorkernel/apply(withextent:inputs:arguments:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(withextent:inputs:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/apply%28withextent%3Ainputs%3Aarguments%3A%29.json'
content_hash: 'sha256:78b518c4967c67bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# apply(withExtent:inputs:arguments:)

<sub>Type Method</sub>

Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func apply(withExtent extent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage
```

## Parameters

- `extent` — The bounding `CGRect` of pixels that the `CIImageProcessorKernel` can produce. This method will return `/CIImage/emptyImage` if extent is empty.

- `inputs` — An array of [CIImage](../ciimage.md) objects to use as input.

- `arguments` — This dictionary contains any additional parameters that the processor needs to produce its output. The argument objects can be of any type but in order for CoreImage to cache intermediates, they must be of the following immutable types: `NSArray`, `NSDictionary`, `NSNumber`, `NSValue`, `NSData`, `NSString`, `NSNull`, [CIVector](../civector.md), [CIColor](../cicolor.md), `CGImage`, `CGColorSpace`, or `MLModel`.

## Return Value

An autoreleased [CIImage](../ciimage.md)

## Discussion

The inputs and arguments will be retained so that your subclass can be called when the image is drawn.

This method will return `nil` and an error if:

- calling [outputFormat](outputformat.md) on your subclass returns an unsupported format.
- calling [+ formatForInputAtIndex:](<formatforinput(at_).md>) on your subclass returns an unsupported format.
- your subclass does not implement [+ processWithInputs:arguments:output:error:](<process(with_arguments_output_).md>)

## See Also

### Type Methods

- [+ formatForInputAtIndex:](<formatforinput(at_).md>) — Override this class method if you want your any of the inputs to be in a specific pixel format.
- [+ processWithInputs:arguments:output:error:](<process(with_arguments_output_).md>) — Override this class method to implement your Core Image Processor Kernel subclass.
- [+ roiForInput:arguments:outputRect:](<roi(forinput_arguments_outputrect_).md>) — Override this class method to implement your processor’s ROI callback.
- [+ roiTileArrayForInput:arguments:outputRect:](<roitilearray(forinput_arguments_outputrect_).md>) — Override this class method to implement your processor’s tiled ROI callback.
