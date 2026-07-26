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
doc_path: /documentation/avfoundation/avvideocomposition/sourcesampledatatrackids-3nrgi
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/sourcesampledatatrackids-3nrgi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/sourcesampledatatrackids-3nrgi.json'
content_hash: 'sha256:ffe49bde54862e24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# sourceSampleDataTrackIDs

<sub>Instance Property</sub>

The identifiers of source sample data tracks in the composition that the compositor requires to compose frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * sourceSampleDataTrackIDs;
```

## See Also

### Identifying source tracks

- [sourceTrackIDForFrameTiming](sourcetrackidforframetiming.md) — An identifier of the source track from which the video composition derives frame timing.
