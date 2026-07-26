---
title: 'requestPlayerItem(forVideo:options:resultHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phimagemanager/requestplayeritem(forvideo:options:resulthandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phimagemanager/requestplayeritem(forvideo:options:resulthandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagemanager/requestplayeritem%28forvideo%3Aoptions%3Aresulthandler%3A%29.json'
content_hash: 'sha256:254aaa6577448fdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageManager](../phimagemanager.md)

# requestPlayerItem(forVideo:options:resultHandler:)

<sub>Instance Method</sub>

Requests a representation of the video asset for playback, to be loaded asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func requestPlayerItem(forVideo asset: PHAsset, options: PHVideoRequestOptions?, resultHandler: @escaping (AVPlayerItem?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

## Parameters

- `asset` — The video asset to be played back.

- `options` — Options specifying how Photos should handle the request and notify your app of progress or errors. For details, see [PHVideoRequestOptions](../phvideorequestoptions.md).

- `resultHandler` — A block Photos calls after loading the asset’s data and preparing the player item. The block takes the following parameters: - **playerItem** — An [AVPlayerItem](../../avfoundation/avplayeritem.md) object that you can use for playing back the video asset. - **info** — A dictionary providing information about the status of the request. See [Image Result Info Keys](../../photokit/image-result-info-keys.md) for possible keys and values.

## Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [- cancelImageRequest:](<cancelimagerequest(__).md>) method.

## Discussion

When you call this method, Photos downloads the video data (if necessary) and creates a player item. It then calls your `resultHandler` block to provide the requested video.

Use this method when you want to simply play back the video asset as it currently exists. For more detailed options or to work with the asset’s audio and video tracks, use the [- requestAVAssetForVideo:options:resultHandler:](<requestavasset(forvideo_options_resulthandler_).md>) method instead.

## See Also

### Requesting Video Objects

- [- requestExportSessionForVideo:options:exportPreset:resultHandler:](<requestexportsession(forvideo_options_exportpreset_resulthandler_).md>) — Requests an export session for writing the video asset’s data to a file, to be loaded asynchronously.
- [- requestAVAssetForVideo:options:resultHandler:](<requestavasset(forvideo_options_resulthandler_).md>) — Requests AVFoundation objects representing the video asset’s content and state, to be loaded asynchronously.
