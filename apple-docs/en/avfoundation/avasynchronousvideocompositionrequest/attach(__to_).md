---
title: 'attach(_:to:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasynchronousvideocompositionrequest/attach(_:to:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/attach(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/attach%28_%3Ato%3A%29.json'
content_hash: 'sha256:62cd0bbc6001a151'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# attach(_:to:)

<sub>Instance Method</sub>

Associates the pixel buffer with the specified spatial configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func attach(_ spatialVideoConfiguration: AVSpatialVideoConfiguration, to pixelBuffer: inout CVMutablePixelBuffer) throws
```

## Parameters

- `spatialVideoConfiguration` — The spatial configuration to associate with the pixel buffer.

- `pixelBuffer` — The pixel buffer to associate with the spatial configuration. NOTE: The spatial configuration must be one of the spatial configurations specified in the AVVideoComposition’s spatialConfigurations property. An exception will be thrown otherwise. NOTE: All pixel buffers from the custom compositor must be associated with the same spatial configuration. An exception will be thrown otherwise. Specify a value of .nonSpatial for spatialVideoConfiguration to indicate the video is not spatial, but note that a .nonSpatial configuration must be in the `AVVideoComposition/spatialConfigurations` property or an exception will be thrown.

## See Also

### Accessing source data

- [- sourceFrameByTrackID:](<sourceframe(bytrackid_).md>) — Returns a source pixel buffer for the track that contains the specified identifier. _(deprecated)_
- [sourceReadOnlyPixelBuffer(byTrackID:)](<sourcereadonlypixelbuffer(bytrackid_).md>) — Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.
- [sourceReadySampleBuffer(byTrackID:)](<sourcereadysamplebuffer(bytrackid_).md>) — Returns the source CMReadySampleBuffer for the given track ID.
- [- sourceSampleBufferByTrackID:](<sourcesamplebuffer(bytrackid_).md>) — Returns a source sample buffer for the track that contains the specified identifier. _(deprecated)_
- [sourceSampleDataTrackIDs](sourcesampledatatrackids-3yiab.md) — The identifiers of tracks that contain source sample data.
- [sourceTaggedDynamicBuffers(byTrackID:)](<sourcetaggeddynamicbuffers(bytrackid_).md>) — Returns the source tagged dynamic buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.
- [- sourceTimedMetadataByTrackID:](<sourcetimedmetadata(bytrackid_).md>) — Returns a source timed metadata group for the track that contains the specified identifier.
- [sourceTrackIDs](sourcetrackids.md) — The identifiers of tracks that contain source video.
