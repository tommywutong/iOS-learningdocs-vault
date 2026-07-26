---
title: kCTFontFeatureSelectorSettingKey
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontfeatureselectorsettingkey
source_url: 'https://developer.apple.com/documentation/coretext/kctfontfeatureselectorsettingkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontfeatureselectorsettingkey.json'
content_hash: 'sha256:6f94c4e303925025'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontFeatureSelectorSettingKey

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontFeatureSelectorSettingKey: CFString
```

## Discussion

Key to be used with a selector dictionary to get or specify the current setting for the selector. This value is a `CFBooleanRef` object to indicate whether this selector is on or off. If this key is not present, the default setting is used.

## See Also

### Constants

- [kCTFontFeatureTypeIdentifierKey](kctfontfeaturetypeidentifierkey.md)
- [kCTFontFeatureTypeNameKey](kctfontfeaturetypenamekey.md)
- [kCTFontFeatureTypeExclusiveKey](kctfontfeaturetypeexclusivekey.md)
- [kCTFontFeatureTypeSelectorsKey](kctfontfeaturetypeselectorskey.md)
- [kCTFontFeatureSelectorIdentifierKey](kctfontfeatureselectoridentifierkey.md)
- [kCTFontFeatureSelectorNameKey](kctfontfeatureselectornamekey.md)
- [kCTFontFeatureSelectorDefaultKey](kctfontfeatureselectordefaultkey.md)
- [kCTFontFeatureSampleTextKey](kctfontfeaturesampletextkey.md)
- [kCTFontFeatureTooltipTextKey](kctfontfeaturetooltiptextkey.md)
