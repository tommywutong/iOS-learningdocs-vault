---
title: 'roi(forInput:arguments:outputRect:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessorkernel/roi(forinput:arguments:outputrect:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/roi(forinput:arguments:outputrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/roi%28forinput%3Aarguments%3Aoutputrect%3A%29.json'
content_hash: 'sha256:5c52cb78e60e924e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# roi(forInput:arguments:outputRect:)

<sub>Type Method</sub>

Override this class method to implement your processor’s ROI callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func roi(forInput inputIndex: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect
```

## Parameters

- `inputIndex` — The index that tells you which processor input for which to return the ROI rectangle.

- `arguments` — The arguments dictionary that was passed to [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>).

- `outputRect` — The output `CGRect` that processor will be asked to output.

## Return Value

The `CGRect` of the `inputIndex`th input that is required for the above `outputRect`

## Discussion

This will be called one or more times per render to determine what portion of the input images are needed to render a given ‘outputRect’ of the output. This will not be called if processor has no input images.

The default implementation would return outputRect.

> [!important] Important
> This is a class method so that you cannot use or capture any state by accident. All the parameters that affect the output results must be passed to [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>).

## See Also

### Type Methods

- [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>) — Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.
- [+ formatForInputAtIndex:](<formatforinput(at_).md>) — Override this class method if you want your any of the inputs to be in a specific pixel format.
- [+ processWithInputs:arguments:output:error:](<process(with_arguments_output_).md>) — Override this class method to implement your Core Image Processor Kernel subclass.
- [+ roiTileArrayForInput:arguments:outputRect:](<roitilearray(forinput_arguments_outputrect_).md>) — Override this class method to implement your processor’s tiled ROI callback.
