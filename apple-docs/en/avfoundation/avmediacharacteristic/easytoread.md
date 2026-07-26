---
title: easyToRead
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic/easytoread
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/easytoread'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/easytoread.json'
content_hash: 'sha256:7261acb50a0f6250'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaCharacteristic](../avmediacharacteristic.md)

# easyToRead

<sub>Type Property</sub>

A media characteristic that indicates a track or media selection option provides legible content that’s edited for easy reading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let easyToRead: AVMediaCharacteristic
```

## Discussion

Closed caption tracks that carry “easy reader” captions, as the CEA-608 specification defines, should have this characteristic.

The value of this characteristic is `public.easy-to-read`.

For QuickTime movies and `.m4v` files, a track has this characteristic only if the media’s author tags it that way.

## See Also

### Legible

- [AVMediaCharacteristicLegible](legible.md) — A media characteristic that indicates that a track or media selection option includes legible content.
- [AVMediaCharacteristicDescribesVideoForAccessibility](describesvideoforaccessibility.md) — A media characteristic that indicates the media includes audible content that describes the visual portion of the presentation.
- [AVMediaCharacteristicContainsOnlyForcedSubtitles](containsonlyforcedsubtitles.md) — A media characteristic that indicates that a track or media selection option presents only forced subtitles.
- [AVMediaCharacteristicLanguageTranslation](languagetranslation.md) — A media characteristic that indicates that a track or media selection option contains a language or dialect translation of the original content.
- [AVMediaCharacteristicTranscribesSpokenDialogForAccessibility](transcribesspokendialogforaccessibility.md) — A media characteristic that indicates that a media selection option includes legible content that transcribes spoken dialog.
