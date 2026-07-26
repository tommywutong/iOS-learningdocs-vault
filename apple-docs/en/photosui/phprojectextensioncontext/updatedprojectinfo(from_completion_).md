---
title: 'updatedProjectInfo(from:completion:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojectextensioncontext/updatedprojectinfo(from:completion:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojectextensioncontext/updatedprojectinfo(from:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectextensioncontext/updatedprojectinfo%28from%3Acompletion%3A%29.json'
content_hash: 'sha256:f3d7b0bd931f2434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectExtensionContext](../phprojectextensioncontext.md)

# updatedProjectInfo(from:completion:)

<sub>Instance Method</sub>

Creates an updated [PHProjectInfo](../phprojectinfo.md) instance from existing project information and current assets.

<sub>macOS</sub>

```swift
func updatedProjectInfo(from existingProjectInfo: PHProjectInfo?, completion: @escaping (PHProjectInfo?) -> Void) -> Progress
```

## Parameters

- `existingProjectInfo` — The project information to update. If this is not `nil`, a new [PHProjectInfo](../phprojectinfo.md) instance is created from all assets in the [PHProject](../../photos/phproject.md).

- `completion` — A closure with code you provide that runs on completion.

## See Also

### Updating Assets

- [- showEditorForAsset:](<showeditor(for_).md>) — Invokes the built-in photo editor for the given asset.
