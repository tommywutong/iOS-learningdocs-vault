---
title: language
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectionoption/language
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption/language'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectionoption/language.json'
content_hash: 'sha256:dddf4a3327dcba08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionOption](../avplaybackuserinterfacemediaselectionoption.md)

# language

<sub>Instance Property</sub>

The language of this media selection option.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var language: Locale.Language? { get }
```

## Discussion

This standardized tag provides detailed language information including region, script, and variants. Returns `nil` for language-neutral content such as music-only audio tracks, sound effects, or visual-only subtitles without spoken content.
