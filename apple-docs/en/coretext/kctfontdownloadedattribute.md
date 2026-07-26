---
title: kCTFontDownloadedAttribute
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontdownloadedattribute
source_url: 'https://developer.apple.com/documentation/coretext/kctfontdownloadedattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontdownloadedattribute.json'
content_hash: 'sha256:d1bacfb26f46441c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontDownloadedAttribute

<sub>Global Variable</sub>

The download state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontDownloadedAttribute: CFString
```

## Discussion

The value associated with this key is a [CFBoolean](../corefoundation/cfboolean.md).  If it is [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), corresponding Font Asset has been downloaded.

> [!note] Note
> It may still be necessary to call appropriate API in order to use the font in the Font Asset.

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
