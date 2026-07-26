---
title: glideReflectedTile()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/glidereflectedtile()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/glidereflectedtile()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/glidereflectedtile%28%29.json'
content_hash: 'sha256:1cb603ab523dcd24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# glideReflectedTile()

<sub>Type Method</sub>

Tiles an image by rotating and reflecting a tile from the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func glideReflectedTile() -> any CIFilter & CIGlideReflectedTile
```

## Return Value

The tiled image.

## Discussion

This method applies the glide reflected tile filter to an image. The effect produces a tiled image by rotating and reflecting a tile from the input image.

The glide reflected tile filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md).
- **`angle`** — A `float` representing the direction of distortion, in radians as an [NSNumber](../../foundation/nsnumber.md).
- **`width`** — A `float` representing the set width of each tile as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that results in flipping the image and then tiling the result:

```swift
func glideReflected(inputImage: CIImage) -> CIImage {
    let glideReflectedTile = CIFilter.glideReflectedTile()
    glideReflectedTile.inputImage = inputImage
    glideReflectedTile.center = CGPoint(x: 150, y: 150)
    glideReflectedTile.angle = 10
    glideReflectedTile.width = 10
    return glideReflectedTile.outputImage!
}
```

![](../../../../attachments/e7736aef7eade0673b94b753fa406c5b/media-3599883@2x.png)

<sub>Two photographs of a bouquet of multiple colorful flowers photographed up close with good lighting and focus. In the photo on the right, a glide reflected tile filter is applied, resulting in a portion of the image containing purple, white and pink petals becoming tiled with every other tile reflected.</sub>

## See Also

### Filters

- [+ affineClampFilter](<affineclamp().md>) — Performs a transform on the image and extends the image edges to infinity.
- [+ affineTileFilter](<affinetile().md>) — Performs a transform on the image and tiles the result.
- [+ eightfoldReflectedTileFilter](<eightfoldreflectedtile().md>) — Creates an eight-way reflected pattern.
- [+ fourfoldReflectedTileFilter](<fourfoldreflectedtile().md>) — Creates a four-way reflected pattern.
- [+ fourfoldRotatedTileFilter](<fourfoldrotatedtile().md>) — Creates a tiled image by rotating a tile in increments of 90 degrees.
- [+ fourfoldTranslatedTileFilter](<fourfoldtranslatedtile().md>) — Creates a tiled image by applying four translation operations.
- [+ kaleidoscopeFilter](<kaleidoscope().md>) — Creates a 12-way kaleidoscopic image from an image.
- [+ opTileFilter](<optile().md>) — Produces an effect that mimics a style of visual art that uses optical illusions.
- [+ parallelogramTileFilter](<parallelogramtile().md>) — Warps the image to create a parallelogram and tiles the result.
- [+ perspectiveTileFilter](<perspectivetile().md>) — Tiles an image by adjusting the perspective of the image.
- [+ sixfoldReflectedTileFilter](<sixfoldreflectedtile().md>) — Produces a tiled image from a source image by applying a six-way reflected symmetry.
- [+ sixfoldRotatedTileFilter](<sixfoldrotatedtile().md>) — Creates a tiled image by rotating in increments of 60 degrees.
- [+ triangleKaleidoscopeFilter](<trianglekaleidoscope().md>) — Create a triangular kaleidoscope effect and then tiles the result.
- [+ triangleTileFilter](<triangletile().md>) — Tiles a triangular area of an image.
- [+ twelvefoldReflectedTileFilter](<twelvefoldreflectedtile().md>) — Creates a tiled image by rotating in increments of 30 degrees.
