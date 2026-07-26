---
title: textStyleRules
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/textstylerules
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/textstylerules'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/textstylerules.json'
content_hash: 'sha256:fd3dc26b9c053415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# textStyleRules

<sub>Instance Property</sub>

An array of text style rules that specify the formatting and presentation of Web Video Text Tracks (WebVTT) subtitles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated var textStyleRules: [AVTextStyleRule]? { get set }
```

## Discussion

Text style rules apply only to WebVTT subtitles. They don’t apply to other subtitle formats and legible text.

## See Also

### Accessing text style rules

- [AVTextStyleRule](../avtextstylerule.md) — An object that represents the text styling rules to apply to a media item’s textual content.
