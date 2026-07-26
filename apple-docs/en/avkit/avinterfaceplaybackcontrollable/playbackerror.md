---
title: playbackError
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfaceplaybackcontrollable/playbackerror
source_url: 'https://developer.apple.com/documentation/avkit/avinterfaceplaybackcontrollable/playbackerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfaceplaybackcontrollable/playbackerror.json'
content_hash: 'sha256:5995db0bab48ad36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfacePlaybackControllable](../avinterfaceplaybackcontrollable.md)

# playbackError

<sub>Instance Property</sub>

Error information when the source encounters a playback failure. Nil when playback is functioning normally. Must be key-value observable.

<sub>tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly, nullable) NSError * playbackError;
```

## See Also

### Inspecting playback state

- [playing](playing.md) — Indicates whether the media is currently playing. Setting this property starts or pauses playback. Must be key-value observable.
- [ready](ready.md) — Indicates whether the media source is ready for playback operations. Returns YES when the source has sufficient data and is prepared to begin playback. Use this property to determine when playback controls should be enabled and when the media can respond to play requests. Must be key-value observable.
- [buffering](buffering.md) — Indicates whether the media source is currently buffering content. Returns YES when the source is loading data and cannot immediately continue playback. Must be key-value observable.
- [state](state.md) — The current operational state of the interface source. Must be key-value observable.
- [containsLiveStreamingContent](containslivestreamingcontent.md) — Indicates whether the content contains live streaming content. Returns YES for live streams and NO for on-demand content. Must be key-value observable.
