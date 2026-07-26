---
title: 'sourceTimedMetadata(byTrackID:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcetimedmetadata(bytrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcetimedmetadata(bytrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcetimedmetadata%28bytrackid%3A%29.json'
content_hash: 'sha256:318f7623d4093634'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# sourceTimedMetadata(byTrackID:)

<sub>Instance Method</sub>

Returns a source timed metadata group for the track that contains the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sourceTimedMetadata(byTrackID trackID: CMPersistentTrackID) -> AVTimedMetadataGroup?
```

## Parameters

- `trackID` — The identifier of the track that contains the timed metadata.

## Return Value

A timed metadata group, or `nil` if not found.

## See Also

### Accessing source data

- [attach(_:to:)](<attach(__to_).md>) — Associates the pixel buffer with the specified spatial configuration.
- [- sourceFrameByTrackID:](<sourceframe(bytrackid_).md>) — Returns a source pixel buffer for the track that contains the specified identifier. _(deprecated)_
- [sourceReadOnlyPixelBuffer(byTrackID:)](<sourcereadonlypixelbuffer(bytrackid_).md>) — Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.
- [sourceReadySampleBuffer(byTrackID:)](<sourcereadysamplebuffer(bytrackid_).md>) — Returns the source CMReadySampleBuffer for the given track ID.
- [- sourceSampleBufferByTrackID:](<sourcesamplebuffer(bytrackid_).md>) — Returns a source sample buffer for the track that contains the specified identifier. _(deprecated)_
- [sourceSampleDataTrackIDs](sourcesampledatatrackids-3yiab.md) — The identifiers of tracks that contain source sample data.
- [sourceTaggedDynamicBuffers(byTrackID:)](<sourcetaggeddynamicbuffers(bytrackid_).md>) — Returns the source tagged dynamic buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.
- [sourceTrackIDs](sourcetrackids.md) — The identifiers of tracks that contain source video.
