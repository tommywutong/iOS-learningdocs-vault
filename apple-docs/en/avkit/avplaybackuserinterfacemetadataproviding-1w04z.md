---
title: AVPlaybackUserInterfaceMetadataProviding
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemetadataproviding-1w04z
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemetadataproviding-1w04z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemetadataproviding-1w04z.json'
content_hash: 'sha256:e5fa636f3c38164e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceMetadataProviding

<sub>Protocol</sub>

Provides metadata information about media content including title, artwork, and content type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@protocol AVPlaybackUserInterfaceMetadataProviding <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-7ti30.md)

## Topics

### Instance Properties

- [metadata](avplaybackuserinterfacemetadataproviding-1w04z/metadata.md) — The metadata object containing information about the media content. Must be key-value observable. _(beta)_

## See Also

### Metadata

- [AVPlaybackUserInterfaceContentMetadata](avplaybackuserinterfacecontentmetadata-c.class.md) — Provides metadata information about media content including title, artwork, and content type. _(beta)_
- [AVPlaybackUserInterfaceContentMetadataTemplate](avplaybackuserinterfacecontentmetadatatemplate.md) — A mutable template for configuring media metadata before creating immutable metadata objects. _(beta)_
- [AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md) — Base class representing artwork or cover art for media content. _(beta)_
- [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md) — An artwork subclass that references artwork via a URL and content type. _(beta)_
- [AVPlaybackUserInterfaceContentVideoProperties](avplaybackuserinterfacecontentvideoproperties.md) — Properties specific to video content. _(beta)_
