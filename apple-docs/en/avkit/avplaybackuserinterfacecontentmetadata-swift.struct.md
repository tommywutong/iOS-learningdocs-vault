---
title: AVPlaybackUserInterfaceContentMetadata
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct.json'
content_hash: 'sha256:751cbb797c4aa0ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceContentMetadata

<sub>Structure</sub>

A Swift-friendly structure representing media metadata.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct AVPlaybackUserInterfaceContentMetadata
```

## Overview

This structure provides metadata information about media content including title, artwork, and content type. Use this to provide rich information for playback interfaces and system integrations.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Structures

- [VideoProperties](avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct.md) — Properties specific to video content. _(beta)_

### Initializers

- [init(videoProperties:title:subtitle:artworkRepresentations:)](<avplaybackuserinterfacecontentmetadata-swift.struct/init(videoproperties_title_subtitle_artworkrepresentations_).md>) — Creates a new metadata object. _(beta)_

### Instance Properties

- [artworkRepresentations](avplaybackuserinterfacecontentmetadata-swift.struct/artworkrepresentations.md) — Array of available artwork representations in various formats and sizes. _(beta)_
- [subtitle](avplaybackuserinterfacecontentmetadata-swift.struct/subtitle.md) — Secondary descriptive text such as artist name or episode description. _(beta)_
- [title](avplaybackuserinterfacecontentmetadata-swift.struct/title.md) — Primary title or name of the media content. _(beta)_
- [videoProperties](avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.property.md) — Properties describing the video content. `nil` if the content contains no video. _(beta)_

## See Also

### Metadata

- [AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-814y4.md) — Provides metadata information about media content including title, artwork, and content type. _(beta)_
- [AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md) — Base class representing artwork or cover art for media content. _(beta)_
- [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md) — An artwork subclass that references artwork via a URL and content type. _(beta)_
