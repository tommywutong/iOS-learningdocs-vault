---
title: areaHistogram()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/areahistogram()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/areahistogram()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/areahistogram%28%29.json'
content_hash: 'sha256:7158431922aa9372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# areaHistogram()

<sub>Type Method</sub>

Returns a histogram of a specified area of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func areaHistogram() -> any CIFilter & CIAreaHistogram
```

## Return Value

A 1 pixel high image containing the calculated histogram`.`

## Discussion

This filter calculates histograms of the red, green, blue, and alpha colors in the region defined by `extent`. The `count` property controls the number of bins (or width) of the histogram. The filter scales the histogram so that the total of all the counts in the bins equals `scale`.

The area histogram filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`extent`** — A [CGRect](../../corefoundation/cgrect.md) that specifies the subregion of the image that you want to process.
- **`scale`** — The scale value to use for the histogram values. If the scale is 1, then the total of all the counts in the histogram equals 1.
- **`count`** — The number of bins for the histogram. This value determines the width of the output image. Minimum value 1, maximum value 2048.

The following code creates a filter that results in an image that has a height of 1 pixel and a width of 256 pixels. The pixel color components contain the histogram values.

```swift
func areaHistogram(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaHistogram()
    filter.inputImage = inputImage
    filter.count = 256
    filter.scale = 50
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}
```

To display the histogram, you can use the [+ histogramDisplayFilter](<histogramdisplay().md>) filter:

```swift
func histogramDisplay(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.histogramDisplay()
    filter.inputImage = areaHistogram(inputImage: inputImage)
    filter.highLimit = 1
    filter.height = 100
    filter.lowLimit = 0
    return filter.outputImage!
}

```

![](../../../../attachments/d97a604d980184e6a74406d6098a21b4/media-4332392@2x.png)

<sub>Two images arranged horizontally. The left image contains a photograph of three hydrangea flowers with leaves in the background. The image on the right shows the result of the histogram display filter. There are three overlaid charts showing the histogram of the red, green, and blue components.</sub>

## See Also

### Filters

- [+ areaAverageFilter](<areaaverage().md>) — Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [+ areaLogarithmicHistogramFilter](<arealogarithmichistogram().md>) — Returns a logarithmic histogram of a specified area of the image.
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
