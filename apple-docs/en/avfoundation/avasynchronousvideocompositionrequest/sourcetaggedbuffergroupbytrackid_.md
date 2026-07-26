---
title: 'sourceTaggedBufferGroupByTrackID:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcetaggedbuffergroupbytrackid:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcetaggedbuffergroupbytrackid:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcetaggedbuffergroupbytrackid%3A.json'
content_hash: 'sha256:1b511473ef449f77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# sourceTaggedBufferGroupByTrackID:

<sub>Instance Method</sub>

Returns the source CMTaggedBufferGroupRef for the given track ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (CMTaggedBufferGroupRef) sourceTaggedBufferGroupByTrackID:(CMPersistentTrackID) trackID;
```

## Parameters

- `trackID` — The track ID for the requested source tagged buffer group.

## Discussion

Returns nil if the video track does not contain tagged buffers. Returns nil if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.

## See Also

### Accessing source data

- [attachSpatialVideoConfiguration:toPixelBuffer:](attachspatialvideoconfiguration_topixelbuffer_.md) — Associates the pixel buffer with the specified spatial configuration.
- [- sourceFrameByTrackID:](<sourceframe(bytrackid_).md>) — Returns a source pixel buffer for the track that contains the specified identifier. _(deprecated)_
- [- sourceSampleBufferByTrackID:](<sourcesamplebuffer(bytrackid_).md>) — Returns a source sample buffer for the track that contains the specified identifier. _(deprecated)_
- [sourceSampleDataTrackIDs](sourcesampledatatrackids-9vxz5.md) — The identifiers of tracks that contain source metadata.
- [- sourceTimedMetadataByTrackID:](<sourcetimedmetadata(bytrackid_).md>) — Returns a source timed metadata group for the track that contains the specified identifier.
- [sourceTrackIDs](sourcetrackids.md) — The identifiers of tracks that contain source video.
