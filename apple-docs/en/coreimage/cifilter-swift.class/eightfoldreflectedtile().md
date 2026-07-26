---
title: eightfoldReflectedTile()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/eightfoldreflectedtile()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/eightfoldreflectedtile()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/eightfoldreflectedtile%28%29.json'
content_hash: 'sha256:936661eff80751d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# eightfoldReflectedTile()

<sub>Type Method</sub>

Creates an eight-way reflected pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func eightfoldReflectedTile() -> any CIFilter & CIEightfoldReflectedTile
```

## Return Value

The tiled image.

## Discussion

This method applies the eight-fold reflected tile filter to an image. The effect creates an eight-way symmetry from the input image and tiles it to create the output image.

The eight-fold reflected tile filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md).
- **`angle`** — A `float` representing the direction of distortion, in radians as an [NSNumber](../../foundation/nsnumber.md).
- **`width`** — A `float` representing the set width of each tile as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that results in small symmetrical repeated tiles:

```swift
func eightFoldReflected(inputImage: CIImage) -> CIImage {
    let eightFoldReflectedTile = CIFilter.eightfoldReflectedTile()
    eightFoldReflectedTile.inputImage = inputImage
    eightFoldReflectedTile.center = CGPoint(x: inputImage.extent.midX, y: inputImage.extent.midY)
    eightFoldReflectedTile.width = 400
    eightFoldReflectedTile.angle = 1
    return eightFoldReflectedTile.outputImage!
}
```

![](../../../../attachments/fb912ed7cc05459e4928c9e8957991af/media-4333630@2x.png)

<sub>A bouquet of multiple colorful flowers photographed up close with good lighting and focus. In the photo on the right, an eight-fold reflected tile filter is applied resulting in a square pattern that is repeated throughout the image.</sub>

## See Also

### Filters

- [+ affineClampFilter](<affineclamp().md>) — Performs a transform on the image and extends the image edges to infinity.
- [+ affineTileFilter](<affinetile().md>) — Performs a transform on the image and tiles the result.
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
- [+ triangleKaleidoscopeFilter](<trianglekaleidoscope().md>) — Create a triangular kaleidoscope effect and then tiles the result.
- [+ triangleTileFilter](<triangletile().md>) — Tiles a triangular area of an image.
- [+ twelvefoldReflectedTileFilter](<twelvefoldreflectedtile().md>) — Creates a tiled image by rotating in increments of 30 degrees.
