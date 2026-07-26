---
title: audioDescriptionOptions
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiodescriptionoptions
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiodescriptionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiodescriptionoptions.json'
content_hash: 'sha256:4d3fa531d356f6ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionControllable](../avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md)

# audioDescriptionOptions

<sub>Instance Property</sub>

Array of available audio description track options.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var audioDescriptionOptions: [AVPlaybackUserInterfaceMediaSelectionOption] { get }
```

## Discussion

Audio description tracks provide narrated descriptions of visual content for visually impaired viewers. Audio description options are distinct from those in [audioOptions](audiooptions.md) — they provide a narration layer played alongside the primary audio rather than replacing it. Options are ordered by preference with the primary language or default audio description track typically appearing first. May be empty for content without audio description tracks.
