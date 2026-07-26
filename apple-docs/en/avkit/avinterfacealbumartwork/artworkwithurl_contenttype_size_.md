---
title: 'artworkWithURL:contentType:size:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinterfacealbumartwork/artworkwithurl:contenttype:size:'
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacealbumartwork/artworkwithurl:contenttype:size:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacealbumartwork/artworkwithurl%3Acontenttype%3Asize%3A.json'
content_hash: 'sha256:3cd5b84b9a71665d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceAlbumArtwork](../avinterfacealbumartwork.md)

# artworkWithURL:contentType:size:

<sub>Type Method</sub>

Creates an artwork instance that references an image at the given URL.

<sub>tvOS, visionOS</sub>

```objc
+ (AVInterfaceURLAlbumArtwork *) artworkWithURL:(NSURL *) url contentType:(UTType *) type size:(CGSize) size;
```

## Parameters

- `url` — URL pointing to the artwork image resource.

- `type` — The uniform type identifier for the image data.

- `size` — The pixel dimensions of the artwork image.
