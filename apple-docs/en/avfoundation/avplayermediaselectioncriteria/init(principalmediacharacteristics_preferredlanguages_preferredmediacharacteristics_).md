---
title: 'init(principalMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayermediaselectioncriteria/init(principalmediacharacteristics:preferredlanguages:preferredmediacharacteristics:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/init(principalmediacharacteristics:preferredlanguages:preferredmediacharacteristics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayermediaselectioncriteria/init%28principalmediacharacteristics%3Apreferredlanguages%3Apreferredmediacharacteristics%3A%29.json'
content_hash: 'sha256:39e4526ef0f0b1d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerMediaSelectionCriteria](../avplayermediaselectioncriteria.md)

# init(principalMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:)

<sub>Initializer</sub>

Creates media selection criteria with the principal media characteristics, and preferred languages and media characteristics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(principalMediaCharacteristics: [AVMediaCharacteristic]?, preferredLanguages: [String]?, preferredMediaCharacteristics: [AVMediaCharacteristic]?)
```

## Parameters

- `principalMediaCharacteristics` — An array of media characteristics that are essential to selecting media with the characteristic. This value may be `nil`.

- `preferredLanguages` — An array of language identifier strings, in order of preference. This value may be `nil`.

- `preferredMediaCharacteristics` — An array of media characteristics, in order of preference. This value may be `nil`.

## Discussion

Principal media characteristics, when present, override language preferences when making selections within a specific media selection group. However, language preferences may still pertain to selections in other groups. For example, the system may consider language preferences when choosing whether to select nonforced subtitles for translation purposes.

## See Also

### Creating media selection criteria

- [- initWithPreferredLanguages:preferredMediaCharacteristics:](<init(preferredlanguages_preferredmediacharacteristics_).md>) — Creates media selection criteria with the preferred languages and media characteristics.
