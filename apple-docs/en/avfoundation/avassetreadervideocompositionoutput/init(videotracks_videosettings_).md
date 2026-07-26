---
title: 'init(videoTracks:videoSettings:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreadervideocompositionoutput/init(videotracks:videosettings:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/init(videotracks:videosettings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadervideocompositionoutput/init%28videotracks%3Avideosettings%3A%29.json'
content_hash: 'sha256:fce446db8689e845'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderVideoCompositionOutput](../avassetreadervideocompositionoutput.md)

# init(videoTracks:videoSettings:)

<sub>Initializer</sub>

Creates an object that reads composited video frames from the specified video tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(videoTracks: [AVAssetTrack], videoSettings: [String : Any]?)
```

## Parameters

- `videoTracks` — An array of asset tracks from which to read video frames for compositing. The media type of each track must be [AVMediaTypeVideo](../avmediatype/video.md).

- `videoSettings` — Specifying a `nil` value configures the output to return samples in an uncompressed format.
