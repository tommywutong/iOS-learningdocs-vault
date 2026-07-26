---
title: allowedSubtitleOptionLanguages
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/allowedsubtitleoptionlanguages
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/allowedsubtitleoptionlanguages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/allowedsubtitleoptionlanguages.json'
content_hash: 'sha256:cc4e2da20a975cba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# allowedSubtitleOptionLanguages

<sub>Instance Property</sub>

An array of language codes that restrict the set of subtitle languages available to the user.

<sub>tvOS</sub>

```swift
var allowedSubtitleOptionLanguages: [String]? { get set }
```

## Discussion

When this property value is `nil` (the default), the player view controller UI presents all available subtitle options. The Auto subtitle option is only available when this property value is `nil` and [requiresFullSubtitles](requiresfullsubtitles.md) is `false`.

To allow only a restricted subset of subtitles, set this property value to an array of BCP 47 language codes. Restricting the set of subtitle languages makes the Auto option unavailable.

## See Also

### Managing subtitles

- [requiresFullSubtitles](requiresfullsubtitles.md) — A Boolean value that indicates whether the user can disable the display of subtitles.
- [mediaCharacteristicsForSupportedCustomMediaSelectionSchemes](mediacharacteristicsforsupportedcustommediaselectionschemes.md)
