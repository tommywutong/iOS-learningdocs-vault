---
title: AVPlaybackUserInterfaceContentVideoProperties
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacecontentvideoproperties
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentvideoproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentvideoproperties.json'
content_hash: 'sha256:184c014471d5bf3a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceContentVideoProperties

<sub>Class</sub>

Properties specific to video content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@interface AVPlaybackUserInterfaceContentVideoProperties : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Instance Properties

- [presentationSize](avplaybackuserinterfacecontentvideoproperties/presentationsize.md) — The natural pixel dimensions of the video content for layout and aspect ratio calculations. _(beta)_

### Instance Methods

- [initWithPresentationSize:](avplaybackuserinterfacecontentvideoproperties/initwithpresentationsize_.md) — Initializes a new video properties instance. _(beta)_

## See Also

### Metadata

- [AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-1w04z.md) — Provides metadata information about media content including title, artwork, and content type. _(beta)_
- [AVPlaybackUserInterfaceContentMetadata](avplaybackuserinterfacecontentmetadata-c.class.md) — Provides metadata information about media content including title, artwork, and content type. _(beta)_
- [AVPlaybackUserInterfaceContentMetadataTemplate](avplaybackuserinterfacecontentmetadatatemplate.md) — A mutable template for configuring media metadata before creating immutable metadata objects. _(beta)_
- [AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md) — Base class representing artwork or cover art for media content. _(beta)_
- [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md) — An artwork subclass that references artwork via a URL and content type. _(beta)_
