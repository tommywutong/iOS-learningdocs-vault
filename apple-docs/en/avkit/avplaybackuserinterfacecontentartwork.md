---
title: AVPlaybackUserInterfaceContentArtwork
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacecontentartwork
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentartwork'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentartwork.json'
content_hash: 'sha256:a31cda32c8501bee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceContentArtwork

<sub>Class</sub>

Base class representing artwork or cover art for media content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class AVPlaybackUserInterfaceContentArtwork
```

## Overview

Use a concrete subclass such as [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md) to create artwork instances.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(coder:)](<avplaybackuserinterfacecontentartwork/init(coder_).md>) _(beta)_

### Instance Properties

- [size](avplaybackuserinterfacecontentartwork/size.md) — The pixel dimensions of the artwork image. _(beta)_

### Type Methods

- [+ artworkWithURL:contentType:size:](<avplaybackuserinterfacecontentartwork/artwork(url_contenttype_size_).md>) — Creates an artwork instance that references an image at the given URL. _(beta)_

## See Also

### Metadata

- [AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-814y4.md) — Provides metadata information about media content including title, artwork, and content type. _(beta)_
- [AVPlaybackUserInterfaceContentMetadata](avplaybackuserinterfacecontentmetadata-swift.struct.md) — A Swift-friendly structure representing media metadata. _(beta)_
- [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md) — An artwork subclass that references artwork via a URL and content type. _(beta)_
