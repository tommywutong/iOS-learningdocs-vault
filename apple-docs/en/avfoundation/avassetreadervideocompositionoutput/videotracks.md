---
title: videoTracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreadervideocompositionoutput/videotracks
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/videotracks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadervideocompositionoutput/videotracks.json'
content_hash: 'sha256:0d663606f0789aec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderVideoCompositionOutput](../avassetreadervideocompositionoutput.md)

# videoTracks

<sub>Instance Property</sub>

The tracks from which the output reads the composited video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var videoTracks: [AVAssetTrack] { get }
```

## Discussion

The array contains [AVAssetTrack](../avassettrack.md) objects owned by the target asset reader’s asset.

## See Also

### Inspecting an output

- [videoSettings](videosettings.md) — The video settings that the output uses.
