---
title: triangleKaleidoscope()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/trianglekaleidoscope()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/trianglekaleidoscope()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/trianglekaleidoscope%28%29.json'
content_hash: 'sha256:beca04246839811e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# triangleKaleidoscope()

<sub>Type Method</sub>

Create a triangular kaleidoscope effect and then tiles the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func triangleKaleidoscope() -> any CIFilter & CITriangleKaleidoscope
```

## Return Value

The tiled image.

## Discussion

This method applies the triangle kaleidoscope filter to an image. The effect produces a complex tiled pattern from a triangular area input image.

The triangle kaleidoscope tile filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`decay`** — A `float` representing the intensity of the color fade from the center of the triangle as an [NSNumber](../../foundation/nsnumber.md).
- **`point`** — A set of coordinates marking the center of the triangular area of the input image as a [CIVector](../civector.md).
- **`rotation`** — A `float` representing the angle of rotation of the triangle as an [NSNumber](../../foundation/nsnumber.md).
- **`size`** — A `float` representing the size in pixels of the triangle as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that produces a triangle tile of the input image, creating an optical illusion:

```swift
func triangleKaleidoscope(inputImage: CIImage) -> CIImage {
    let triangleKaleidoscopeTile = CIFilter.triangleKaleidoscope()
    triangleKaleidoscopeTile.inputImage = inputImage
    triangleKaleidoscopeTile.point = CGPoint(x: 150, y: 150)
    triangleKaleidoscopeTile.size = 700
    triangleKaleidoscopeTile.rotation = -0.36
    triangleKaleidoscopeTile.decay = 0.85
    return triangleKaleidoscopeTile.outputImage!
}
```

![](../../../../attachments/f00ec66d6be96e93b06365f384ff0dfb/media-3599889@2x.png)

<sub>Two photographs of a bouquet of multiple colorful flowers. The photo on the left is up close with good lighting and focus. In the photo on the right, a triangle kaleidoscope filter is applied, resulting in a triangular portion of the image being angled and repeated throughout the entire image.</sub>

## See Also

### Filters

- [+ affineClampFilter](<affineclamp().md>) — Performs a transform on the image and extends the image edges to infinity.
- [+ affineTileFilter](<affinetile().md>) — Performs a transform on the image and tiles the result.
- [+ eightfoldReflectedTileFilter](<eightfoldreflectedtile().md>) — Creates an eight-way reflected pattern.
- [+ fourfoldReflectedTileFilter](<fourfoldreflectedtile().md>) — Creates a four-way reflected pattern.
- [+ fourfoldRotatedTileFilter](<fourfoldrotatedtile().md>) — Creates a tiled image by rotating a tile in increments of 90 degrees.
- [+ fourfoldTranslatedTileFilter](<fourfoldtranslatedtile().md>) — Creates a tiled image by applying four translation operations.
- [+ glideReflectedTileFilter](<glidereflectedtile().md>) — Tiles an image by rotating and reflecting a tile from the image.
- [+ kaleidoscopeFilter](<kaleidoscope().md>) — Creates a 12-way kaleidoscopic image from an image.
- [+ opTileFilter](<optile().md>) — Produces an effect that mimics a style of visual art that uses optical illusions.
- [+ parallelogramTileFilter](<parallelogramtile().md>) — Warps the image to create a parallelogram and tiles the result.
- [+ perspectiveTileFilter](<perspectivetile().md>) — Tiles an image by adjusting the perspective of the image.
- [+ sixfoldReflectedTileFilter](<sixfoldreflectedtile().md>) — Produces a tiled image from a source image by applying a six-way reflected symmetry.
- [+ sixfoldRotatedTileFilter](<sixfoldrotatedtile().md>) — Creates a tiled image by rotating in increments of 60 degrees.
- [+ triangleTileFilter](<triangletile().md>) — Tiles a triangular area of an image.
- [+ twelvefoldReflectedTileFilter](<twelvefoldreflectedtile().md>) — Creates a tiled image by rotating in increments of 30 degrees.
