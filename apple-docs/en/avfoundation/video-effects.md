---
title: Video effects
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/video-effects
source_url: 'https://developer.apple.com/documentation/avfoundation/video-effects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/video-effects.json'
content_hash: 'sha256:71be0d410e8281f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# Video effects

<sub>API Collection</sub>

Define standard video transition effects, synchronize layer animations with media timing, and create custom video compositors.

## Topics

### Core Animation integration

- [AVVideoCompositionCoreAnimationTool](avvideocompositioncoreanimationtool.md) — An object used to incorporate Core Animation into a video composition.

### Built-in video compositing

- [Editing and playing HDR video](editing-and-playing-hdr-video.md) — Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md) — Resolve common problems when creating compositions, video compositions, and audio mixes.
- [AVVideoComposition](avvideocomposition.md) — An object that describes how to compose video frames at particular points in time.
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md) — An operation that a compositor performs.
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [AVMutableVideoComposition](avmutablevideocomposition.md) — A mutable video composition subclass. _(deprecated)_
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md) — A mutable video composition instruction subclass. _(deprecated)_
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition. _(deprecated)_

### Custom video compositing

- [Processing spatial video with a custom video compositor](processing-spatial-video-with-a-custom-video-compositor.md) — Create a custom video compositor to edit spatial video for playback and export.
- [AVVideoCompositing](avvideocompositing.md) — A protocol that defines the methods custom video compositors must implement.

## See Also

### Editing

- [Composite assets](composite-assets.md) — Combine tracks and segments of tracks from multiple assets into a composite asset that you can play or process.
- [QuickTime movies](quicktime-movies.md) — Access the contents of a QuickTime movie file, and perform sample-level edits of its media tracks.
- [Audio mixing](audio-mixing.md) — Define how to mix the audio levels from multiple audio tracks over an asset’s duration.
