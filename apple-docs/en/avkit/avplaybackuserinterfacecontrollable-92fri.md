---
title: AVPlaybackUserInterfaceControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacecontrollable-92fri
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontrollable-92fri'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontrollable-92fri.json'
content_hash: 'sha256:d484dcd902196a05'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceControllable

<sub>Protocol</sub>

A comprehensive protocol that provides complete media control and information for playback, timeline navigation, audio/subtitle selection, volume control, and metadata access.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol AVPlaybackUserInterfaceControllable : AVPlaybackUserInterfaceMediaSelectionControllable, AVPlaybackUserInterfaceMetadataProviding, AVPlaybackUserInterfacePlaybackControllable, AVPlaybackUserInterfaceTimeControllable, AVPlaybackUserInterfaceVolumeControllable
```

## Overview

This protocol consolidates all media source capabilities into a single interface, enabling rich media experiences with full control over playback state, timeline interactions, and content metadata.

## Relationships

- **Inherits From**: [AVPlaybackUserInterfaceMediaSelectionControllable](avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md), [AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-814y4.md), [AVPlaybackUserInterfacePlaybackControllable](avplaybackuserinterfaceplaybackcontrollable-9he54.md), [AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-50vcy.md), [AVPlaybackUserInterfaceVolumeControllable](avplaybackuserinterfacevolumecontrollable-4vgi1.md), [Observable](../observation/observable.md)
