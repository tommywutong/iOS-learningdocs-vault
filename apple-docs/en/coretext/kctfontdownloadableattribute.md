---
title: kCTFontDownloadableAttribute
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontdownloadableattribute
source_url: 'https://developer.apple.com/documentation/coretext/kctfontdownloadableattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontdownloadableattribute.json'
content_hash: 'sha256:b6564b461f1e5fd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontDownloadableAttribute

<sub>Global Variable</sub>

The font downloadable state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontDownloadableAttribute: CFString
```

## Discussion

The value associated with this key is a [CFBoolean](../corefoundation/cfboolean.md).  If it is [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), Core Text attempts to download a font if necessary when matching a descriptor.

## See Also

### Constants

- [ATSFONTREF_DEFINED](atsfontref_defined.md)
- [kBSLNIdeographicHighBaseline](kbslnideographichighbaseline.md)
- [kCTAdaptiveImageProviderAttributeName](kctadaptiveimageproviderattributename.md)
- [kCTBackgroundColorAttributeName](kctbackgroundcolorattributename.md)
- [kCTBaselineClassAttributeName](kctbaselineclassattributename.md)
- [kCTBaselineClassHanging](kctbaselineclasshanging.md)
- [kCTBaselineClassIdeographicCentered](kctbaselineclassideographiccentered.md)
- [kCTBaselineClassIdeographicHigh](kctbaselineclassideographichigh.md)
- [kCTBaselineClassIdeographicLow](kctbaselineclassideographiclow.md)
- [kCTBaselineClassMath](kctbaselineclassmath.md)
- [kCTBaselineClassRoman](kctbaselineclassroman.md)
- [kCTBaselineInfoAttributeName](kctbaselineinfoattributename.md)
- [kCTBaselineOriginalFont](kctbaselineoriginalfont.md)
- [kCTBaselineReferenceFont](kctbaselinereferencefont.md)
- [kCTBaselineReferenceInfoAttributeName](kctbaselinereferenceinfoattributename.md)
