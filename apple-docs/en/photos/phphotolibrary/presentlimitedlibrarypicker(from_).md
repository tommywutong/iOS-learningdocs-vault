---
title: 'presentLimitedLibraryPicker(from:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/presentlimitedlibrarypicker(from:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/presentlimitedlibrarypicker(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/presentlimitedlibrarypicker%28from%3A%29.json'
content_hash: 'sha256:b5e3b6ac4dc57404'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# presentLimitedLibraryPicker(from:)

<sub>Instance Method</sub>

Prompts the user to update their limited library selection.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func presentLimitedLibraryPicker(from controller: UIViewController)
```

## Parameters

- `controller` — The view controller from which to present the limited library picker.

## Discussion

If the user enabled limited library access using [+ requestAuthorizationForAccessLevel:handler:](<requestauthorization(for_handler_).md>), use this method to present the limited library picker so they can update their selection. If the user hasn’t enabled limited library access mode for your app, calling this method does nothing. Use this method when disabling the automatic limited library alert prompt. By default, the system automatically prompts the user to update their limited library selection once per app life cycle. To suppress the prompt, add `PHPhotoLibraryPreventAutomaticLimitedAccessAlert` to your app’s `Info.plist` file.

Any changes the user applies to the limited library selection trigger a [PHPhotoLibraryChangeObserver](../phphotolibrarychangeobserver.md) update.

## See Also

### Presenting the Limited Library Picker

- [- presentLimitedLibraryPickerFromViewController:completionHandler:](<presentlimitedlibrarypicker(from_completionhandler_).md>) — Prompts the user to update their limited library selection with a callback providing newly selected identifiers.
