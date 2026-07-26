---
title: AVInterfaceMediaSelectionControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacemediaselectioncontrollable
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemediaselectioncontrollable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemediaselectioncontrollable.json'
content_hash: 'sha256:6d654436f0a99b5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVInterfaceMediaSelectionControllable

<sub>Protocol</sub>

Provides audio and subtitle selection capabilities for media content.

<sub>tvOS, visionOS</sub>

```objc
@protocol AVInterfaceMediaSelectionControllable <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [AVInterfaceControllable](avinterfacecontrollable.md)

## Topics

### Inspecting media selection options

- [audioOptions](avinterfacemediaselectioncontrollable/audiooptions.md) — Array of available audio track options for selection. This includes all audio streams provided by the media source such as different languages, audio descriptions, director’s commentary, and alternative audio mixes. Options are ordered by preference with the primary language or default audio track typically appearing first. May be empty for content without selectable audio options. Must be key-value observable.
- [currentAudioOption](avinterfacemediaselectioncontrollable/currentaudiooption.md) — Currently selected audio track for playback. Setting this property changes the active audio stream. This includes language variants, audio descriptions, director’s commentary, and other audio content. Must be key-value observable.
- [legibleOptions](avinterfacemediaselectioncontrollable/legibleoptions.md) — Array of available subtitle and caption track options for selection. This includes text overlays in different languages, closed captions for accessibility, forced narrative subtitles, and sign language interpretation tracks. May be empty for content without text tracks. Must be key-value observable.
- [currentLegibleOption](avinterfacemediaselectioncontrollable/currentlegibleoption.md) — Currently selected subtitle or caption track. Setting this property controls text overlay presentation. This includes subtitles in different languages, closed captions, and forced narrative text. Set to nil to disable text display. Must be key-value observable.
