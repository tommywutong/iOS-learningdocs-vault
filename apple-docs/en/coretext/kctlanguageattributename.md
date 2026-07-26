---
title: kCTLanguageAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctlanguageattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctlanguageattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctlanguageattributename.json'
content_hash: 'sha256:2049df1be4764646'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTLanguageAttributeName

<sub>Global Variable</sub>

The name of the text language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTLanguageAttributeName: CFString
```

## Discussion

The value of this attribute must be a [CFString](../corefoundation/cfstring.md) containing a language identifier conforming to [UTS #35](http://unicode.org/reports/tr35/). The default is unset. When this attribute is set to a valid identifier, it will be used to select localized glyphs (if supported by the font), and locale-specific line-breaking rules.

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
