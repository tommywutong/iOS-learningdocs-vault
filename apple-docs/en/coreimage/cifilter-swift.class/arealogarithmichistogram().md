---
title: areaLogarithmicHistogram()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/arealogarithmichistogram()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/arealogarithmichistogram()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/arealogarithmichistogram%28%29.json'
content_hash: 'sha256:3deb88ccb37ffa23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# areaLogarithmicHistogram()

<sub>Type Method</sub>

Returns a logarithmic histogram of a specified area of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func areaLogarithmicHistogram() -> any CIFilter & CIAreaLogarithmicHistogram
```

## Return Value

A 1-pixel-high image containing the calculated histogram`.`

## Discussion

This filter calculates histograms of the `red,``green,``blue,` and `alpha` colors for the specified area of an image. A base two-logarithm function is applied to the values before binning. The `count` property controls the number of bins (or width) of the histogram. The histogram is scaled so that all the values sum to `scale`.

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`extent`** — A [CGRect](../../corefoundation/cgrect.md) that specifies the subregion of the image you want to process.
- **`scale`** — The scale value for the histogram values. If the scale is `1`, then the bins in the resulting image sum to `1`.
- **`count`** — The number of bins for the histogram. This value determines the width of the output image. Minimum value `1`, and maximum value `2048`.
- **`minimumStop`** — The minimum of the range of color channel values in the logarithmic histogram image. Defaults to `-10`.
- **`maximumStop`** — The maximum of the range of color channel values in the logarithmic histogram image. Defaults to 4.

The following code creates a filter that results in a 1-pixel-tall image with a width of 256. The pixel color components contain the logarithmic histogram values:

```swift
func areaLogarithmicHistogram(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaLogarithmicHistogram()
    filter.inputImage = inputImage
    filter.count = 256
    filter.scale = 15
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}
```

Use the [+ histogramDisplayFilter](<histogramdisplay().md>) filter to display the histogram:

```swift
func logarithmicHistogramDisplay(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.histogramDisplay()
    filter.inputImage = areaLogarithmicHistogram(inputImage: inputImage)
    filter.highLimit = 1
    filter.height = 100
    filter.lowLimit = 0
    return filter.outputImage!
}
```

![](../../../../attachments/4df896e45ef3556427ad53eb0c914aa8/media-4407281@2x.png)

<sub>Two images arranged horizontally. The image on the left contains a photograph of a vineyard. The lower third of the image contains gravel with a deep shadow in the foreground. The middle of the image shows the vineyard receding into the distance. The top of the image shows a partially cloudy sky. The image on the right shows the result of the logarithmic histogram display filter. There are three overlayed charts showing the histogram of the red, green and blue components.</sub>

## See Also

### Filters

- [+ areaAverageFilter](<areaaverage().md>) — Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [+ areaHistogramFilter](<areahistogram().md>) — Returns a histogram of a specified area of the image.
- [+ areaMaximumFilter](<areamaximum().md>) — Calculates the maximum color components of a specified area of the image.
- [+ areaMaximumAlphaFilter](<areamaximumalpha().md>) — Finds the pixel with the highest alpha value.
- [+ areaMinimumFilter](<areaminimum().md>) — Calculates the minimum color component values for a specified area of the image.
- [+ areaMinimumAlphaFilter](<areaminimumalpha().md>) — Calculates the pixel within a specified area that has the smallest alpha value.
- [+ areaMinMaxFilter](<areaminmax().md>) — Calculates minimum and maximum color components for a specified area of the image.
- [+ areaMinMaxRedFilter](<areaminmaxred().md>) — Calculates the minimum and maximum red component value.
- [+ columnAverageFilter](<columnaverage().md>) — Calculates the average color for a specified column of an image.
- [+ histogramDisplayFilter](<histogramdisplay().md>) — Generates a histogram map from the image.
- [+ KMeansFilter](<kmeans().md>) — Applies the k-means algorithm to find the most common colors in an image.
- [+ rowAverageFilter](<rowaverage().md>) — Calculates the average color for the specified row of pixels in an image.
