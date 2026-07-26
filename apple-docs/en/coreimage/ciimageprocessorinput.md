---
title: CIImageProcessorInput
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessorinput
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorinput.json'
content_hash: 'sha256:c1f77752153ee79d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIImageProcessorInput

<sub>Protocol</sub>

A container of image data and information for use in a custom image processor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIImageProcessorInput
```

## Overview

Your app does not define classes that adopt this protocol; Core Image provides an object of this type when applying a custom image processor you create with a [CIImageProcessorKernel](ciimageprocessorkernel.md) subclass.

In your image processor class’ [+ processWithInputs:arguments:output:error:](<ciimageprocessorkernel/process(with_arguments_output_).md>) method, use the provided `CIImageProcessorInput` object to access the image data and supporting information to perform your custom image processing routine. For example, if you process the image using a Metal shader, use the [metalTexture](ciimageprocessorinput/metaltexture.md) property to bind the image as an input texture. Or, if you process the image using a CPU-based routine, use the [baseAddress](ciimageprocessorinput/baseaddress.md) property to access pixel data in memory.

To finish setting up or performing your image processing routine, use the provided [CIImageProcessorOutput](ciimageprocessoroutput.md) object to return processed pixel data to Core Image.

## Topics

### Accessing Input Image Data

- [baseAddress](ciimageprocessorinput/baseaddress.md) — The base address of CPU memory that your Core Image Processor Kernel can read pixels from.
- [metalTexture](ciimageprocessorinput/metaltexture.md) — A MTLTexture object that can be bound for input using Metal.
- [pixelBuffer](ciimageprocessorinput/pixelbuffer.md) — An input pixel buffer object that your Core Image Processor Kernel can read from.
- [surface](ciimageprocessorinput/surface.md) — An input surface object that your Core Image Processor Kernel can read from.

### Getting Supplemental Information for Image Processing

- [region](ciimageprocessorinput/region.md) — The rectangular region of the input image that your Core Image Processor Kernel can use to provide the output.
- [bytesPerRow](ciimageprocessorinput/bytesperrow.md) — The bytes per row of the CPU memory that your Core Image Processor Kernel can read pixelsfrom.
- [format](ciimageprocessorinput/format.md) — The pixel format of the CPU memory that your Core Image Processor Kernel can read pixels from.

### Instance Properties

- [digest](ciimageprocessorinput/digest.md) — A 64-bit digest that uniquely describes the contents of the input to a processor.
- [roiTileCount](ciimageprocessorinput/roitilecount.md) — This property tells a tiled-input processor how many input tiles will be processed.
- [roiTileIndex](ciimageprocessorinput/roitileindex.md) — This property tells a tiled-input processor which input tile index is being processed.

## See Also

### Custom Image Processors

- [CIImageProcessorKernel](ciimageprocessorkernel.md) — The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- [CIImageProcessorOutput](ciimageprocessoroutput.md) — A container for writing image data and information produced by a custom image processor.
