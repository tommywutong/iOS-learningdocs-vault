---
title: containsOnlyForcedSubtitles
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/containsonlyforcedsubtitles
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/containsonlyforcedsubtitles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/containsonlyforcedsubtitles.json'
content_hash: 'sha256:e835fdd50bb3f3cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# containsOnlyForcedSubtitles

<sub>Type Property</sub>

A media characteristic that indicates that a track or media selection option presents only forced subtitles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let containsOnlyForcedSubtitles: AVMediaCharacteristic
```

## Discussion

The value of this characteristic is `public.subtitles.forced-only`.

The system infers this characteristic from the format description of the associated track.

## See Also

### Legible

- [AVMediaCharacteristicLegible](legible.md) — A media characteristic that indicates that a track or media selection option includes legible content.
- [AVMediaCharacteristicEasyToRead](easytoread.md) — A media characteristic that indicates a track or media selection option provides legible content that’s edited for easy reading.
- [AVMediaCharacteristicDescribesVideoForAccessibility](describesvideoforaccessibility.md) — A media characteristic that indicates the media includes audible content that describes the visual portion of the presentation.
- [AVMediaCharacteristicLanguageTranslation](languagetranslation.md) — A media characteristic that indicates that a track or media selection option contains a language or dialect translation of the original content.
- [AVMediaCharacteristicTranscribesSpokenDialogForAccessibility](transcribesspokendialogforaccessibility.md) — A media characteristic that indicates that a media selection option includes legible content that transcribes spoken dialog.
