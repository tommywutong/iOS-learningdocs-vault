---
title: AVPlaybackUserInterfacePlaybackControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54.json'
content_hash: 'sha256:ce8acdea3cb324ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfacePlaybackControllable

<sub>Protocol</sub>

Provides playback control and state management for media content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol AVPlaybackUserInterfacePlaybackControllable : AnyObject, Observable
```

## Relationships

- **Inherits From**: [Observable](../observation/observable.md)

- **Inherited By**: [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)

## Topics

### Instance Properties

- [containsLiveStreamingContent](avplaybackuserinterfaceplaybackcontrollable-9he54/containslivestreamingcontent.md) — Indicates whether the content is a live stream. _(beta)_
- [error](avplaybackuserinterfaceplaybackcontrollable-9he54/error.md) — Error information when the source encounters a playback failure. _(beta)_
- [isBuffering](avplaybackuserinterfaceplaybackcontrollable-9he54/isbuffering.md) — Indicates whether the media source is currently stalled waiting for data. _(beta)_
- [isPlaying](avplaybackuserinterfaceplaybackcontrollable-9he54/isplaying.md) — Indicates whether playback is active. _(beta)_
- [isReady](avplaybackuserinterfaceplaybackcontrollable-9he54/isready.md) — Indicates whether the media source is ready to begin playback. _(beta)_
- [playbackSpeed](avplaybackuserinterfaceplaybackcontrollable-9he54/playbackspeed.md) — The user’s preferred playback speed multiplier. This value is preserved across scanning operations. _(beta)_
- [scanSpeed](avplaybackuserinterfaceplaybackcontrollable-9he54/scanspeed.md) — The speed multiplier used during scanning (fast-forward or rewind). This is a transient override active only while `state` is scanning. It does not affect `playbackSpeed`. When scanning ends, playback resumes at `playbackSpeed`. _(beta)_
- [state](avplaybackuserinterfaceplaybackcontrollable-9he54/state.md) — The current transport state of the playback source. _(beta)_
- [supportedSeekCapabilities](avplaybackuserinterfaceplaybackcontrollable-9he54/supportedseekcapabilities.md) — The supported timeline navigation operations. _(beta)_

## See Also

### Playback

- [AVPlaybackUserInterfacePlaybackState](avplaybackuserinterfaceplaybackstate.md) — Describes possible transport states of the playback source. _(beta)_
- [AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities.md) — Describes navigation capabilities of the media source. _(beta)_
