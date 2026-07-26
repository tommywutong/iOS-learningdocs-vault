---
title: AVPlaybackUserInterfaceMetadataProviding
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemetadataproviding-814y4
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemetadataproviding-814y4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemetadataproviding-814y4.json'
content_hash: 'sha256:59e4856284e5f1a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceMetadataProviding

<sub>Protocol</sub>

Provides metadata information about media content including title, artwork, and content type.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol AVPlaybackUserInterfaceMetadataProviding : AnyObject, Observable
```

## Relationships

- **Inherits From**: [Observable](../observation/observable.md)

- **Inherited By**: [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)

## Topics

### Instance Properties

- [metadata](avplaybackuserinterfacemetadataproviding-814y4/metadata.md) — The metadata object containing information about the media content. _(beta)_

## See Also

### Metadata

- [AVPlaybackUserInterfaceContentMetadata](avplaybackuserinterfacecontentmetadata-swift.struct.md) — A Swift-friendly structure representing media metadata. _(beta)_
- [AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md) — Base class representing artwork or cover art for media content. _(beta)_
- [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md) — An artwork subclass that references artwork via a URL and content type. _(beta)_
