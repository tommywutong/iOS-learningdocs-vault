---
title: variations
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfont/variations
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/variations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/variations.json'
content_hash: 'sha256:a21e6d790c94f4f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# variations

<sub>Instance Property</sub>

Returns the variation specification dictionary for a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var variations: CFDictionary? { get }
```

## Discussion

The variation specification dictionary contains keys that correspond to the variation axis names of the font. Each key is a variation axis name. The value for each key is the value specified for that particular variation axis represented as a [CFNumber](../../corefoundation/cfnumber.md) object.

## See Also

### Working with Variations

- [CGFontCreateCopyWithVariations](<copy(withvariations_).md>) — Creates a copy of a font using a variation specification dictionary.
- [CGFontCopyVariationAxes](variationaxes.md) — Returns an array of the variation axis dictionaries for a font.
- [Font Variation Axis Keys](../font-variation-axis-keys.md) — Keys used for a font variation axis dictionary.
