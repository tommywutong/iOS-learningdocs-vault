---
title: 'stopCachingImages(for:targetSize:contentMode:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcachingimagemanager/stopcachingimages(for:targetsize:contentmode:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phcachingimagemanager/stopcachingimages(for:targetsize:contentmode:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcachingimagemanager/stopcachingimages%28for%3Atargetsize%3Acontentmode%3Aoptions%3A%29.json'
content_hash: 'sha256:2ca51b3552dc48c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCachingImageManager](../phcachingimagemanager.md)

# stopCachingImages(for:targetSize:contentMode:options:)

<sub>Instance Method</sub>

Cancels image preparation for the specified assets and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func stopCachingImages(for assets: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)
```

## Parameters

- `assets` — The array of specific [PHAsset](../phasset.md) objects for which image preparation is in progress but is no longer needed.

- `targetSize` — The target size with which you requested image preparation.

- `contentMode` — The content mode with which you requested image preparation.

- `options` — The options with which you requested image preparation.

## Discussion

This method cancels image preparation for the specified assets with the specified options. Use it when image preparation that might be in progress is no longer needed. For example, if you prepare images for a collection view filled with photo thumbnails and then the user chooses a different thumbnail size for your collection view, call this method to cancel generating thumbnail images at the old size.

## See Also

### Preparing Images

- [- startCachingImagesForAssets:targetSize:contentMode:options:](<startcachingimages(for_targetsize_contentmode_options_).md>) — Prepares image representations of the specified assets for later use.
- [- stopCachingImagesForAllAssets](<stopcachingimagesforallassets().md>) — Cancels all image preparation that is currently in progress.
