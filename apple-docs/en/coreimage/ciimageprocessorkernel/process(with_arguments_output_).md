---
title: 'process(with:arguments:output:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessorkernel/process(with:arguments:output:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/process(with:arguments:output:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/process%28with%3Aarguments%3Aoutput%3A%29.json'
content_hash: 'sha256:b881a40c1c57b797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# process(with:arguments:output:)

<sub>Type Method</sub>

Override this class method to implement your Core Image Processor Kernel subclass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func process(with inputs: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws
```

## Parameters

- `inputs` — An array of `id<CIImageProcessorInput>` that the class consumes to produce its output. The `input.region` may be larger than the rect returned by [+ roiForInput:arguments:outputRect:](<roi(forinput_arguments_outputrect_).md>).

- `arguments` — The arguments dictionary that was passed to [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>).

- `output` — The `id<CIImageProcessorOutput>` that the `CIImageProcessorKernel` must provide results to.

## Discussion

When a `CIImage` containing your `CIImageProcessorKernel` class is rendered, your class’ implementation of this method will be called as needed for that render.  The method may be called more than once if Core Image needs to tile to limit memory usage.

When your implementation of this class method is called, use the provided `inputs` and `arguments` objects to return processed pixel data to Core Image via `output`.

> [!important] Important
> This is a class method so that you cannot use or capture any state by accident. All the parameters that affect the output results must be passed to [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>).

## See Also

### Type Methods

- [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>) — Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.
- [+ formatForInputAtIndex:](<formatforinput(at_).md>) — Override this class method if you want your any of the inputs to be in a specific pixel format.
- [+ roiForInput:arguments:outputRect:](<roi(forinput_arguments_outputrect_).md>) — Override this class method to implement your processor’s ROI callback.
- [+ roiTileArrayForInput:arguments:outputRect:](<roitilearray(forinput_arguments_outputrect_).md>) — Override this class method to implement your processor’s tiled ROI callback.
