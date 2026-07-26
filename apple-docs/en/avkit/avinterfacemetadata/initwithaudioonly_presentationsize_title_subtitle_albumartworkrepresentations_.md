---
title: 'initWithAudioOnly:presentationSize:title:subtitle:albumArtworkRepresentations:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinterfacemetadata/initwithaudioonly:presentationsize:title:subtitle:albumartworkrepresentations:'
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemetadata/initwithaudioonly:presentationsize:title:subtitle:albumartworkrepresentations:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemetadata/initwithaudioonly%3Apresentationsize%3Atitle%3Asubtitle%3Aalbumartworkrepresentations%3A.json'
content_hash: 'sha256:671f2892a7338d9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceMetadata](../avinterfacemetadata.md)

# initWithAudioOnly:presentationSize:title:subtitle:albumArtworkRepresentations:

<sub>Instance Method</sub>

Initializes a new metadata object with the specified properties.

<sub>tvOS, visionOS</sub>

```objc
- (instancetype) initWithAudioOnly:(BOOL) audioOnly presentationSize:(CGSize) presentationSize title:(NSString *) title subtitle:(NSString *) subtitle albumArtworkRepresentations:(NSArray<AVInterfaceAlbumArtwork *> *) albumArtworkRepresentations;
```

## Parameters

- `audioOnly` — Whether the content is audio-only (no video component).

- `presentationSize` — The pixel dimensions for video presentation.

- `title` — Primary title or name of the media content.

- `subtitle` — Secondary descriptive text such as artist name or episode description.

- `albumArtworkRepresentations` — Array of available album artwork representations in various formats and sizes.

## See Also

### Creating metadata

- [initWithTemplate:](initwithtemplate_.md) — Initializes a new metadata object by copying values from a metadata template.
