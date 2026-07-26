---
title: legibleOptions
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/legibleoptions
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/legibleoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/legibleoptions.json'
content_hash: 'sha256:e8ba787124b977e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionControllable](../avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md)

# legibleOptions

<sub>Instance Property</sub>

Array of available subtitle and caption track options.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var legibleOptions: [AVPlaybackUserInterfaceMediaSelectionOption] { get }
```

## Discussion

This includes text overlays in different languages, closed captions for accessibility, forced narrative subtitles, and sign language interpretation tracks. May be empty for content without text tracks.
