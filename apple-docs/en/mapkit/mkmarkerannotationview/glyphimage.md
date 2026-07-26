---
title: glyphImage
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmarkerannotationview/glyphimage
source_url: 'https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/glyphimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmarkerannotationview/glyphimage.json'
content_hash: 'sha256:a5f06474e621c613'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMarkerAnnotationView](../mkmarkerannotationview.md)

# glyphImage

<sub>Instance Property</sub>

An image to display in the marker balloon.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var glyphImage: UIImage? { get set }
```

<sub>macOS</sub>

```swift
@NSCopying var glyphImage: NSImage? { get set }
```

## Discussion

Use this property or the [glyphText](glyphtext.md) property to specify the marker balloon content. If you specify both an image and text, MapKit displays the text.

MapKit displays the glyph image when the marker is in the normal state. Create glyph images as template images so that MapKit can apply the glyph tint color to the image. Normally, you set the size of this image to 20 by 20 points on iOS and 40 by 40 points on tvOS. However, if you don’t provide a separate selected image in the [selectedGlyphImage](selectedglyphimage.md) property, make the size of this image 40 by 40 points on iOS and 60 by 40 points on tvOS instead. MapKit scales images that are larger or smaller than those sizes.

## See Also

### Setting the Marker Content

- [glyphText](glyphtext.md) — The text to display in the marker balloon.
- [glyphTintColor](glyphtintcolor.md) — The color to apply to the glyph text or image.
- [selectedGlyphImage](selectedglyphimage.md) — An image to display when the user selects the marker.
