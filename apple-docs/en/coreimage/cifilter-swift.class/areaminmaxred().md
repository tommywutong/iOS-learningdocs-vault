---
title: areaMinMaxRed()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/areaminmaxred()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/areaminmaxred()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/areaminmaxred%28%29.json'
content_hash: 'sha256:c900279b58b19db1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# areaMinMaxRed()

<sub>Type Method</sub>

Calculates the minimum and maximum red component value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func areaMinMaxRed() -> any CIFilter & CIAreaMinMaxRed
```

## Return Value

The generated image.

## Discussion

This method applies the area-minimum-maximum-red filter to an image. This effect calculates the darkest and lightest red color value in the region defined by `extent`. The red and green components of the 1 x 1 pixel output image contain the result.

The area-minimum-maximum-red filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`extent`** — A [CGRect](../../corefoundation/cgrect.md) that specifies the subregion of the image that you want to process.

The following code creates a filter that results in a 1 x 1 pixel image with the red and green color components populated:

```swift
func areaMinMaxRed(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaMinMaxRed()
    filter.inputImage = inputImage
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
     return filter.outputImage!
}
```

![](../../../../attachments/46cac0e7bbcdb6c0c381bc0b7fd2b2fd/media-4331787@2x.png)

<sub>Two images arranged horizontally. The left image contains a photograph of three hydrangea flowers with leaves in the background. A 500 x 500 pixel square in the center of the image is highlighted using an outlined box. The image on the right shows the result of applying the area min-max red filter to the 500 x 500 pixel square. The result is a 1 x 1 pixel image containing a green color. This indicates that the 100 x 100 pixel square contains colors that contain a strong red component along with colors that contain a weak red component.</sub>

## See Also

### Filters

- [+ areaAverageFilter](<areaaverage().md>) — Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [+ areaHistogramFilter](<areahistogram().md>) — Returns a histogram of a specified area of the image.
- [+ areaLogarithmicHistogramFilter](<arealogarithmichistogram().md>) — Returns a logarithmic histogram of a specified area of the image.
- [+ areaMaximumFilter](<areamaximum().md>) — Calculates the maximum color components of a specified area of the image.
- [+ areaMaximumAlphaFilter](<areamaximumalpha().md>) — Finds the pixel with the highest alpha value.
- [+ areaMinimumFilter](<areaminimum().md>) — Calculates the minimum color component values for a specified area of the image.
- [+ areaMinimumAlphaFilter](<areaminimumalpha().md>) — Calculates the pixel within a specified area that has the smallest alpha value.
- [+ areaMinMaxFilter](<areaminmax().md>) — Calculates minimum and maximum color components for a specified area of the image.
- [+ columnAverageFilter](<columnaverage().md>) — Calculates the average color for a specified column of an image.
- [+ histogramDisplayFilter](<histogramdisplay().md>) — Generates a histogram map from the image.
- [+ KMeansFilter](<kmeans().md>) — Applies the k-means algorithm to find the most common colors in an image.
- [+ rowAverageFilter](<rowaverage().md>) — Calculates the average color for the specified row of pixels in an image.
