---
title: audioDescriptionOptions
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn/audiodescriptionoptions
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn/audiodescriptionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn/audiodescriptionoptions.json'
content_hash: 'sha256:208abfce6b364948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionControllable](../avplaybackuserinterfacemediaselectioncontrollable-2fftn.md)

# audioDescriptionOptions

<sub>Instance Property</sub>

Array of available audio description track options. Audio description tracks provide narrated descriptions of visual content for visually impaired viewers. Audio description options are distinct from those in `audioOptions` — they provide a narration layer played alongside the primary audio rather than replacing it. Options are ordered by preference with the primary language or default audio description track typically appearing first. May be empty for content without audio description tracks. Must be key-value observable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, copy, readonly) NSArray<AVPlaybackUserInterfaceMediaSelectionOption *> * audioDescriptionOptions;
```
