---
title: AVPlaybackUserInterfaceContentMetadataTemplate
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacecontentmetadatatemplate
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadatatemplate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentmetadatatemplate.json'
content_hash: 'sha256:cbc18d5681280fcf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceContentMetadataTemplate

<sub>Class</sub>

A mutable template for configuring media metadata before creating immutable metadata objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@interface AVPlaybackUserInterfaceContentMetadataTemplate : NSObject
```

## Overview

Use this class to build and configure metadata for media content with full control over all properties. Once configured, create an immutable `AVPlaybackUserInterfaceContentMetadata` object using `initWithTemplate:` to provide stable metadata for playback interfaces.

This template provides a convenient way to incrementally build metadata information, allowing you to set properties individually before finalizing the metadata. All properties are mutable (readwrite), making it ideal for scenarios where metadata is constructed from multiple sources or updated over time.

Example usage:

AVPlaybackUserInterfaceContentMetadataTemplate *template = [[AVPlaybackUserInterfaceContentMetadataTemplate alloc] init]; template.videoProperties = [[AVPlaybackUserInterfaceContentVideoProperties alloc] initWithPresentationSize:CGSizeMake(1920, 1080)]; template.title = @“Episode 5: The Journey Continues”; template.subtitle = @“Season 2”; template.artworkRepresentations = @[artwork1, artwork2];

AVPlaybackUserInterfaceContentMetadata *metadata = [[AVPlaybackUserInterfaceContentMetadata alloc] initWithTemplate:template];

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Instance Properties

- [artworkRepresentations](avplaybackuserinterfacecontentmetadatatemplate/artworkrepresentations.md) — Array of available artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance. _(beta)_
- [subtitle](avplaybackuserinterfacecontentmetadatatemplate/subtitle.md) — Secondary descriptive text such as artist name, episode description, or additional context for the content. This provides supplementary information to help users identify and understand the content being played. _(beta)_
- [title](avplaybackuserinterfacecontentmetadatatemplate/title.md) — Primary title or name of the media content for display in player UI and system interfaces. This should be the main identifying text for the content, such as a song title, episode name, or movie title. _(beta)_
- [videoProperties](avplaybackuserinterfacecontentmetadatatemplate/videoproperties.md) — Properties describing the video content. `nil` if the content contains no video. _(beta)_

## See Also

### Metadata

- [AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-1w04z.md) — Provides metadata information about media content including title, artwork, and content type. _(beta)_
- [AVPlaybackUserInterfaceContentMetadata](avplaybackuserinterfacecontentmetadata-c.class.md) — Provides metadata information about media content including title, artwork, and content type. _(beta)_
- [AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md) — Base class representing artwork or cover art for media content. _(beta)_
- [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md) — An artwork subclass that references artwork via a URL and content type. _(beta)_
- [AVPlaybackUserInterfaceContentVideoProperties](avplaybackuserinterfacecontentvideoproperties.md) — Properties specific to video content. _(beta)_
