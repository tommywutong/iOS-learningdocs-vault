---
title: AVInterfaceAlbumArtwork
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacealbumartwork
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacealbumartwork'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacealbumartwork.json'
content_hash: 'sha256:f6eedb06f45e5184'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVInterfaceAlbumArtwork

<sub>Class</sub>

Base class representing album artwork or cover art for media content.

<sub>tvOS, visionOS</sub>

```objc
@interface AVInterfaceAlbumArtwork : NSObject
```

## Overview

Use a concrete subclass such as @c AVInterfaceURLAlbumArtwork to create artwork instances.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVInterfaceURLAlbumArtwork](avinterfaceurlalbumartwork.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating album artwork

- [initWithURL:contentType:size:](avinterfacealbumartwork/initwithurl_contenttype_size_.md) — Initializes a new album artwork object with the specified image resource information.

### Inspecting the artwork

- [url](avinterfacealbumartwork/url.md) — URL pointing to the album artwork image resource.
- [contentType](avinterfacealbumartwork/contenttype.md) — The uniform type identifier for the artwork image data.
- [size](avinterfacealbumartwork/size.md) — The pixel dimensions of the artwork image.

### Type Methods

- [artworkWithURL:contentType:size:](avinterfacealbumartwork/artworkwithurl_contenttype_size_.md) — Creates an artwork instance that references an image at the given URL.
