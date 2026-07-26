---
title: 'setProjectPreviewImage(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phprojectchangerequest/setprojectpreviewimage(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phprojectchangerequest/setprojectpreviewimage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phprojectchangerequest/setprojectpreviewimage%28_%3A%29.json'
content_hash: 'sha256:565ff69088c750cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHProjectChangeRequest](../phprojectchangerequest.md)

# setProjectPreviewImage(_:)

<sub>Instance Method</sub>

Updates the project preview in Photos.

<sub>macOS</sub>

```swift
func setProjectPreviewImage(_ previewImage: NSImage)
```

## Parameters

- `previewImage` — A rendered project preview with dimensions of 1024 x 1024.

## Discussion

PhotoKit requires that you set a project preview in the following situations:

- Whenever the project changes in a way that requires a new preview.
- During or after execution of the [- beginProjectWithExtensionContext:projectInfo:completion:](<../../photosui/phprojectextensioncontroller/beginproject(with_projectinfo_completion_).md>) protocol method.
- During or after execution of the [- resumeProjectWithExtensionContext:completion:](<../../photosui/phprojectextensioncontroller/resumeproject(with_completion_).md>) protocol method.

## See Also

### Responding to Change Requests

- [- setKeyAsset:](<setkeyasset(__).md>) — Sets the key asset representing the project. _(deprecated)_
