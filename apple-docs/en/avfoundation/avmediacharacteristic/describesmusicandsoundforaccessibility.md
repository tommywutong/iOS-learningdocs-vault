---
title: describesMusicAndSoundForAccessibility
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/describesmusicandsoundforaccessibility
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/describesmusicandsoundforaccessibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/describesmusicandsoundforaccessibility.json'
content_hash: 'sha256:88389366a32362b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# describesMusicAndSoundForAccessibility

<sub>Type Property</sub>

A media characteristic that indicates that a track or media selection option includes legible content in the language of its specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let describesMusicAndSoundForAccessibility: AVMediaCharacteristic
```

## Discussion

Legible media options may include transcriptions of spoken dialog and descriptions of music and sound effects.

The value of this characteristic is `public.accessibility.describes-music-and-sound`.

For QuickTime movies and `.m4v` files, a media option has this characteristic only if the media’s author tags it that way.

## See Also

### Audible

- [AVMediaCharacteristicAudible](audible.md) — A media characteristic that indicates that a track or media selection option includes audible content.
- [AVMediaCharacteristicDubbedTranslation](dubbedtranslation.md) — A media characteristic that indicates that a track or media selection option contains audio language or dialect translation of the original content.
- [AVMediaCharacteristicVoiceOverTranslation](voiceovertranslation.md) — A media characteristic that indicates that a track or media selection option contains a language translation and verbal interpretation of spoken dialog.
- [AVMediaCharacteristicEnhancesSpeechIntelligibility](enhancesspeechintelligibility.md) — A media characteristic that indicates a track or media selection option includes audio processed to enhance the intelligibility of speech.
- [AVMediaCharacteristicTactileMinimal](tactileminimal.md) — A media characteristic that indicates that a track or media selection option includes haptic content.
