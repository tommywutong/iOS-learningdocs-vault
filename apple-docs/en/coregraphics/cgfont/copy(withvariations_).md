---
title: 'copy(withVariations:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfont/copy(withvariations:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/copy(withvariations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/copy%28withvariations%3A%29.json'
content_hash: 'sha256:1344a93857252bb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# copy(withVariations:)

<sub>Instance Method</sub>

Creates a copy of a font using a variation specification dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy(withVariations variations: CFDictionary?) -> CGFont?
```

## Parameters

- `variations` — A variation specification dictionary that contains keys corresponding to the variation axis names of the font. Each key in the dictionary is a variation axis name. The value for each key is the value specified for that particular variation axis represented as a CFNumber object. If a variation axis name is not specified in `variations`, then the current value from `font` is used.

## Return Value

The font object.

## See Also

### Working with Variations

- [CGFontCopyVariations](variations.md) — Returns the variation specification dictionary for a font.
- [CGFontCopyVariationAxes](variationaxes.md) — Returns an array of the variation axis dictionaries for a font.
- [Font Variation Axis Keys](../font-variation-axis-keys.md) — Keys used for a font variation axis dictionary.
