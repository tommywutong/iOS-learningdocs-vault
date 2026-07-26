---
title: 'init(items:defaultAlbumIdentifier:photoLibrary:)'
framework: PhotosUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photosui/phsharedalbumpostingviewcontroller/init(items:defaultalbumidentifier:photolibrary:)'
source_url: 'https://developer.apple.com/documentation/photosui/phsharedalbumpostingviewcontroller/init(items:defaultalbumidentifier:photolibrary:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phsharedalbumpostingviewcontroller/init%28items%3Adefaultalbumidentifier%3Aphotolibrary%3A%29.json'
content_hash: 'sha256:acece4b948547d33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHSharedAlbumPostingViewController](../phsharedalbumpostingviewcontroller.md)

# init(items:defaultAlbumIdentifier:photoLibrary:)

<sub>Initializer</sub>

Returns a view controller that allows the user to create a new shared album.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(items: [PHPickerResult], defaultAlbumIdentifier: String?, photoLibrary: PHPhotoLibrary)
```

## Parameters

- `items` — The items to be posted to the shared album.

- `defaultAlbumIdentifier` — Identifier for the shared album to be pre-selected. If none provided, the user can manually choose a shared album.

- `photoLibrary` — The photo library to choose from.
