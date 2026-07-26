---
title: currentLegibleOption
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentlegibleoption
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentlegibleoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentlegibleoption.json'
content_hash: 'sha256:033a7cbd5a4e6e64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionControllable](../avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md)

# currentLegibleOption

<sub>Instance Property</sub>

The currently selected subtitle or caption track.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var currentLegibleOption: AVPlaybackUserInterfaceMediaSelectionOption? { get set }
```

## Discussion

Should be one of the options in [legibleOptions](legibleoptions.md).
