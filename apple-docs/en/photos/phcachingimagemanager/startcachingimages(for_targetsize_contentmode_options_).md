---
title: 'startCachingImages(for:targetSize:contentMode:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcachingimagemanager/startcachingimages(for:targetsize:contentmode:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phcachingimagemanager/startcachingimages(for:targetsize:contentmode:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcachingimagemanager/startcachingimages%28for%3Atargetsize%3Acontentmode%3Aoptions%3A%29.json'
content_hash: 'sha256:049b497fa0ba8037'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCachingImageManager](../phcachingimagemanager.md)

# startCachingImages(for:targetSize:contentMode:options:)

<sub>Instance Method</sub>

Prepares image representations of the specified assets for later use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startCachingImages(for assets: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)
```

## Parameters

- `assets` — An array of [PHAsset](../phasset.md) objects for which to prepare image representations.

- `targetSize` — The size of the images to be prepared.

- `contentMode` — An option for how to fit the images to the aspect ratio of the requested size. For details, see [PHImageContentMode](../phimagecontentmode.md).

- `options` — Options specifying how Photos should handle the request, format the requested images, and notify your app of progress or errors. For details, see [PHImageRequestOptions](../phimagerequestoptions.md).

## Discussion

When you call this method, Photos begins to fetch image data and generates thumbnail images on a background thread. At any time afterward, you can use the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<../phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method to request individual images from the cache. If Photos has finished preparing a requested image, that method provides the image immediately.

Photos caches images with the exact target size, content mode, and options you specify in this method. If you later request an image with, for example, a different target size than you passed when calling this method, Photos cannot make use of the cache and so it must fetch or generate a new image.

## See Also

### Preparing Images

- [- stopCachingImagesForAssets:targetSize:contentMode:options:](<stopcachingimages(for_targetsize_contentmode_options_).md>) — Cancels image preparation for the specified assets and options.
- [- stopCachingImagesForAllAssets](<stopcachingimagesforallassets().md>) — Cancels all image preparation that is currently in progress.
