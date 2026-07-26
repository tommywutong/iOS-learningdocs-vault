---
title: isPlayable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+（16.0 起废弃）, iPadOS 4.3+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/isplayable
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/isplayable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/isplayable.json'
content_hash: 'sha256:ba75c51fed672a9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# isPlayable

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset has playable content.

> [!warning] Deprecated
> Load the value of [isPlayable](../avpartialasyncproperty/isplayable-45h5v.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var isPlayable: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you can use the asset to create an [AVPlayerItem](../avplayeritem.md).
