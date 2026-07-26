---
title: variationAxisDefaultValue
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfont/variationaxisdefaultvalue
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/variationaxisdefaultvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/variationaxisdefaultvalue.json'
content_hash: 'sha256:1d3d957305ffa0d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# variationAxisDefaultValue

<sub>Type Property</sub>

The key used to obtain the default variation axis value from a variation axis dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let variationAxisDefaultValue: CFString
```

## Discussion

The value obtained with this key is a [CFNumber](../../corefoundation/cfnumber.md) that specifies the default value of the variation axis.

## See Also

### Constants

- [kCGFontVariationAxisName](variationaxisname.md) — The key used to obtain the variation axis name from a variation axis dictionary.
- [kCGFontVariationAxisMinValue](variationaxisminvalue.md) — The key used to obtain the minimum variation axis value from a variation axis dictionary.
- [kCGFontVariationAxisMaxValue](variationaxismaxvalue.md) — The key used to obtain the maximum variation axis value from a variation axis dictionary.
