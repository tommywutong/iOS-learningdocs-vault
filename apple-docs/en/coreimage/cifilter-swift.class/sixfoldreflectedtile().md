---
title: sixfoldReflectedTile()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/sixfoldreflectedtile()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/sixfoldreflectedtile()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/sixfoldreflectedtile%28%29.json'
content_hash: 'sha256:5db9a64ef3c72833'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# sixfoldReflectedTile()

<sub>Type Method</sub>

Produces a tiled image from a source image by applying a six-way reflected symmetry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func sixfoldReflectedTile() -> any CIFilter & CISixfoldReflectedTile
```

## Return Value

The tiled image.

## Discussion

This filter produces a tiled image from a source image by applying a six-way reflected symmetry.

The six-fold reflected tile filter uses the following properties:

- **`inputImage`** — An image with the type [CIImage](../ciimage.md).
- **`center`** — A set of coordinates marking the center of the image as a [CGPoint](../../corefoundation/cgpoint.md).
- **`angle`** — A `float` representing the direction of distortion , in radians as an [NSNumber](../../foundation/nsnumber.md).
- **`width`** — A `float` representing the set width of each tile as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that results in a six-fold pattern repeated and angled for distortion:

```swift
func sixFoldReflected(inputImage: CIImage) -> CIImage {
    let sixFoldReflectedTile = CIFilter.sixfoldReflectedTile()
    sixFoldReflectedTile.inputImage = inputImage
    sixFoldReflectedTile.center = CGPoint(x: 150, y: 150)
    sixFoldReflectedTile.angle = 0
    sixFoldReflectedTile.width = 100
    return sixFoldReflectedTile.outputImage!
}
```

![](../../../../attachments/ba9b2b0b4658e526cc5879ec352c051a/media-3599882@2x.png)

<sub>Two photographs. The photo on the left is of a bouquet of colorful flowers up close with good lighting and focus. In the photo on the right, a six-fold reflected tile filter is applied, resulting in triangles, each with a portion of the image containing white and purple petals, tiled throughout the entire photo.</sub>

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
- [+ sixfoldRotatedTileFilter](<sixfoldrotatedtile().md>) — Creates a tiled image by rotating in increments of 60 degrees.
- [+ triangleKaleidoscopeFilter](<trianglekaleidoscope().md>) — Create a triangular kaleidoscope effect and then tiles the result.
- [+ triangleTileFilter](<triangletile().md>) — Tiles a triangular area of an image.
- [+ twelvefoldReflectedTileFilter](<twelvefoldreflectedtile().md>) — Creates a tiled image by rotating in increments of 30 degrees.
