---
title: 'artwork(url:contentType:size:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfacecontentartwork/artwork(url:contenttype:size:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentartwork/artwork(url:contenttype:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentartwork/artwork%28url%3Acontenttype%3Asize%3A%29.json'
content_hash: 'sha256:a6cc6338956d40ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceContentArtwork](../avplaybackuserinterfacecontentartwork.md)

# artwork(url:contentType:size:)

<sub>Type Method</sub>

Creates an artwork instance that references an image at the given URL.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func artwork(url: URL, contentType type: UTType, size: CGSize) -> AVPlaybackUserInterfaceContentURLArtwork
```

## Parameters

- `url` — URL pointing to the artwork image resource.

- `type` — The uniform type identifier for the image data.

- `size` — The pixel dimensions of the artwork image.
