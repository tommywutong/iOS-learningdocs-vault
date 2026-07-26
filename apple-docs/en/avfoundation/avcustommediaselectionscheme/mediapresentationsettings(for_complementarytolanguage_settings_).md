---
title: 'mediaPresentationSettings(for:complementaryToLanguage:settings:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcustommediaselectionscheme/mediapresentationsettings(for:complementarytolanguage:settings:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcustommediaselectionscheme/mediapresentationsettings(for:complementarytolanguage:settings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcustommediaselectionscheme/mediapresentationsettings%28for%3Acomplementarytolanguage%3Asettings%3A%29.json'
content_hash: 'sha256:021a7a73ec6f57dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCustomMediaSelectionScheme](../avcustommediaselectionscheme.md)

# mediaPresentationSettings(for:complementaryToLanguage:settings:)

<sub>Instance Method</sub>

Provides an array of media presentation settings that can be effective at the same time as the specified language and settings for other selectors of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mediaPresentationSettings(for selector: AVMediaPresentationSelector, complementaryToLanguage language: String?, settings: [AVMediaPresentationSetting]) -> [AVMediaPresentationSetting]
```

## Parameters

- `selector` — The AVMediaPresentationSelector for which complementary settings are requested.

- `language` — A BCP 47 language tag chosen among the availableLanguages of the receiver. If no language setting pertains, can be nil.

- `settings` — A collection of AVMediaPresentationSettings provided by selectors of the receiver other than the specified selector. Because no two AVMediaPresentationSettings of the same AVMediaPresentationSelector are complementary, an empty array will be returned if you specify more than one setting for any selector.

## Discussion

If the content is authored to provide a collection of AVMediaSelectionOptions that include one or more with all of the combinations of media characteristics of the specified AVMediaPresentationSettings together with all of the settings of the specified AVMediaPresentationSelector, this method will return all of the settings for that selector. However, if one or more of the available combinations are not possessed by any of the AVMediaSelectionOptions, it will return fewer.

## See Also

### Inspecting the scheme

- [availableLanguages](availablelanguages.md) — Provides available language choices.
- [selectors](selectors.md) — Provides custom settings.
- [shouldOfferLanguageSelection](shouldofferlanguageselection.md) — Indicates whether an alternative selection interface should provide a menu of language choices.
