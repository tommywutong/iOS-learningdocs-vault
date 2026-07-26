---
title: kCTFontFeatureSelectorDefaultKey
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontfeatureselectordefaultkey
source_url: 'https://developer.apple.com/documentation/coretext/kctfontfeatureselectordefaultkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontfeatureselectordefaultkey.json'
content_hash: 'sha256:90fbe3048885f681'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontFeatureSelectorDefaultKey

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontFeatureSelectorDefaultKey: CFString
```

## Discussion

Key to be used with a selector dictionary to get the default indicator for the selector. This value is a `CFBooleanRef` object, which if present and true, indicates that this selector is the default setting for the current feature type.

## See Also

### Constants

- [kCTFontFeatureTypeIdentifierKey](kctfontfeaturetypeidentifierkey.md)
- [kCTFontFeatureTypeNameKey](kctfontfeaturetypenamekey.md)
- [kCTFontFeatureTypeExclusiveKey](kctfontfeaturetypeexclusivekey.md)
- [kCTFontFeatureTypeSelectorsKey](kctfontfeaturetypeselectorskey.md)
- [kCTFontFeatureSelectorIdentifierKey](kctfontfeatureselectoridentifierkey.md)
- [kCTFontFeatureSelectorNameKey](kctfontfeatureselectornamekey.md)
- [kCTFontFeatureSelectorSettingKey](kctfontfeatureselectorsettingkey.md)
- [kCTFontFeatureSampleTextKey](kctfontfeaturesampletextkey.md)
- [kCTFontFeatureTooltipTextKey](kctfontfeaturetooltiptextkey.md)
