---
title: allowsCachingHighQualityImages
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（26.0 起废弃）, iPadOS 8.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.15+（26.0 起废弃）, tvOS 10.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phcachingimagemanager/allowscachinghighqualityimages
source_url: 'https://developer.apple.com/documentation/photos/phcachingimagemanager/allowscachinghighqualityimages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcachingimagemanager/allowscachinghighqualityimages.json'
content_hash: 'sha256:e80a9b1ea1e174f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCachingImageManager](../phcachingimagemanager.md)

# allowsCachingHighQualityImages

<sub>Instance Property</sub>

A Boolean value that determines whether the image manager prepares high-quality images.

> [!warning] Deprecated
> This property is unused and will be removed in a future release

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allowsCachingHighQualityImages: Bool { get set }
```

## Discussion

If `true` (the default), the image manager prepares images at high quality. This option produces better images, at a high performance cost.

For faster performance when preparing large numbers of images—such as while the user is scrolling quickly through a collection of thumbnails—set this property to `false`.
