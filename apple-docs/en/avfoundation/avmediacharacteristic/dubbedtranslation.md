---
title: dubbedTranslation
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/dubbedtranslation
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/dubbedtranslation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/dubbedtranslation.json'
content_hash: 'sha256:9cb525da9f0fd089'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# dubbedTranslation

<sub>Type Property</sub>

A media characteristic that indicates that a track or media selection option contains audio language or dialect translation of the original content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let dubbedTranslation: AVMediaCharacteristic
```

## Discussion

The value of this characteristic is `public.translation.dubbed`.

For QuickTime movies and `.m4v` files, a media option has this characteristic only if the media’s author tags it that way.

## See Also

### Audible

- [AVMediaCharacteristicAudible](audible.md) — A media characteristic that indicates that a track or media selection option includes audible content.
- [AVMediaCharacteristicVoiceOverTranslation](voiceovertranslation.md) — A media characteristic that indicates that a track or media selection option contains a language translation and verbal interpretation of spoken dialog.
- [AVMediaCharacteristicEnhancesSpeechIntelligibility](enhancesspeechintelligibility.md) — A media characteristic that indicates a track or media selection option includes audio processed to enhance the intelligibility of speech.
- [AVMediaCharacteristicDescribesMusicAndSoundForAccessibility](describesmusicandsoundforaccessibility.md) — A media characteristic that indicates that a track or media selection option includes legible content in the language of its specified locale.
- [AVMediaCharacteristicTactileMinimal](tactileminimal.md) — A media characteristic that indicates that a track or media selection option includes haptic content.
