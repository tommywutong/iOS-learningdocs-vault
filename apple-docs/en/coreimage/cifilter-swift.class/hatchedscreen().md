---
title: hatchedScreen()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/hatchedscreen()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/hatchedscreen()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/hatchedscreen%28%29.json'
content_hash: 'sha256:fbada01fa91cfbc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# hatchedScreen()

<sub>Type Method</sub>

Creates a monochrome image with a series of lines to add detail.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func hatchedScreen() -> any CIFilter & CIHatchedScreen
```

## Return Value

The modified image.

## Discussion

This method applies a hatched screen filter to an image. The effect generates a monochrome image containing a series of lines in hatched pattern to create detail. The halftone effect is a set of lines, dots, or circles that contain detail. When viewing the image from a distance, the markings blend together, creating the illusion of continuous lines and shapes. The effect is often used in print media for more efficient printing.

The hatched screen filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md).
- **`angle`** — A `float` representing the angle of the pattern as an [NSNumber](../../foundation/nsnumber.md).
- **`width`** — A `float` representing the distance between lines in the pattern as an [NSNumber](../../foundation/nsnumber.md).
- **`sharpness`** — A `float` representing the sharpness of the pattern as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that produces a monochrome image containing lines of detail on a black background:

```swift
func hatched(inputImage: CIImage) -> CIImage {
    let hatchedScreen = CIFilter.hatchedScreen()
    hatchedScreen.inputImage = inputImage
    hatchedScreen.center = CGPoint(x: 2016, y: 1512)
    hatchedScreen.angle = 10
    hatchedScreen.width = 35
    hatchedScreen.sharpness = 0.7
    return hatchedScreen.outputImage!
}
```

![](../../../../attachments/d95bfbb2d1541d005276bd8e53ad7990/media-3595917@2x.png)

<sub>Two photographs of wooden barrel of green artichokes. The artichokes are crisp with good lighting. The photo on the left has no modifications to color or detail. In the photo on the right, a hatched screen filter is applied, resulting in a lighter, grayscale image with an overlay of small lines in a hatched pattern, creating the detail of the image.</sub>

## See Also

### Filters

- [+ circularScreenFilter](<circularscreen().md>) — Adds a circular overlay to an image.
- [+ CMYKHalftone](<cmykhalftone().md>) — Adds a series of colorful dots to an image.
- [+ dotScreenFilter](<dotscreen().md>) — Creates a monochrome image with a series of dots to add detail.
- [+ lineScreenFilter](<linescreen().md>) — Creates a monochrome image with a series of small lines to add detail.
