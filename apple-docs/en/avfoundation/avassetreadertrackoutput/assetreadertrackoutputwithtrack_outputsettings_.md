---
title: 'assetReaderTrackOutputWithTrack:outputSettings:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreadertrackoutput/assetreadertrackoutputwithtrack:outputsettings:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/assetreadertrackoutputwithtrack:outputsettings:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadertrackoutput/assetreadertrackoutputwithtrack%3Aoutputsettings%3A.json'
content_hash: 'sha256:5fa77e5209c09bda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderTrackOutput](../avassetreadertrackoutput.md)

# assetReaderTrackOutputWithTrack:outputSettings:

<sub>Type Method</sub>

Returns a new object that reads media data from an asset track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetReaderTrackOutputWithTrack:(AVAssetTrack *) track outputSettings:(NSDictionary<NSString *,id> *) outputSettings;
```

## Parameters

- `track` — The track from which to read media samples.

- `outputSettings` — A dictionary of settings to use for sample output. Specify `nil` to receive samples in their storage format. You use keys and values from [Audio settings](../audio-settings.md), [Video settings](../video-settings.md), or [CVPixelBuffer](../../corevideo/cvpixelbuffer.md), depending on the media type and the output format you require.

## Return Value

A new asset reader, or `nil` if initialization fails.

## See Also

### Creating a track output

- [- initWithTrack:outputSettings:](<init(track_outputsettings_).md>) — Creates an object that reads media data from an asset track.
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
