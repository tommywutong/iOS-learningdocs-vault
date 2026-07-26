---
title: legible
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/legible
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/legible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/legible.json'
content_hash: 'sha256:a055a607bc5bb65e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# legible

<sub>Type Property</sub>

A media characteristic that indicates that a track or media selection option includes legible content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let legible: AVMediaCharacteristic
```

## Discussion

Media types with this characteristic include [AVMediaTypeSubtitle](../avmediatype/subtitle.md) and [AVMediaTypeClosedCaption](../avmediatype/closedcaption.md).

## See Also

### Legible

- [AVMediaCharacteristicEasyToRead](easytoread.md) — A media characteristic that indicates a track or media selection option provides legible content that’s edited for easy reading.
- [AVMediaCharacteristicDescribesVideoForAccessibility](describesvideoforaccessibility.md) — A media characteristic that indicates the media includes audible content that describes the visual portion of the presentation.
- [AVMediaCharacteristicContainsOnlyForcedSubtitles](containsonlyforcedsubtitles.md) — A media characteristic that indicates that a track or media selection option presents only forced subtitles.
- [AVMediaCharacteristicLanguageTranslation](languagetranslation.md) — A media characteristic that indicates that a track or media selection option contains a language or dialect translation of the original content.
- [AVMediaCharacteristicTranscribesSpokenDialogForAccessibility](transcribesspokendialogforaccessibility.md) — A media characteristic that indicates that a media selection option includes legible content that transcribes spoken dialog.
