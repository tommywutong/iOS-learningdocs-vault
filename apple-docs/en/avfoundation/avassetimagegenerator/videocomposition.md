---
title: videoComposition
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/videocomposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/videocomposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/videocomposition.json'
content_hash: 'sha256:80a004e3cca96a17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# videoComposition

<sub>Instance Property</sub>

A video composition to use when extracting images from assets with multiple video tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var videoComposition: AVVideoComposition? { get set }
```

## Discussion

If you don’t specify a video composition, the generator only uses the first enabled video track.

If specify a video composition, the image generator ignores the value of the [appliesPreferredTrackTransform](appliespreferredtracktransform.md) property.

Setting a video composition with any of the following attributes generates an exception:

- A [renderScale](../avvideocomposition/renderscale.md) not equal to `1.0`.
- A [renderSize](../avvideocomposition/rendersize.md) with a width or height less than `0`.
- A [frameDuration](../avvideocomposition/frameduration.md) that’s invalid, or less than or equal to [zero](../../coremedia/cmtime/zero.md).
- A [sourceTrackIDForFrameTiming](../avvideocomposition/sourcetrackidforframetiming.md) less than [zero](../../coremedia/cmtime/zero.md).

## See Also

### Configuring compositing

- [customVideoCompositor](customvideocompositor.md) — A custom video compositor to use when extracting images from assets with multiple video tracks.
