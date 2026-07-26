---
title: 'showEditor(for:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojectextensioncontext/showeditor(for:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojectextensioncontext/showeditor(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectextensioncontext/showeditor%28for%3A%29.json'
content_hash: 'sha256:c788a6b735b6fcb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectExtensionContext](../phprojectextensioncontext.md)

# showEditor(for:)

<sub>Instance Method</sub>

Invokes the built-in photo editor for the given asset.

<sub>macOS</sub>

```swift
func showEditor(for asset: PHAsset)
```

## Parameters

- `asset` — The asset to edit.

## Discussion

To be notified when assets are edited, the extension should observe library changes by implementing the [PHPhotoLibraryChangeObserver](../../photos/phphotolibrarychangeobserver.md) protocol.

## See Also

### Updating Assets

- [- updatedProjectInfoFromProjectInfo:completion:](<updatedprojectinfo(from_completion_).md>) — Creates an updated [PHProjectInfo](../phprojectinfo.md) instance from existing project information and current assets.
