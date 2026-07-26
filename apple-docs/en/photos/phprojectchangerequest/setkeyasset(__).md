---
title: 'setKeyAsset(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.13+（10.14 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phprojectchangerequest/setkeyasset(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phprojectchangerequest/setkeyasset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phprojectchangerequest/setkeyasset%28_%3A%29.json'
content_hash: 'sha256:9a160859b3c3d3e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHProjectChangeRequest](../phprojectchangerequest.md)

# setKeyAsset(_:)

<sub>Instance Method</sub>

Sets the key asset representing the project.

<sub>macOS</sub>

```swift
func setKeyAsset(_ keyAsset: PHAsset?)
```

## Discussion

> [!note] Note
> Setting a key asset has been deprecated in macOS 10.14. Use [- setProjectPreviewImage:](<setprojectpreviewimage(__).md>) to provide a rendered preview image instead of designating a key asset.

## See Also

### Responding to Change Requests

- [- setProjectPreviewImage:](<setprojectpreviewimage(__).md>) — Updates the project preview in Photos.
