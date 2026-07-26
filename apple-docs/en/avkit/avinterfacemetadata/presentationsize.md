---
title: presentationSize
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacemetadata/presentationsize
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemetadata/presentationsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemetadata/presentationsize.json'
content_hash: 'sha256:03a75449aead50ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceMetadata](../avinterfacemetadata.md)

# presentationSize

<sub>Instance Property</sub>

The natural pixel dimensions of the video content for display purposes. This represents the encoded size of the video stream and can be used to determine aspect ratio and optimal presentation layout. For audio-only content, this value is CGSizeZero.

<sub>tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly) CGSize presentationSize;
```

## See Also

### Inspecting the metadata

- [title](title.md) — Primary title or name of the media content for display in player UI and system interfaces. This should be the main identifying text for the content, such as a song title, episode name, or movie title.
- [subtitle](subtitle.md) — Secondary descriptive text such as artist name, episode description, or additional context for the content. This provides supplementary information to help users identify and understand the content being played.
- [audioOnly](audioonly.md) — Indicates whether the content is audio-only (no video component). Used to optimize UI layout and player controls for audio-focused presentations. When YES, video-related controls and layouts should be hidden or adapted for audio-only playback experiences.
- [albumArtworkRepresentations](albumartworkrepresentations.md) — Array of available album artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.
