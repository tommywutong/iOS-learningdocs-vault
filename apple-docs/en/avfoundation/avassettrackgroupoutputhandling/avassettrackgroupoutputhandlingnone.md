---
title: AVAssetTrackGroupOutputHandlingNone
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrackgroupoutputhandling/avassettrackgroupoutputhandlingnone
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackgroupoutputhandling/avassettrackgroupoutputhandlingnone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackgroupoutputhandling/avassettrackgroupoutputhandlingnone.json'
content_hash: 'sha256:6a6a2899940dd71c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrackGroupOutputHandling](../avassettrackgroupoutputhandling.md)

# AVAssetTrackGroupOutputHandlingNone

<sub>Enumeration Case</sub>

A policy that doesn’t pass through alternate audio tracks from the source asset during export.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
AVAssetTrackGroupOutputHandlingNone
```

## Discussion

Setting this policy tells the session to disregard alternate track group assignments in the original asset.

## See Also

### Policies

- [AVAssetTrackGroupOutputHandlingPreserveAlternateTracks](preservealternatetracks.md) — A policy that passes through alternate audio tracks from the source asset during export.
- [AVAssetTrackGroupOutputHandlingDefaultPolicy](avassettrackgroupoutputhandlingdefaultpolicy.md) — The default track group output handling policy.
