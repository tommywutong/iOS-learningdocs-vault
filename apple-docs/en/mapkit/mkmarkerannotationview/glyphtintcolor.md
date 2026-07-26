---
title: glyphTintColor
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmarkerannotationview/glyphtintcolor
source_url: 'https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/glyphtintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmarkerannotationview/glyphtintcolor.json'
content_hash: 'sha256:98b3e49f94b82397'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMarkerAnnotationView](../mkmarkerannotationview.md)

# glyphTintColor

<sub>Instance Property</sub>

The color to apply to the glyph text or image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var glyphTintColor: UIColor? { get set }
```

<sub>macOS</sub>

```swift
@NSCopying var glyphTintColor: NSColor? { get set }
```

## Discussion

The default value of this property is `nil`, which applies the standard tint color for the current map style.

## See Also

### Setting the Marker Content

- [glyphText](glyphtext.md) — The text to display in the marker balloon.
- [glyphImage](glyphimage.md) — An image to display in the marker balloon.
- [selectedGlyphImage](selectedglyphimage.md) — An image to display when the user selects the marker.
