---
title: variationAxes
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfont/variationaxes
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/variationaxes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/variationaxes.json'
content_hash: 'sha256:6c54ea1e5797f5cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# variationAxes

<sub>Instance Property</sub>

Returns an array of the variation axis dictionaries for a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var variationAxes: CFArray? { get }
```

## Discussion

A variation axis is a range included in a font by the font designer that allows a font to produce different type styles. Each variation axis dictionary contains key-value pairs that specify the variation axis name and the minimum, maximum, and default values for that variation axis.

## See Also

### Working with Variations

- [CGFontCreateCopyWithVariations](<copy(withvariations_).md>) — Creates a copy of a font using a variation specification dictionary.
- [CGFontCopyVariations](variations.md) — Returns the variation specification dictionary for a font.
- [Font Variation Axis Keys](../font-variation-axis-keys.md) — Keys used for a font variation axis dictionary.
