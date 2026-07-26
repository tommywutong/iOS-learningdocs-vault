---
title: AVPlaybackUserInterfaceMediaSelectionControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z.json'
content_hash: 'sha256:c061641a53f9ba87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceMediaSelectionControllable

<sub>Protocol</sub>

Provides audio and subtitle selection capabilities for media content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol AVPlaybackUserInterfaceMediaSelectionControllable : AnyObject, Observable
```

## Relationships

- **Inherits From**: [Observable](../observation/observable.md)

- **Inherited By**: [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)

## Topics

### Instance Properties

- [audioDescriptionOptions](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiodescriptionoptions.md) — Array of available audio description track options. _(beta)_
- [audioOptions](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiooptions.md) — Array of available audio track options. _(beta)_
- [currentAudioDescriptionOption](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentaudiodescriptionoption.md) — The currently selected audio description track. _(beta)_
- [currentAudioOption](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentaudiooption.md) — The currently selected audio track. _(beta)_
- [currentLegibleOption](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentlegibleoption.md) — The currently selected subtitle or caption track. _(beta)_
- [legibleOptions](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/legibleoptions.md) — Array of available subtitle and caption track options. _(beta)_

## See Also

### Media selection

- [AVPlaybackUserInterfaceMediaSelectionOption](avplaybackuserinterfacemediaselectionoption.md) — Represents a media selection option for audio tracks or subtitle tracks. _(beta)_
