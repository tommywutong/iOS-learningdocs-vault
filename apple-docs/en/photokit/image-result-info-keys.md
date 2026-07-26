---
title: Image Result Info Keys
framework: Photos
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/image-result-info-keys
source_url: 'https://developer.apple.com/documentation/photokit/image-result-info-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/image-result-info-keys.json'
content_hash: 'sha256:1902133603372576'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md) · [Photos](../photos.md) · [PHImageManager](../photos/phimagemanager.md)

# Image Result Info Keys

<sub>API Collection</sub>

Keys identifying information about an image loading result, used in the `resultHandler` block with image request methods.

## Topics

### Constants

- [PHImageResultIsInCloudKey](../photos/phimageresultisincloudkey.md) — A key whose value indicates whether photo asset data is stored on the local device or must be downloaded from iCloud.
- [PHImageResultIsDegradedKey](../photos/phimageresultisdegradedkey.md) — A key whose value indicates whether the result image is a low-quality substitute for the requested image.
- [PHImageResultRequestIDKey](../photos/phimageresultrequestidkey.md) — A key whose value is a unique identifier for the image request.
- [PHImageCancelledKey](../photos/phimagecancelledkey.md) — A key whose value indicates whether the image request was canceled.
- [PHImageErrorKey](../photos/phimageerrorkey.md) — A key whose value is an error that occurred when Photos attempted to load the image.

## See Also

### Constants

- [PHImageContentMode](../photos/phimagecontentmode.md) — Options for fitting an image’s aspect ratio to a requested size, used by the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<../photos/phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method.
