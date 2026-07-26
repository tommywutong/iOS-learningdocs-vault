---
title: 'moveAsset(withIdentifier:afterAssetWithIdentifier:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phpickerviewcontroller/moveasset(withidentifier:afterassetwithidentifier:)'
source_url: 'https://developer.apple.com/documentation/photosui/phpickerviewcontroller/moveasset(withidentifier:afterassetwithidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerviewcontroller/moveasset%28withidentifier%3Aafterassetwithidentifier%3A%29.json'
content_hash: 'sha256:aa84ff2784ade991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerViewController](../phpickerviewcontroller.md)

# moveAsset(withIdentifier:afterAssetWithIdentifier:)

<sub>Instance Method</sub>

Reorders assets that are in a selected state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func moveAsset(withIdentifier identifier: String, afterAssetWithIdentifier afterIdentifier: String?)
```

## Parameters

- `identifier` — The identifier that represents the asset to move.

- `afterIdentifier` — The identifier to move the asset to.

## Discussion

This method ignores assets that are invalid or aren’t in a selected state, and if you don’t specify a library when calling [init(photoLibrary:)](<../phpickerconfiguration-swift.struct/init(photolibrary_).md>).

If `afterIdentifier` is `nil`, the identifier you specify moves to the beginning of the picker.
