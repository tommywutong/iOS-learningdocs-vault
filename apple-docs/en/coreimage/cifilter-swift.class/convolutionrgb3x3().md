---
title: convolutionRGB3X3()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/convolutionrgb3x3()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/convolutionrgb3x3()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/convolutionrgb3x3%28%29.json'
content_hash: 'sha256:bb4595e8af95767d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# convolutionRGB3X3()

<sub>Type Method</sub>

Applies a convolution 3 x 3 filter to the `RGB` components of an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func convolutionRGB3X3() -> any CIFilter & CIConvolution
```

## Return Value

The convolved image.

## Discussion

This method applies a 3 x 3 convolution to the `RGB` components of an image. The effect uses a 3 x 3 area surrounding an input pixel, the pixel itself, and those within a distance of 1 pixel horizontally and vertically. This filter differs from the [+ convolution3X3Filter](<convolution3x3().md>) filter, which processes all of the color components including the alpha component.

The convolution-RGB 3 x 3 filter uses the following properties:

- **`bias`** — A `float` representing the value that’s added to each output pixel.
- **`weights`** — A [CIVector](../civector.md) representing the convolution kernel.
- **`inputImage`** — A [CIImage](../ciimage.md) containing the image to process.

> [!note] Note
> When using a nonzero `bias` value, the output image has an infinite extent. You should crop the output image before attempting to render it.

The following code creates a filter that sharpens the input image:

```swift
func convolutionRGB3X3(inputImage: CIImage) -> CIImage {
    let convolutionFilter = CIFilter.convolutionRGB3X3()
    convolutionFilter.inputImage = inputImage
    let kernel = CIVector(values: [
        0, -2, 0,
        -2, 9, -2,
        0, -2, 0
    ], count: 9)
    convolutionFilter.weights = kernel
    convolutionFilter.bias = 0.0
    return convolutionFilter.outputImage!
}
```

![](../../../../attachments/3822396c355353c595422bd0a53e4d95/media-4407321@2x.png)

<sub>Two images arranged horizontally. The left image is of a modern building with horizontal concrete beams and large tinted windows. The right image shows the result of applying the convolution RGB 3 x 3 filter with a kernel that sharpens the image. Edges and fine detail in the image are emphasized.</sub>

## See Also

### Filters

- [+ convolution3X3Filter](<convolution3x3().md>) — Applies a convolution 3 x 3 filter to the `RGBA` components of an image.
- [+ convolution5X5Filter](<convolution5x5().md>) — Applies a convolution 5 x 5 filter to the `RGBA` components image.
- [+ convolution7X7Filter](<convolution7x7().md>) — Applies a convolution 7 x 7 filter to the `RGBA` color components of an image.
- [+ convolution9HorizontalFilter](<convolution9horizontal().md>) — Applies a convolution-9 horizontal filter to the `RGBA` components of an image.
- [+ convolution9VerticalFilter](<convolution9vertical().md>) — Applies a convolution-9 vertical filter to the `RGBA` components of an image.
- [+ convolutionRGB5X5Filter](<convolutionrgb5x5().md>) — Applies a convolution 5 x 5 filter to the `RGB` components of an image.
- [+ convolutionRGB7X7Filter](<convolutionrgb7x7().md>) — Applies a convolution 7 x 7 filter to the RGB components of an image.
- [+ convolutionRGB9HorizontalFilter](<convolutionrgb9horizontal().md>) — Applies a convolution 9 x 1 filter to the RGB components of an image.
- [+ convolutionRGB9VerticalFilter](<convolutionrgb9vertical().md>) — Applies a convolution 1 x 9 filter to the RGB components of an image.
