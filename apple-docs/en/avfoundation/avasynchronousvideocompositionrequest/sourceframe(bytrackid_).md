---
title: 'sourceFrame(byTrackID:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.9+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasynchronousvideocompositionrequest/sourceframe(bytrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourceframe(bytrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/sourceframe%28bytrackid%3A%29.json'
content_hash: 'sha256:07f97d502eedd5e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# sourceFrame(byTrackID:)

<sub>Instance Method</sub>

Returns a source pixel buffer for the track that contains the specified identifier.

> [!warning] Deprecated
> Use sourceReadOnlyPixelBuffer(byTrackID:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sourceFrame(byTrackID trackID: CMPersistentTrackID) -> CVPixelBuffer?
```

## Parameters

- `trackID` — The identifier of the track that contains the source frame.

## Return Value

A pixel buffer, or `nil` if not found.

## See Also

### Accessing source data

- [attach(_:to:)](<attach(__to_).md>) — Associates the pixel buffer with the specified spatial configuration.
- [sourceReadOnlyPixelBuffer(byTrackID:)](<sourcereadonlypixelbuffer(bytrackid_).md>) — Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.
- [sourceReadySampleBuffer(byTrackID:)](<sourcereadysamplebuffer(bytrackid_).md>) — Returns the source CMReadySampleBuffer for the given track ID.
- [- sourceSampleBufferByTrackID:](<sourcesamplebuffer(bytrackid_).md>) — Returns a source sample buffer for the track that contains the specified identifier. _(deprecated)_
- [sourceSampleDataTrackIDs](sourcesampledatatrackids-3yiab.md) — The identifiers of tracks that contain source sample data.
- [sourceTaggedDynamicBuffers(byTrackID:)](<sourcetaggeddynamicbuffers(bytrackid_).md>) — Returns the source tagged dynamic buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.
- [- sourceTimedMetadataByTrackID:](<sourcetimedmetadata(bytrackid_).md>) — Returns a source timed metadata group for the track that contains the specified identifier.
- [sourceTrackIDs](sourcetrackids.md) — The identifiers of tracks that contain source video.
