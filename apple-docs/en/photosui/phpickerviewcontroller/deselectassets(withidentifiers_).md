---
title: 'deselectAssets(withIdentifiers:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phpickerviewcontroller/deselectassets(withidentifiers:)'
source_url: 'https://developer.apple.com/documentation/photosui/phpickerviewcontroller/deselectassets(withidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerviewcontroller/deselectassets%28withidentifiers%3A%29.json'
content_hash: 'sha256:612900aa893d1011'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerViewController](../phpickerviewcontroller.md)

# deselectAssets(withIdentifiers:)

<sub>Instance Method</sub>

Deselects assets that are in a selected state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func deselectAssets(withIdentifiers identifiers: [String])
```

## Parameters

- `identifiers` — The list of identifiers to deselect.

## Discussion

This method ignores assets that are invalid or aren’t in a selected state, and if you don’t specify a library when calling [init(photoLibrary:)](<../phpickerconfiguration-swift.struct/init(photolibrary_).md>).
