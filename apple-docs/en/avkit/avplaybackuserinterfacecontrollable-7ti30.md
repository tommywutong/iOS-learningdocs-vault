---
title: AVPlaybackUserInterfaceControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacecontrollable-7ti30
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontrollable-7ti30'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontrollable-7ti30.json'
content_hash: 'sha256:5940c06ab8af173f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceControllable

<sub>Protocol</sub>

A comprehensive protocol that provides complete media control and information for playback, timeline navigation, audio/subtitle selection, volume control, and metadata access.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@protocol AVPlaybackUserInterfaceControllable <AVPlaybackUserInterfaceTimeControllable, AVPlaybackUserInterfacePlaybackControllable, AVPlaybackUserInterfaceMediaSelectionControllable, AVPlaybackUserInterfaceVolumeControllable, AVPlaybackUserInterfaceMetadataProviding>
```

## Overview

This protocol consolidates all media source capabilities into a single interface, enabling rich media experiences with full control over playback state, timeline interactions, and content metadata. Implementations should provide key-value observable properties where specified to ensure proper integration with media player controls and UI frameworks.

## Relationships

- **Inherits From**: [AVPlaybackUserInterfaceMediaSelectionControllable](avplaybackuserinterfacemediaselectioncontrollable-2fftn.md), [AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-1w04z.md), [AVPlaybackUserInterfacePlaybackControllable](avplaybackuserinterfaceplaybackcontrollable-81n66.md), [AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-62fq2.md), [AVPlaybackUserInterfaceVolumeControllable](avplaybackuserinterfacevolumecontrollable-5ystg.md)
