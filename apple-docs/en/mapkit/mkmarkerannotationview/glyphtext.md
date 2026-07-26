---
title: glyphText
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmarkerannotationview/glyphtext
source_url: 'https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/glyphtext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmarkerannotationview/glyphtext.json'
content_hash: 'sha256:c4eb234ce7b01720'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMarkerAnnotationView](../mkmarkerannotationview.md)

# glyphText

<sub>Instance Property</sub>

The text to display in the marker balloon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var glyphText: String? { get set }
```

## Discussion

Use this property or the [glyphText](glyphtext.md) property to specify the marker balloon content. If you specify both an image and text, MapKit displays the text.

MapKit limits the amount of space available for displaying your glyph text. Specify no more than two or three characters for any strings you assign to this property.

## See Also

### Setting the Marker Content

- [glyphImage](glyphimage.md) — An image to display in the marker balloon.
- [glyphTintColor](glyphtintcolor.md) — The color to apply to the glyph text or image.
- [selectedGlyphImage](selectedglyphimage.md) — An image to display when the user selects the marker.
