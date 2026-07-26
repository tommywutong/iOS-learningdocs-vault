---
title: 'roiTileArray(forInput:arguments:outputRect:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/roitilearray%28forinput%3Aarguments%3Aoutputrect%3A%29.json'
content_hash: 'sha256:f76f3e1c514ee316'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# roiTileArray(forInput:arguments:outputRect:)

<sub>Type Method</sub>

Override this class method to implement your processor’s tiled ROI callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func roiTileArray(forInput inputIndex: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]
```

## Parameters

- `inputIndex` — The index that tells you which processor input for which to return the array of ROI rectangles

- `arguments` — The arguments dictionary that was passed to [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>).

- `outputRect` — The output `CGRect` that processor will be asked to output.

## Return Value

An array of [CIVector](../civector.md) that specify tile regions of the `inputIndex`’th input that is required for the above `outputRect` Each region tile in the array is a created by calling `/CIVector/vectorWithCGRect:` The tiles may overlap but should fully cover the area of ‘input’ that is needed. If a processor has multiple inputs, then each input should return the same number of region tiles.

## Discussion

This will be called one or more times per render to determine what tiles of the input images are needed to render a given `outputRect` of the output.

If the processor implements this method, then when rendered;

- as CoreImage prepares for a render, this method will be called for each input to return an ROI tile array.
- as CoreImage performs the render, the method [+ processWithInputs:arguments:output:error:](<process(with_arguments_output_).md>) will be called once for each tile.

> [!important] Important
> This is a class method so that you cannot use or capture any state by accident. All the parameters that affect the output results must be passed to [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>).

## See Also

### Type Methods

- [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>) — Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.
- [+ formatForInputAtIndex:](<formatforinput(at_).md>) — Override this class method if you want your any of the inputs to be in a specific pixel format.
- [+ processWithInputs:arguments:output:error:](<process(with_arguments_output_).md>) — Override this class method to implement your Core Image Processor Kernel subclass.
- [+ roiForInput:arguments:outputRect:](<roi(forinput_arguments_outputrect_).md>) — Override this class method to implement your processor’s ROI callback.
