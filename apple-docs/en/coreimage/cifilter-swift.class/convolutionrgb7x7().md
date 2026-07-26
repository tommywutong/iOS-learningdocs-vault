---
title: convolutionRGB7X7()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/convolutionrgb7x7()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/convolutionrgb7x7()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/convolutionrgb7x7%28%29.json'
content_hash: 'sha256:cb31a7f6257aac78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# convolutionRGB7X7()

<sub>Type Method</sub>

Applies a convolution 7 x 7 filter to the RGB components of an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func convolutionRGB7X7() -> any CIFilter & CIConvolution
```

## Return Value

The convolved image.

## Discussion

This method applies a 7 x 7 convolution to the `RGB` components image. The effect uses a 7 x 7 area surrounding an input pixel, the pixel itself, and those within a distance of 3 pixels horizontally and vertically. The effect repeats this for every pixel within the image. The work area is then combined with the weight property vector to produce the processed image. This filter differs from the [+ convolution7X7Filter](<convolution7x7().md>) filter, which processes all of the color components including the alpha component.

The convolution-RGB 7 x 7 filter uses the following properties:

- **`inputImage`** — A [CIImage](../ciimage.md) containing the image to process.
- **`weights`** — A [CIVector](../civector.md) representing the convolution kernel.
- **`bias`** — A `float` representing the value that’s added to each output pixel.

> [!note] Note
> When using a nonzero `bias` value, the output image has an infinite extent. You should crop the output image before attempting to render it.

The following code creates a filter that highlights edges in the input image:

```swift
func convolutionRGB7X7(inputImage: CIImage) -> CIImage {
    let convolutionFilter = CIFilter.convolutionRGB7X7()
    convolutionFilter.inputImage = inputImage
    let weights: [CGFloat] = [
        0, 0, -1, -1, -1, 0, 0,
        0, -1, -3, -3, -3, -1, 0,
        -1, -3, 0, 7, 0, -3, -1,
        -1, -3, 7, 25, 7, -3, -1,
        -1, -3, 0, 7, 0, -3, -1,
        0, -1, -3, -3, -3, -1, 0,
        0, 0, -1, -1, -1, 0, 0
    ]
    let kernel = CIVector(values: weights, count: 49)
    convolutionFilter.weights = kernel
    convolutionFilter.bias = 0.0
    return convolutionFilter.outputImage!
}
```

![](../../../../attachments/e13d156f8eeffbdeaa74cb99335d304f/media-4407333@2x.png)

<sub>Two images arranged horizontally. The left image contains a photo of the Golden Gate Bridge with a clear sky as the background. The right image shows the result of applying a 7 x 7 convolution kernel that highlights edges. Fine detail and noise in the image are highlighted.</sub>

## See Also

### Filters

- [+ convolution3X3Filter](<convolution3x3().md>) — Applies a convolution 3 x 3 filter to the `RGBA` components of an image.
- [+ convolution5X5Filter](<convolution5x5().md>) — Applies a convolution 5 x 5 filter to the `RGBA` components image.
- [+ convolution7X7Filter](<convolution7x7().md>) — Applies a convolution 7 x 7 filter to the `RGBA` color components of an image.
- [+ convolution9HorizontalFilter](<convolution9horizontal().md>) — Applies a convolution-9 horizontal filter to the `RGBA` components of an image.
- [+ convolution9VerticalFilter](<convolution9vertical().md>) — Applies a convolution-9 vertical filter to the `RGBA` components of an image.
- [+ convolutionRGB3X3Filter](<convolutionrgb3x3().md>) — Applies a convolution 3 x 3 filter to the `RGB` components of an image.
- [+ convolutionRGB5X5Filter](<convolutionrgb5x5().md>) — Applies a convolution 5 x 5 filter to the `RGB` components of an image.
- [+ convolutionRGB9HorizontalFilter](<convolutionrgb9horizontal().md>) — Applies a convolution 9 x 1 filter to the RGB components of an image.
- [+ convolutionRGB9VerticalFilter](<convolutionrgb9vertical().md>) — Applies a convolution 1 x 9 filter to the RGB components of an image.
