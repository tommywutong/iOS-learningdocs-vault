---
title: 'process(with:arguments:outputs:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageprocessorkernel/process(with:arguments:outputs:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/process(with:arguments:outputs:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorkernel/process%28with%3Aarguments%3Aoutputs%3A%29.json'
content_hash: 'sha256:f0ae6b12ebdad792'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorKernel](../ciimageprocessorkernel.md)

# process(with:arguments:outputs:)

<sub>Type Method</sub>

Override this class method of your Core Image Processor Kernel subclass if it needs to produce multiple outputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func process(with inputs: [any CIImageProcessorInput]?, arguments: [String : Any]?, outputs: [any CIImageProcessorOutput]) throws
```

## Parameters

- `inputs` — An array of `id<CIImageProcessorInput>` that the class consumes to produce its output. The `input.region` may be larger than the rect returned by [+ roiForInput:arguments:outputRect:](<roi(forinput_arguments_outputrect_).md>).

- `arguments` — The arguments dictionary that was passed to [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>).

- `outputs` — An array `id<CIImageProcessorOutput>` that the `CIImageProcessorKernel` must provide results to.

## Discussion

This supports 0, 1, 2 or more input images and 2 or more output images.

When a `CIImage` containing your `CIImageProcessorKernel` class is rendered, your class’ implementation of this method will be called as needed for that render.  The method may be called more than once if Core Image needs to tile to limit memory usage.

When your implementation of this class method is called, use the provided `inputs` and `arguments` objects to return processed pixel data to Core Image via multiple `outputs`.

> [!important] Important
> This is a class method so that you cannot use or capture any state by accident. All the parameters that affect the output results must be passed to [+ applyWithExtent:inputs:arguments:error:](<apply(withextent_inputs_arguments_).md>).
