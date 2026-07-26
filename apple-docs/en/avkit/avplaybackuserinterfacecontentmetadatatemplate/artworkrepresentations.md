---
title: artworkRepresentations
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacecontentmetadatatemplate/artworkrepresentations
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadatatemplate/artworkrepresentations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentmetadatatemplate/artworkrepresentations.json'
content_hash: 'sha256:decf5d12e5cfd158'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceContentMetadataTemplate](../avplaybackuserinterfacecontentmetadatatemplate.md)

# artworkRepresentations

<sub>Instance Property</sub>

Array of available artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, copy, readwrite) NSArray<AVPlaybackUserInterfaceContentArtwork *> * artworkRepresentations;
```
