---
title: 'requestAVAsset(forVideo:options:resultHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phimagemanager/requestavasset(forvideo:options:resulthandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phimagemanager/requestavasset(forvideo:options:resulthandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagemanager/requestavasset%28forvideo%3Aoptions%3Aresulthandler%3A%29.json'
content_hash: 'sha256:088d827305b87140'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageManager](../phimagemanager.md)

# requestAVAsset(forVideo:options:resultHandler:)

<sub>Instance Method</sub>

Requests AVFoundation objects representing the video asset’s content and state, to be loaded asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func requestAVAsset(forVideo asset: PHAsset, options: PHVideoRequestOptions?, resultHandler: @escaping (AVAsset?, AVAudioMix?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

## Parameters

- `asset` — The video asset for which video objects are to be loaded.

- `options` — Options specifying how Photos should handle the request and notify your app of progress or errors. For details, see [PHVideoRequestOptions](../phvideorequestoptions.md).

- `resultHandler` — A block that Photos calls after loading the asset’s data. The block takes the following parameters: - **asset** — An object that provides access to the video asset as a collection of tracks and metadata. For details on working with [AVAsset](../../avfoundation/avasset.md) objects, see [AVFoundation Programming Guide](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40010188). - **audioMix** — Use this object to rearrange the asset’s audio tracks, edit additional audio into the mix, or configure an [AVAssetReaderOutput](../../avfoundation/avassetreaderoutput.md) object for exporting the asset’s audio data. If `nil`, the asset uses a default audio mix. - **info** — A dictionary providing information about the status of the request. See [Image Result Info Keys](../../photokit/image-result-info-keys.md) for possible keys and values.

## Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [- cancelImageRequest:](<cancelimagerequest(__).md>) method.

## Discussion

When you call this method, Photos downloads the video data (if necessary) and creates AVFoundation objects. It then calls your `resultHandler` block to provide the requested video.

Use this method when you want to work with the arrangement of audio and video tracks that an asset contains. If you plan to use the asset only for playback, call the [- requestPlayerItemForVideo:options:resultHandler:](<requestplayeritem(forvideo_options_resulthandler_).md>) method. If you plan to export the asset data, call the [- requestExportSessionForVideo:options:exportPreset:resultHandler:](<requestexportsession(forvideo_options_exportpreset_resulthandler_).md>) method.

## See Also

### Requesting Video Objects

- [- requestPlayerItemForVideo:options:resultHandler:](<requestplayeritem(forvideo_options_resulthandler_).md>) — Requests a representation of the video asset for playback, to be loaded asynchronously.
- [- requestExportSessionForVideo:options:exportPreset:resultHandler:](<requestexportsession(forvideo_options_exportpreset_resulthandler_).md>) — Requests an export session for writing the video asset’s data to a file, to be loaded asynchronously.
