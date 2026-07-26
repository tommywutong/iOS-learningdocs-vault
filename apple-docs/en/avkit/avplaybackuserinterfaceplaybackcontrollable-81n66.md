---
title: AVPlaybackUserInterfacePlaybackControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66.json'
content_hash: 'sha256:f8f15bd7e97ae3fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfacePlaybackControllable

<sub>Protocol</sub>

Provides playback control and state management for media content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@protocol AVPlaybackUserInterfacePlaybackControllable <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-7ti30.md)

## Topics

### Instance Properties

- [buffering](avplaybackuserinterfaceplaybackcontrollable-81n66/buffering.md) — Indicates whether the media source is currently stalled waiting for data. Returns YES when the source cannot immediately sustain continuous playback. This may occur both before `isReady` becomes YES during initial loading, and after `isReady` is YES during mid-playback stalls. When YES, `isPlaying` may still be YES, indicating that playback should resume automatically once sufficient data is available. Must be key-value observable. _(beta)_
- [containsLiveStreamingContent](avplaybackuserinterfaceplaybackcontrollable-81n66/containslivestreamingcontent.md) — Indicates whether the content is a live stream. Returns YES for live streams and NO for on-demand content. Must be key-value observable. _(beta)_
- [defaultPlaybackSpeed](avplaybackuserinterfaceplaybackcontrollable-81n66/defaultplaybackspeed.md) — The default playback speed to use when playback begins. This value is used to set the initial playback rate when starting playback. A value of 1.0 represents normal speed. Must be key-value observable.
- [error](avplaybackuserinterfaceplaybackcontrollable-81n66/error.md) — Error information when the source encounters a playback failure. Nil when playback is functioning normally. Must be key-value observable. _(beta)_
- [playbackSpeed](avplaybackuserinterfaceplaybackcontrollable-81n66/playbackspeed.md) — The user’s preferred playback speed multiplier. This value is preserved across scanning operations. Must be key-value observable. _(beta)_
- [playing](avplaybackuserinterfaceplaybackcontrollable-81n66/playing.md) — Indicates whether playback is active. Setting this property to YES starts playback; setting it to NO pauses it. This property reflects playback intent — it should remain YES while `isBuffering` is YES, indicating that playback should resume automatically once sufficient data is available. Must be key-value observable. _(beta)_
- [ready](avplaybackuserinterfaceplaybackcontrollable-81n66/ready.md) — Indicates whether the media source is ready to begin playback. This property should transition from NO to YES once the source has loaded enough data to start playback, and should not revert. Use `isBuffering` to track temporary stalls that may occur after this point. Must be key-value observable. _(beta)_
- [scanSpeed](avplaybackuserinterfaceplaybackcontrollable-81n66/scanspeed.md) — The speed multiplier used during scanning (fast-forward or rewind). This is a transient override that is active only while `state` is scanning. It does not affect `playbackSpeed`. When scanning ends, playback resumes at `playbackSpeed`. Must be key-value observable. _(beta)_
- [state](avplaybackuserinterfaceplaybackcontrollable-81n66/state.md) — The current transport state of the playback source. Must be key-value observable. _(beta)_
- [supportedSeekCapabilities](avplaybackuserinterfaceplaybackcontrollable-81n66/supportedseekcapabilities.md) — An option set indicating which timeline navigation operations are supported by this media source. This property defines the available navigation capabilities, including precise seeking to specific time positions and accelerated scanning for fast-forward/rewind operations. The supported modes may vary based on content type, licensing restrictions, or technical limitations of the underlying media format. Must be key-value observable. _(beta)_

## See Also

### Playback

- [AVPlaybackUserInterfacePlaybackState](avplaybackuserinterfaceplaybackstate.md) — Describes possible transport states of the playback source. _(beta)_
- [AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities.md) — Describes navigation capabilities of the media source. _(beta)_
