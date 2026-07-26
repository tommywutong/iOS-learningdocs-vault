---
title: 'init(albumIdentifier:photoLibrary:)'
framework: PhotosUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photosui/phsharedalbumcustomizationviewcontroller/init(albumidentifier:photolibrary:)'
source_url: 'https://developer.apple.com/documentation/photosui/phsharedalbumcustomizationviewcontroller/init(albumidentifier:photolibrary:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phsharedalbumcustomizationviewcontroller/init%28albumidentifier%3Aphotolibrary%3A%29.json'
content_hash: 'sha256:ad47dc79884c061a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHSharedAlbumCustomizationViewController](../phsharedalbumcustomizationviewcontroller.md)

# init(albumIdentifier:photoLibrary:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(albumIdentifier: String, photoLibrary: PHPhotoLibrary)
```

## Parameters

- `albumIdentifier` — The identifier of the shared album to be customized.

- `photoLibrary` — The photo library in which the specified shared album exists.

## Discussion

Returns a view controller that allows the user to customize a specified shared album.

Only the system photo library is supported, so `albumIdentifier` must be for an album in the system photo library. If `albumIdentifier` is from a different library, showing a customization sheet will fail.
