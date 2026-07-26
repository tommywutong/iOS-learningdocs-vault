---
title: kCTFontManagerRegisteredFontsChangedNotification
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontmanagerregisteredfontschangednotification
source_url: 'https://developer.apple.com/documentation/coretext/kctfontmanagerregisteredfontschangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontmanagerregisteredfontschangednotification.json'
content_hash: 'sha256:e74041ac31690bfa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontManagerRegisteredFontsChangedNotification

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontManagerRegisteredFontsChangedNotification: CFString
```

## Discussion

This is the string to use as the notification name when subscribing to Core Text Font Manager notifications. This notification is posted when fonts are added to the font registry. The client is responsible for registered with the distributed notification center to receive notifications for changes to the session or user scopes, and with a local notification center for changes to the process scope.

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
