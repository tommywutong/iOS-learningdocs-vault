---
title: isSynchronous
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptions/issynchronous
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions/issynchronous'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions/issynchronous.json'
content_hash: 'sha256:ea87152a976b476a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptions](../phimagerequestoptions.md)

# isSynchronous

<sub>Instance Property</sub>

A Boolean value that determines whether Photos processes the image request synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isSynchronous: Bool { get set }
```

## Discussion

If `false` (the default), the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<../phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method returns immediately. Depending on the [deliveryMode](deliverymode.md) property, Photos may call your `resultHandler` block before the method returns, at some later time, or both.

If `true`, the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<../phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method blocks the calling thread until image data is ready or an error occurs. Photos calls your result handler block exactly once.

> [!note] Note
> Perform synchronous requests from a background thread only.
