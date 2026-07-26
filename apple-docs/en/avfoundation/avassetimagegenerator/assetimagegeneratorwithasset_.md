---
title: 'assetImageGeneratorWithAsset:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetimagegenerator/assetimagegeneratorwithasset:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/assetimagegeneratorwithasset:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/assetimagegeneratorwithasset%3A.json'
content_hash: 'sha256:d1b2b7362f3298a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# assetImageGeneratorWithAsset:

<sub>Type Method</sub>

Returns a new object that generates images for times within a video asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetImageGeneratorWithAsset:(AVAsset *) asset;
```

## Parameters

- `asset` — A video asset from which to generate images.

## Return Value

A new image generator.

## See Also

### Creating an image generator

- [- initWithAsset:](<init(asset_).md>) — Creates an object that generates images for times within a video asset.
