---
title: 'initWithURL:contentType:size:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinterfacealbumartwork/initwithurl:contenttype:size:'
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacealbumartwork/initwithurl:contenttype:size:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacealbumartwork/initwithurl%3Acontenttype%3Asize%3A.json'
content_hash: 'sha256:9ef30a3d69415ca3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceAlbumArtwork](../avinterfacealbumartwork.md)

# initWithURL:contentType:size:

<sub>Instance Method</sub>

Initializes a new album artwork object with the specified image resource information.

<sub>tvOS, visionOS</sub>

```objc
- (instancetype) initWithURL:(NSURL *) url contentType:(UTType *) contentType size:(CGSize) size;
```

## Parameters

- `url` — URL pointing to the album artwork image resource.

- `contentType` — The uniform type identifier for the artwork image data.

- `size` — The pixel dimensions of the artwork image.
