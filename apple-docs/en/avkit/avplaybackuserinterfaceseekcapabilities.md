---
title: AVPlaybackUserInterfaceSeekCapabilities
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceseekcapabilities
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceseekcapabilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceseekcapabilities.json'
content_hash: 'sha256:948461ce320eed28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceSeekCapabilities

<sub>Structure</sub>

Describes navigation capabilities of the media source.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct AVPlaybackUserInterfaceSeekCapabilities
```

## Overview

This option set defines timeline navigation operations. Different content types and sources may have varying levels of navigation support based on technical limitations, licensing restrictions, or content type.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<avplaybackuserinterfaceseekcapabilities/init(rawvalue_).md>) _(beta)_

### Type Properties

- [AVPlaybackUserInterfaceSeekCapabilitiesScanBackward](avplaybackuserinterfaceseekcapabilities/scanbackward.md) — The source supports backward scanning at accelerated rates for rewind operations. Enables rapid reverse progression through content at speeds greater than normal playback. _(beta)_
- [AVPlaybackUserInterfaceSeekCapabilitiesScanForward](avplaybackuserinterfaceseekcapabilities/scanforward.md) — The source supports forward scanning at accelerated rates for fast-forward operations. Enables rapid progression through content at speeds greater than normal playback. _(beta)_
- [AVPlaybackUserInterfaceSeekCapabilitiesSeek](avplaybackuserinterfaceseekcapabilities/seek.md) — The source supports seeking to specific time positions for precise navigation. Enables jumping directly to any arbitrary point within the seekable time ranges. _(beta)_

## See Also

### Playback

- [AVPlaybackUserInterfacePlaybackControllable](avplaybackuserinterfaceplaybackcontrollable-9he54.md) — Provides playback control and state management for media content. _(beta)_
- [AVPlaybackUserInterfacePlaybackState](avplaybackuserinterfaceplaybackstate.md) — Describes possible transport states of the playback source. _(beta)_
