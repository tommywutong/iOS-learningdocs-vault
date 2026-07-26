---
title: requiresFullSubtitles
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/requiresfullsubtitles
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/requiresfullsubtitles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/requiresfullsubtitles.json'
content_hash: 'sha256:c38b8be8177f4680'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# requiresFullSubtitles

<sub>Instance Property</sub>

A Boolean value that indicates whether the user can disable the display of subtitles.

<sub>tvOS</sub>

```swift
var requiresFullSubtitles: Bool { get set }
```

## Discussion

When this property value is `true`, the subtitle menu doesn’t present the Off or Auto options, because subtitles are always displayed, if available.

The default value is `false`.

## See Also

### Managing subtitles

- [allowedSubtitleOptionLanguages](allowedsubtitleoptionlanguages.md) — An array of language codes that restrict the set of subtitle languages available to the user.
- [mediaCharacteristicsForSupportedCustomMediaSelectionSchemes](mediacharacteristicsforsupportedcustommediaselectionschemes.md)
