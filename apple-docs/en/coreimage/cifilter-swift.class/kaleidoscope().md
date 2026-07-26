---
title: kaleidoscope()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/kaleidoscope()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/kaleidoscope()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/kaleidoscope%28%29.json'
content_hash: 'sha256:43efbf09706bcbe4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# kaleidoscope()

<sub>Type Method</sub>

Creates a 12-way kaleidoscopic image from an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func kaleidoscope() -> any CIFilter & CIKaleidoscope
```

## Return Value

The tiled image.

## Discussion

This method applies the kaleidoscope tile filter to an image. The effect produces a complex 12-way symmetrical reflected pattern from the input image.

The kaleidoscope tile filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md).
- **`angle`** — A `float` representing the direction of distortion, in radians as an [NSNumber](../../foundation/nsnumber.md).
- **`count`** — A `float` representing the number of reflections in the pattern as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that results in the creation of a kaleidoscope effect from the input image:

```swift
func kaleidoscope(inputImage: CIImage) -> CIImage {
    let kaleidoscopeEffect = CIFilter.kaleidoscope()
    kaleidoscopeEffect.inputImage = inputImage
    kaleidoscopeEffect.count = 6
    kaleidoscopeEffect.center = CGPoint(x: 150, y: 150)
    kaleidoscopeEffect.angle = 0
    return kaleidoscopeEffect.outputImage!
}
```

![](../../../../attachments/dd280f88d3dc1783e908c2a52cdb35e4/media-3599884@2x.png)

<sub>Two photographs. The photo on the left is of a bouquet of colorful flowers up close with good lighting and focus. In the photo on the right, a kaleidoscope filter is applied, resulting in an small segment of the image being repeated around 360 degrees.</sub>

## See Also

### Filters

- [+ affineClampFilter](<affineclamp().md>) — Performs a transform on the image and extends the image edges to infinity.
- [+ affineTileFilter](<affinetile().md>) — Performs a transform on the image and tiles the result.
- [+ eightfoldReflectedTileFilter](<eightfoldreflectedtile().md>) — Creates an eight-way reflected pattern.
- [+ fourfoldReflectedTileFilter](<fourfoldreflectedtile().md>) — Creates a four-way reflected pattern.
- [+ fourfoldRotatedTileFilter](<fourfoldrotatedtile().md>) — Creates a tiled image by rotating a tile in increments of 90 degrees.
- [+ fourfoldTranslatedTileFilter](<fourfoldtranslatedtile().md>) — Creates a tiled image by applying four translation operations.
- [+ glideReflectedTileFilter](<glidereflectedtile().md>) — Tiles an image by rotating and reflecting a tile from the image.
- [+ opTileFilter](<optile().md>) — Produces an effect that mimics a style of visual art that uses optical illusions.
- [+ parallelogramTileFilter](<parallelogramtile().md>) — Warps the image to create a parallelogram and tiles the result.
- [+ perspectiveTileFilter](<perspectivetile().md>) — Tiles an image by adjusting the perspective of the image.
- [+ sixfoldReflectedTileFilter](<sixfoldreflectedtile().md>) — Produces a tiled image from a source image by applying a six-way reflected symmetry.
- [+ sixfoldRotatedTileFilter](<sixfoldrotatedtile().md>) — Creates a tiled image by rotating in increments of 60 degrees.
- [+ triangleKaleidoscopeFilter](<trianglekaleidoscope().md>) — Create a triangular kaleidoscope effect and then tiles the result.
- [+ triangleTileFilter](<triangletile().md>) — Tiles a triangular area of an image.
- [+ twelvefoldReflectedTileFilter](<twelvefoldreflectedtile().md>) — Creates a tiled image by rotating in increments of 30 degrees.
