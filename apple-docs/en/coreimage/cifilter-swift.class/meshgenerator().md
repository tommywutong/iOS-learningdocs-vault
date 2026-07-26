---
title: meshGenerator()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/meshgenerator()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/meshgenerator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/meshgenerator%28%29.json'
content_hash: 'sha256:563dbf8a13544c71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# meshGenerator()

<sub>Type Method</sub>

Generates a pattern made from an array of line segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func meshGenerator() -> any CIFilter & CIMeshGenerator
```

## Return Value

The generated image.

## Discussion

This method generates a mesh generator image. The effect uses an array of line segments to create the resulting image.

The mesh generator filter uses the following properties:

- **`inputMesh`** — An `array` of line segments stored as an array of [CIVector](../civector.md), each containing a start point and end point.
- **`color`** — A [CIColor](../cicolor.md) representing the color used to make the mesh.
- **`width`** — A `float` representing the width of the line segments as an [NSNumber](../../foundation/nsnumber.md)

The following code creates a filter that generates a green star made from mesh segments:

```swift
func mesh(mesh: NSdata) -> CIImage {
    let meshGenerator = CIFilter.meshGenerator()
    meshGenerator.color = CIColor.green
    meshGenerator.width = 3
    meshGenerator.inputmesh = mesh
    return meshGenerator.outputImage!
}
```

![A set of green mesh line segments connected together to draw a five-point star pattern.](../../../../attachments/5465d1956143e017dbc430fc7bb49f3c/media-3590974@2x.png)

## See Also

### Filters

- [+ attributedTextImageGeneratorFilter](<attributedtextimagegenerator().md>) — Generates an attributed-text image.
- [+ aztecCodeGeneratorFilter](<azteccodegenerator().md>) — Generates a low-density barcode.
- [+ barcodeGeneratorFilter](<barcodegenerator().md>) — Generates a barcode as an image from the descriptor.
- [+ blurredRectangleGeneratorFilter](<blurredrectanglegenerator().md>) — Generates a blurred rectangle.
- [+ checkerboardGeneratorFilter](<checkerboardgenerator().md>) — Generates a checkerboard image.
- [+ code128BarcodeGeneratorFilter](<code128barcodegenerator().md>) — Generates a high-density, linear barcode.
- [+ lenticularHaloGeneratorFilter](<lenticularhalogenerator().md>) — Generates a lenticular halo image.
- [+ PDF417BarcodeGenerator](<pdf417barcodegenerator().md>) — Generates a high-density linear barcode.
- [+ QRCodeGenerator](<qrcodegenerator().md>) — Generates a quick response (QR) code image.
- [+ randomGeneratorFilter](<randomgenerator().md>) — Generates a random filter image.
- [+ roundedRectangleGeneratorFilter](<roundedrectanglegenerator().md>) — Generates a rounded rectangle image.
- [+ roundedRectangleStrokeGeneratorFilter](<roundedrectanglestrokegenerator().md>) — Creates an image containing the outline of a rounded rectangle.
- [+ starShineGeneratorFilter](<starshinegenerator().md>) — Generates a star-shine image.
- [+ stripesGeneratorFilter](<stripesgenerator().md>) — Generates a line of stripes as an image
- [+ sunbeamsGeneratorFilter](<sunbeamsgenerator().md>) — Generates an image resembling the sun.
