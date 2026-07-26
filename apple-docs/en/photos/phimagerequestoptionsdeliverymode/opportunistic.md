---
title: PHImageRequestOptionsDeliveryMode.opportunistic
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsdeliverymode/opportunistic
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsdeliverymode/opportunistic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsdeliverymode/opportunistic.json'
content_hash: 'sha256:4e6317c9754afd6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md)

# PHImageRequestOptionsDeliveryMode.opportunistic

<sub>Case</sub>

Photos automatically provides one or more results in order to balance image quality and responsiveness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case opportunistic
```

## Discussion

If the [synchronous](../phimagerequestoptions/issynchronous.md) property is `false`, Photos may call the `resultHandler` block (that you specified in the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<../phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method more than once. Photos may call your result handler once to provide a low-quality image suitable for displaying temporarily while it prepares a high-quality image. If low-quality image data is immediately available, this first call may occur before the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<../phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method returns. When the high-quality image is ready, Photos calls your result handler again to provide it.

If the image manager has already cached the requested image, or if the [synchronous](../phimagerequestoptions/issynchronous.md) property is `true`, Photos calls your result handler only once.

## See Also

### Constants

- [PHImageRequestOptionsDeliveryModeHighQualityFormat](highqualityformat.md) — Photos provides only the highest-quality image available, regardless of how much time it takes to load.
- [PHImageRequestOptionsDeliveryModeFastFormat](fastformat.md) — Photos provides only a fast-loading image, possibly sacrificing image quality.
