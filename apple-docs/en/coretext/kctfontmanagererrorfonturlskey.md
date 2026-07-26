---
title: kCTFontManagerErrorFontURLsKey
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontmanagererrorfonturlskey
source_url: 'https://developer.apple.com/documentation/coretext/kctfontmanagererrorfonturlskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontmanagererrorfonturlskey.json'
content_hash: 'sha256:20447f787b69d176'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontManagerErrorFontURLsKey

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontManagerErrorFontURLsKey: CFString
```

## Discussion

User info key to be used with CFError references returned from registration functions. The value associated with this key in the user info dictionary of a CFError object is a CFArray of font URLs that failed with the given error.

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
