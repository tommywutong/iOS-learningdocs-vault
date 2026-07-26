---
title: mediaCharacteristics
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectionoption/mediacharacteristics
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption/mediacharacteristics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectionoption/mediacharacteristics.json'
content_hash: 'sha256:284f8953426273f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionOption](../avplaybackuserinterfacemediaselectionoption.md)

# mediaCharacteristics

<sub>Instance Property</sub>

The media characteristics describing accessibility features and content properties of this option. Common values include `AVMediaCharacteristicContainsOnlyForcedSubtitles`, `AVMediaCharacteristicTranscribesSpokenDialogForAccessibility`, and `AVMediaCharacteristicDescribesMusicAndSoundForAccessibility`. May be empty if no characteristics apply.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var mediaCharacteristics: [AVMediaCharacteristic] { get }
```
