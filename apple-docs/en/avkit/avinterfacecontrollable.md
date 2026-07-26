---
title: AVInterfaceControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacecontrollable
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacecontrollable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacecontrollable.json'
content_hash: 'sha256:ec5c0fa0a79847b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVInterfaceControllable

<sub>Protocol</sub>

A comprehensive protocol that provides complete media control and information for playback, timeline navigation, audio/subtitle selection, volume control, and metadata access.

<sub>tvOS, visionOS</sub>

```objc
@protocol AVInterfaceControllable <AVInterfaceTimeControllable, AVInterfacePlaybackControllable, AVInterfaceMediaSelectionControllable, AVInterfaceVolumeControllable, AVInterfaceMetadataProviding>
```

## Overview

This protocol consolidates all media source capabilities into a single interface, enabling rich media experiences with full control over playback state, timeline interactions, and content metadata. Implementations should provide key-value observable properties where specified to ensure proper integration with media player controls and UI frameworks.

## Relationships

- **Inherits From**: [AVInterfaceMediaSelectionControllable](avinterfacemediaselectioncontrollable.md), [AVInterfaceMetadataProviding](avinterfacemetadataproviding.md), [AVInterfacePlaybackControllable](avinterfaceplaybackcontrollable.md), [AVInterfaceTimeControllable](avinterfacetimecontrollable.md), [AVInterfaceVolumeControllable](avinterfacevolumecontrollable.md)
