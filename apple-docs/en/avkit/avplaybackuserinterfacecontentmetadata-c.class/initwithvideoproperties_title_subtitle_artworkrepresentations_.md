---
title: 'initWithVideoProperties:title:subtitle:artworkRepresentations:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class/initwithvideoproperties:title:subtitle:artworkrepresentations:'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class/initwithvideoproperties:title:subtitle:artworkrepresentations:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class/initwithvideoproperties%3Atitle%3Asubtitle%3Aartworkrepresentations%3A.json'
content_hash: 'sha256:f44b03ff4ad603e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceContentMetadata](../avplaybackuserinterfacecontentmetadata-c.class.md)

# initWithVideoProperties:title:subtitle:artworkRepresentations:

<sub>Instance Method</sub>

Initializes a new metadata object with the specified properties.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
- (instancetype) initWithVideoProperties:(AVPlaybackUserInterfaceContentVideoProperties *) videoProperties title:(NSString *) title subtitle:(NSString *) subtitle artworkRepresentations:(NSArray<AVPlaybackUserInterfaceContentArtwork *> *) artworkRepresentations;
```

## Parameters

- `videoProperties` — Properties describing the video content, or `nil` for content without video.

- `title` — Primary title or name of the media content.

- `subtitle` — Secondary descriptive text such as artist name or episode description.

- `artworkRepresentations` — Array of available artwork representations in various formats and sizes.
