---
title: AVPlaybackUserInterfaceMediaSelectionControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn.json'
content_hash: 'sha256:f7b92a7cbad424b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceMediaSelectionControllable

<sub>Protocol</sub>

Provides audio and subtitle selection capabilities for media content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@protocol AVPlaybackUserInterfaceMediaSelectionControllable <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-7ti30.md)

## Topics

### Instance Properties

- [audioDescriptionOptions](avplaybackuserinterfacemediaselectioncontrollable-2fftn/audiodescriptionoptions.md) — Array of available audio description track options. Audio description tracks provide narrated descriptions of visual content for visually impaired viewers. Audio description options are distinct from those in `audioOptions` — they provide a narration layer played alongside the primary audio rather than replacing it. Options are ordered by preference with the primary language or default audio description track typically appearing first. May be empty for content without audio description tracks. Must be key-value observable. _(beta)_
- [audioOptions](avplaybackuserinterfacemediaselectioncontrollable-2fftn/audiooptions.md) — Array of available audio track options. This includes all audio streams provided by the media source such as different languages, director’s commentary, and alternative audio mixes. Options are ordered by preference with the primary language or default audio track typically appearing first. May be empty for content without selectable audio options. Must be key-value observable. _(beta)_
- [currentAudioDescriptionOption](avplaybackuserinterfacemediaselectioncontrollable-2fftn/currentaudiodescriptionoption.md) — The currently selected audio description track. Should be one of the options in `audioDescriptionOptions`. Must be key-value observable. _(beta)_
- [currentAudioOption](avplaybackuserinterfacemediaselectioncontrollable-2fftn/currentaudiooption.md) — The currently selected audio track. Should be one of the options in `audioOptions`. Must be key-value observable. _(beta)_
- [currentLegibleOption](avplaybackuserinterfacemediaselectioncontrollable-2fftn/currentlegibleoption.md) — The currently selected subtitle or caption track. Should be one of the options in `legibleOptions`. Must be key-value observable. _(beta)_
- [legibleOptions](avplaybackuserinterfacemediaselectioncontrollable-2fftn/legibleoptions.md) — Array of available subtitle and caption track options. This includes text overlays in different languages, closed captions for accessibility, forced narrative subtitles, and sign language interpretation tracks. May be empty for content without text tracks. Must be key-value observable. _(beta)_

## See Also

### Media selection

- [AVPlaybackUserInterfaceMediaSelectionOption](avplaybackuserinterfacemediaselectionoption.md) — Represents a media selection option for audio tracks or subtitle tracks. _(beta)_
