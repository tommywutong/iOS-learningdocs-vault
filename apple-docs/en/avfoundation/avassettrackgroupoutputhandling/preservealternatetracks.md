---
title: preserveAlternateTracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrackgroupoutputhandling/preservealternatetracks
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackgroupoutputhandling/preservealternatetracks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackgroupoutputhandling/preservealternatetracks.json'
content_hash: 'sha256:3cb42088a047abc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrackGroupOutputHandling](../avassettrackgroupoutputhandling.md)

# preserveAlternateTracks

<sub>Type Property</sub>

A policy that passes through alternate audio tracks from the source asset during export.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var preserveAlternateTracks: AVAssetTrackGroupOutputHandling { get }
```

## Discussion

Setting this policy tells the session to export alternate tracks in a track group without reencoding them.
