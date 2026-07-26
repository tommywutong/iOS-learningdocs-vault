---
title: areaMaximum()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/areamaximum()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/areamaximum()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/areamaximum%28%29.json'
content_hash: 'sha256:46d25514933926c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# areaMaximum()

<sub>Type Method</sub>

Calculates the maximum color components of a specified area of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func areaMaximum() -> any CIFilter & CIAreaMaximum
```

## Return Value

A 1 x 1 size image containing the maximum color components.

## Discussion

This filter returns the maximum color components in the region defined by `extent`.

The area maximum filter uses the following properties:.

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`extent`** — A [CGRect](../../corefoundation/cgrect.md) that specifies the subregion of the image that you want to process.

The following code creates a filter that calculates the maximum color components of a 500 x 500 set of pixels from the center of the image:

```swift
func areaMaximum(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaMaximum()
    filter.inputImage = inputImage
    filter.extent = CGRect(
        x: inputImage.extent.width/2,
        y: inputImage.extent.height/2,
        width: 100,
        height: 100)
     return filter.outputImage!
}
```

![](../../../../attachments/7f79d65b99ec177329e6dc785fb9c98b/media-4331784@2x.png)

<sub>Two images arranged horizontally. The left image contains a photograph of three hydrangea flowers with leaves in the background. A 500 x 500 pixel square in the center of the image is highlighted using an outlined box. The image on the right shows the result of applying the area maximum filter to the 500 x 500 pixel square. The result is a 1 x 1 pixel image containing a color made up of the maximum color components from the highlighted square.</sub>

## See Also

### Filters

- [+ areaAverageFilter](<areaaverage().md>) — Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [+ areaHistogramFilter](<areahistogram().md>) — Returns a histogram of a specified area of the image.
- [+ areaLogarithmicHistogramFilter](<arealogarithmichistogram().md>) — Returns a logarithmic histogram of a specified area of the image.
- [+ areaMaximumAlphaFilter](<areamaximumalpha().md>) — Finds the pixel with the highest alpha value.
- [+ areaMinimumFilter](<areaminimum().md>) — Calculates the minimum color component values for a specified area of the image.
- [+ areaMinimumAlphaFilter](<areaminimumalpha().md>) — Calculates the pixel within a specified area that has the smallest alpha value.
- [+ areaMinMaxFilter](<areaminmax().md>) — Calculates minimum and maximum color components for a specified area of the image.
- [+ areaMinMaxRedFilter](<areaminmaxred().md>) — Calculates the minimum and maximum red component value.
- [+ columnAverageFilter](<columnaverage().md>) — Calculates the average color for a specified column of an image.
- [+ histogramDisplayFilter](<histogramdisplay().md>) — Generates a histogram map from the image.
- [+ KMeansFilter](<kmeans().md>) — Applies the k-means algorithm to find the most common colors in an image.
- [+ rowAverageFilter](<rowaverage().md>) — Calculates the average color for the specified row of pixels in an image.
