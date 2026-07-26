---
title: trackGroups
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/trackgroups
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/trackgroups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/trackgroups.json'
content_hash: 'sha256:461a8ebeea45a29c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# trackGroups

<sub>Instance Property</sub>

The track groups an asset contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var trackGroups: [AVAssetTrackGroup] { get }
```

## Discussion

This value is an empty array if the composition has no track groups.
