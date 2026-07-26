---
title: 'assetReaderVideoCompositionOutputWithVideoTracks:videoSettings:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreadervideocompositionoutput/assetreadervideocompositionoutputwithvideotracks:videosettings:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/assetreadervideocompositionoutputwithvideotracks:videosettings:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadervideocompositionoutput/assetreadervideocompositionoutputwithvideotracks%3Avideosettings%3A.json'
content_hash: 'sha256:ca4f136dcb5f0fb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderVideoCompositionOutput](../avassetreadervideocompositionoutput.md)

# assetReaderVideoCompositionOutputWithVideoTracks:videoSettings:

<sub>Type Method</sub>

Returns a new object that reads composited video from the specified video tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetReaderVideoCompositionOutputWithVideoTracks:(NSArray<AVAssetTrack *> *) videoTracks videoSettings:(NSDictionary<NSString *,id> *) videoSettings;
```

## Parameters

- `videoTracks` — An array of asset tracks from which the created object should read video frames for compositing. The media type of each track must be [AVMediaTypeVideo](../avmediatype/video.md).

- `videoSettings` — A dictionary of video settings to use for sample output, or `nil` if you want to receive decoded samples in a convenient uncompressed format, with properties determined according to the properties of the specified video tracks. You use keys from [CVPixelBuffer](../../corevideo/cvpixelbuffer.md), depending on the output format you want.

## Return Value

A new video composition output, or `nil` if initialization fails.

## See Also

### Creating a video composition output

- [- initWithVideoTracks:videoSettings:](<init(videotracks_videosettings_).md>) — Creates an object that reads composited video frames from the specified video tracks.
