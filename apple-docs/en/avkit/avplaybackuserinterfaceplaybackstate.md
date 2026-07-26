---
title: AVPlaybackUserInterfacePlaybackState
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackstate
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackstate.json'
content_hash: 'sha256:119ab309bd93578c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfacePlaybackState

<sub>Enumeration</sub>

Describes possible transport states of the playback source.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum AVPlaybackUserInterfacePlaybackState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [AVPlaybackUserInterfacePlaybackStateNormal](avplaybackuserinterfaceplaybackstate/normal.md) — Indicates the source is in a normal state. _(beta)_
- [AVPlaybackUserInterfacePlaybackStateScanning](avplaybackuserinterfaceplaybackstate/scanning.md) — Indicates the source is scanning forward or backward at an accelerated rate. _(beta)_
- [AVPlaybackUserInterfacePlaybackStateScrubbing](avplaybackuserinterfaceplaybackstate/scrubbing.md) — Indicates the source is being scrubbed by user interaction with the timeline. _(beta)_

### Initializers

- [init(rawValue:)](<avplaybackuserinterfaceplaybackstate/init(rawvalue_).md>) _(beta)_

## See Also

### Playback

- [AVPlaybackUserInterfacePlaybackControllable](avplaybackuserinterfaceplaybackcontrollable-9he54.md) — Provides playback control and state management for media content. _(beta)_
- [AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities.md) — Describes navigation capabilities of the media source. _(beta)_
