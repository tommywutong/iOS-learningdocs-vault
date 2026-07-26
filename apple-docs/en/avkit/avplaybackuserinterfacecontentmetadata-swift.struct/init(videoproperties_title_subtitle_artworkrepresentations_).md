---
title: 'init(videoProperties:title:subtitle:artworkRepresentations:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/init(videoproperties:title:subtitle:artworkrepresentations:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/init(videoproperties:title:subtitle:artworkrepresentations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/init%28videoproperties%3Atitle%3Asubtitle%3Aartworkrepresentations%3A%29.json'
content_hash: 'sha256:e7c3e4a12ca10259'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceContentMetadata](../avplaybackuserinterfacecontentmetadata-swift.struct.md)

# init(videoProperties:title:subtitle:artworkRepresentations:)

<sub>Initializer</sub>

Creates a new metadata object.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(videoProperties: AVPlaybackUserInterfaceContentMetadata.VideoProperties? = nil, title: String? = nil, subtitle: String? = nil, artworkRepresentations: [AVPlaybackUserInterfaceContentArtwork] = [])
```

## Parameters

- `videoProperties` — Properties describing the video content, or `nil` for content without video.

- `title` — Primary title or name of the media content.

- `subtitle` — Secondary descriptive text.

- `artworkRepresentations` — Array of available artwork representations in various formats and sizes.
