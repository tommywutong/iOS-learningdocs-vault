---
title: currentAudioOption
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentaudiooption
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentaudiooption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentaudiooption.json'
content_hash: 'sha256:97af4944854cbff6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionControllable](../avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md)

# currentAudioOption

<sub>Instance Property</sub>

The currently selected audio track.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var currentAudioOption: AVPlaybackUserInterfaceMediaSelectionOption? { get set }
```

## Discussion

Should be one of the options in [audioOptions](audiooptions.md).
