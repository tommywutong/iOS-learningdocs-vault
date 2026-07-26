---
title: AVPlaybackUserInterfaceContentMetadata
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class.json'
content_hash: 'sha256:ca226f874d36c1fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceContentMetadata

<sub>Class</sub>

Provides metadata information about media content including title, artwork, and content type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@interface AVPlaybackUserInterfaceContentMetadata : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Instance Properties

- [artworkRepresentations](avplaybackuserinterfacecontentmetadata-c.class/artworkrepresentations.md) — Array of available artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance. _(beta)_
- [subtitle](avplaybackuserinterfacecontentmetadata-c.class/subtitle.md) — Secondary descriptive text such as artist name, episode description, or additional context for the content. This provides supplementary information to help users identify and understand the content being played. _(beta)_
- [title](avplaybackuserinterfacecontentmetadata-c.class/title.md) — Primary title or name of the media content for display in player UI and system interfaces. This should be the main identifying text for the content, such as a song title, episode name, or movie title. _(beta)_
- [videoProperties](avplaybackuserinterfacecontentmetadata-c.class/videoproperties.md) — Properties describing the video content. `nil` if the content contains no video. _(beta)_

### Instance Methods

- [initWithTemplate:](avplaybackuserinterfacecontentmetadata-c.class/initwithtemplate_.md) — Initializes a new metadata object by copying values from a metadata template. _(beta)_
- [initWithVideoProperties:title:subtitle:artworkRepresentations:](avplaybackuserinterfacecontentmetadata-c.class/initwithvideoproperties_title_subtitle_artworkrepresentations_.md) — Initializes a new metadata object with the specified properties. _(beta)_

## See Also

### Metadata

- [AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-1w04z.md) — Provides metadata information about media content including title, artwork, and content type. _(beta)_
- [AVPlaybackUserInterfaceContentMetadataTemplate](avplaybackuserinterfacecontentmetadatatemplate.md) — A mutable template for configuring media metadata before creating immutable metadata objects. _(beta)_
- [AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md) — Base class representing artwork or cover art for media content. _(beta)_
- [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md) — An artwork subclass that references artwork via a URL and content type. _(beta)_
- [AVPlaybackUserInterfaceContentVideoProperties](avplaybackuserinterfacecontentvideoproperties.md) — Properties specific to video content. _(beta)_
