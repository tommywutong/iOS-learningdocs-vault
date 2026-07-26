---
title: sourceSampleDataTrackIDs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasynchronousvideocompositionrequest/sourcesampledatatrackids-9vxz5
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcesampledatatrackids-9vxz5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcesampledatatrackids-9vxz5.json'
content_hash: 'sha256:26b6b7a1a1ae182a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# sourceSampleDataTrackIDs

<sub>Instance Property</sub>

The identifiers of tracks that contain source metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * sourceSampleDataTrackIDs;
```

## Discussion

The track identifiers are of type [kCMMediaType_Metadata](../../coremedia/kcmmediatype_metadata.md).

## See Also

### Accessing source data

- [attachSpatialVideoConfiguration:toPixelBuffer:](attachspatialvideoconfiguration_topixelbuffer_.md) — Associates the pixel buffer with the specified spatial configuration.
- [- sourceFrameByTrackID:](<sourceframe(bytrackid_).md>) — Returns a source pixel buffer for the track that contains the specified identifier. _(deprecated)_
- [- sourceSampleBufferByTrackID:](<sourcesamplebuffer(bytrackid_).md>) — Returns a source sample buffer for the track that contains the specified identifier. _(deprecated)_
- [sourceTaggedBufferGroupByTrackID:](sourcetaggedbuffergroupbytrackid_.md) — Returns the source CMTaggedBufferGroupRef for the given track ID.
- [- sourceTimedMetadataByTrackID:](<sourcetimedmetadata(bytrackid_).md>) — Returns a source timed metadata group for the track that contains the specified identifier.
- [sourceTrackIDs](sourcetrackids.md) — The identifiers of tracks that contain source video.
