---
title: parallelogramTile()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/parallelogramtile()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/parallelogramtile()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/parallelogramtile%28%29.json'
content_hash: 'sha256:ab0bfade95ce6aa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# parallelogramTile()

<sub>Type Method</sub>

Warps the image to create a parallelogram and tiles the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func parallelogramTile() -> any CIFilter & CIParallelogramTile
```

## Return Value

The tiled image.

## Discussion

This method applies the parallelogram tile filter to an image. The effect warps the input image to create a parallelogram and then tiles the result.

The parallelogram tile filter uses the following properties:

- **inputImage** — An image with the type [CIImage](../ciimage.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md).
- **`angle`** — A `float` representing the direction of distortion, in radians as an [NSNumber](../../foundation/nsnumber.md).
- **`width`** — A `float` representing the set width of each tile as an [NSNumber](../../foundation/nsnumber.md).
- **`acuteAngle`** — A `float` representing the primary angle for the repeating parallelogram tile.

The following code creates a filter that results in the image being cropped to a parallelogram and then tiled:

```swift
func parallelogram(inputImage: CIImage) -> CIImage {
    let parallelogramTile = CIFilter.parallelogramTile()
    parallelogramTile.inputImage = inputImage
    parallelogramTile.center = CGPoint(x: 150, y: 150)
    parallelogramTile.angle = 0
    parallelogramTile.acuteAngle = 1.57
    parallelogramTile.width = 100
    return parallelogramTile.outputImage!
}
```

![](../../../../attachments/334a9544f874ff65b346cc4020b154c2/media-3599887@2x.png)

<sub>Two photographs of a bouquet of multiple colorful flowers. The photo on the left is up close with good lighting and focus. In the photo on the right, a parallelogram tile filter is applied, resulting in the image becoming a set of parallelogram tiles that contain portions of white and yellow petals surrounded by a blue center.</sub>

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
- [+ perspectiveTileFilter](<perspectivetile().md>) — Tiles an image by adjusting the perspective of the image.
- [+ sixfoldReflectedTileFilter](<sixfoldreflectedtile().md>) — Produces a tiled image from a source image by applying a six-way reflected symmetry.
- [+ sixfoldRotatedTileFilter](<sixfoldrotatedtile().md>) — Creates a tiled image by rotating in increments of 60 degrees.
- [+ triangleKaleidoscopeFilter](<trianglekaleidoscope().md>) — Create a triangular kaleidoscope effect and then tiles the result.
- [+ triangleTileFilter](<triangletile().md>) — Tiles a triangular area of an image.
- [+ twelvefoldReflectedTileFilter](<twelvefoldreflectedtile().md>) — Creates a tiled image by rotating in increments of 30 degrees.
