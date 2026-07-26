---
title: 'init(track:outputSettings:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreadertrackoutput/init(track:outputsettings:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/init(track:outputsettings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadertrackoutput/init%28track%3Aoutputsettings%3A%29.json'
content_hash: 'sha256:afa106ba45ffc9ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderTrackOutput](../avassetreadertrackoutput.md)

# init(track:outputSettings:)

<sub>Initializer</sub>

Creates an object that reads media data from an asset track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(track: AVAssetTrack, outputSettings: [String : Any]?)
```

## Parameters

- `track` — The track from which to read media samples.

- `outputSettings` — A dictionary of settings to use for sample output. Specify `nil` to receive samples in their storage format. You use keys and values from [Audio settings](../audio-settings.md), [Video settings](../video-settings.md), or [CVPixelBuffer](../../corevideo/cvpixelbuffer.md), depending on the media type and the output format you require.

## See Also

### Creating a track output

- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
