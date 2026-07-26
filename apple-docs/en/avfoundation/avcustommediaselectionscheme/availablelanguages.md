---
title: availableLanguages
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcustommediaselectionscheme/availablelanguages
source_url: 'https://developer.apple.com/documentation/avfoundation/avcustommediaselectionscheme/availablelanguages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcustommediaselectionscheme/availablelanguages.json'
content_hash: 'sha256:6d1aa5106e6e31ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCustomMediaSelectionScheme](../avcustommediaselectionscheme.md)

# availableLanguages

<sub>Instance Property</sub>

Provides available language choices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var availableLanguages: [String] { get }
```

## Discussion

Each string in the array is intended to be interpreted as a BCP 47 language tag.

## See Also

### Inspecting the scheme

- [selectors](selectors.md) — Provides custom settings.
- [shouldOfferLanguageSelection](shouldofferlanguageselection.md) — Indicates whether an alternative selection interface should provide a menu of language choices.
- [- mediaPresentationSettingsForSelector:complementaryToLanguage:settings:](<mediapresentationsettings(for_complementarytolanguage_settings_).md>) — Provides an array of media presentation settings that can be effective at the same time as the specified language and settings for other selectors of the receiver.
