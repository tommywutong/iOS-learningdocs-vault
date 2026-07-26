---
title: AVInterfaceMetadataTemplate
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacemetadatatemplate
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemetadatatemplate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemetadatatemplate.json'
content_hash: 'sha256:abfe49048d23ff47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVInterfaceMetadataTemplate

<sub>Class</sub>

A mutable template for configuring media metadata before creating immutable metadata objects.

<sub>tvOS, visionOS</sub>

```objc
@interface AVInterfaceMetadataTemplate : NSObject
```

## Overview

Use this class to build and configure metadata for media content with full control over all properties. Once configured, create an immutable `AVInterfaceMetadata` object using `initWithTemplate:` to provide stable metadata for playback interfaces.

This template provides a convenient way to incrementally build metadata information, allowing you to set properties individually before finalizing the metadata. All properties are mutable (readwrite), making it ideal for scenarios where metadata is constructed from multiple sources or updated over time.

Example usage:

AVInterfaceMetadataTemplate *template = [[AVInterfaceMetadataTemplate alloc] init]; template.audioOnly = NO; template.title = @“Episode 5: The Journey Continues”; template.subtitle = @“Season 2”; template.albumArtworkRepresentations = @[artwork1, artwork2];

AVInterfaceMetadata *metadata = [[AVInterfaceMetadata alloc] initWithTemplate:template];

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Inspecting the template

- [title](avinterfacemetadatatemplate/title.md) — Primary title or name of the media content for display in player UI and system interfaces. This should be the main identifying text for the content, such as a song title, episode name, or movie title.
- [subtitle](avinterfacemetadatatemplate/subtitle.md) — Secondary descriptive text such as artist name, episode description, or additional context for the content. This provides supplementary information to help users identify and understand the content being played.
- [audioOnly](avinterfacemetadatatemplate/audioonly.md) — Indicates whether the content is audio-only (no video component). Used to optimize UI layout and player controls for audio-focused presentations. When YES, video-related controls and layouts should be hidden or adapted for audio-only playback experiences.
- [presentationSize](avinterfacemetadatatemplate/presentationsize.md) — The natural pixel dimensions of the video content for display purposes. This represents the encoded size of the video stream and can be used to determine aspect ratio and optimal presentation layout. For audio-only content, this value is CGSizeZero.
- [albumArtworkRepresentations](avinterfacemetadatatemplate/albumartworkrepresentations.md) — Array of available album artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.
