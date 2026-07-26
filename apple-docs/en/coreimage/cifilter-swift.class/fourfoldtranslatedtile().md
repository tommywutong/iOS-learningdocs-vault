---
title: fourfoldTranslatedTile()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/fourfoldtranslatedtile()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/fourfoldtranslatedtile()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/fourfoldtranslatedtile%28%29.json'
content_hash: 'sha256:67ffb3010191ee5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# fourfoldTranslatedTile()

<sub>Type Method</sub>

Creates a tiled image by applying four translation operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fourfoldTranslatedTile() -> any CIFilter & CIFourfoldTranslatedTile
```

## Return Value

The tiled image.

## Discussion

This method applies the four-fold translated tile filter to an image. The effect produces a four-way tiled image by applying four translation operations. Translation operations map the position of each element in the photo to a new position in the output image.

The four-fold translated tile filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md). This controls the source of the tile contents.
- **`angle`** — A `float` representing the direction of the tiled patten, in radians as an [NSNumber](../../foundation/nsnumber.md).
- **`width`** — A `float` representing the set width of each tile as an [NSNumber](../../foundation/nsnumber.md).
- **`acuteAngle`** — A `float` representing the primary angle for the repeating translated tile as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that performs a four-fold translated tile operation on the image:

```swift
func fourFoldTranslated(inputImage: CIImage) -> CIImage {
    let fourFoldTranslatedTile = CIFilter.fourfoldTranslatedTile()
    fourFoldTranslatedTile.inputImage = inputImage
    fourFoldTranslatedTile.center = CGPoint(x: inputImage.extent.midX, y: inputImage.extent.midY)
    fourFoldTranslatedTile.angle = 1
    fourFoldTranslatedTile.width = 400
    fourFoldTranslatedTile.acuteAngle = 1
    return fourFoldTranslatedTile.outputImage!.cropped(to: inputImage.extent)
}
```

![](../../../../attachments/abb14263a43b433b085745239ea1e141/media-4333629@2x.png)

<sub>Two photographs of a bouquet of multiple colorful flowers. The photo on the left is up close with good lighting and focus. In the photo on the right, a four-fold translate tile filter is applied, resulting in a rotated and tiled diamond pattern. The source for each tile is the center region of the left image.</sub>

## See Also

### Filters

- [+ affineClampFilter](<affineclamp().md>) — Performs a transform on the image and extends the image edges to infinity.
- [+ affineTileFilter](<affinetile().md>) — Performs a transform on the image and tiles the result.
- [+ eightfoldReflectedTileFilter](<eightfoldreflectedtile().md>) — Creates an eight-way reflected pattern.
- [+ fourfoldReflectedTileFilter](<fourfoldreflectedtile().md>) — Creates a four-way reflected pattern.
- [+ fourfoldRotatedTileFilter](<fourfoldrotatedtile().md>) — Creates a tiled image by rotating a tile in increments of 90 degrees.
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
