---
title: 'presentLimitedLibraryPicker(from:completionHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/presentlimitedlibrarypicker(from:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/presentlimitedlibrarypicker(from:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/presentlimitedlibrarypicker%28from%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:df98af806275c02f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# presentLimitedLibraryPicker(from:completionHandler:)

<sub>Instance Method</sub>

Prompts the user to update their limited library selection with a callback providing newly selected identifiers.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func presentLimitedLibraryPicker(from controller: UIViewController, completionHandler: @escaping @Sendable ([String]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func presentLimitedLibraryPicker(from controller: UIViewController) async -> [String]
```

## Parameters

- `controller` — The view controller from which to present the limited library picker.

- `completionHandler` — A closure the system invokes when the user finishes their selection. The closure provides only the newly selected asset identifiers.

## Discussion

If the user enabled limited library access using [+ requestAuthorizationForAccessLevel:handler:](<requestauthorization(for_handler_).md>), use this method to present the limited library picker so they can update their selection. If the user hasn’t enabled limited library access mode for your app, calling this method does nothing. Use this method when disabling the automatic limited library alert prompt. By default, the system automatically prompts the user to update their limited library selection once per app life cycle. To suppress the prompt, add `PHPhotoLibraryPreventAutomaticLimitedAccessAlert` to your app’s `Info.plist` file.

Any changes the user applies to the limited library selection trigger a [PHPhotoLibraryChangeObserver](../phphotolibrarychangeobserver.md) update.

## See Also

### Presenting the Limited Library Picker

- [- presentLimitedLibraryPickerFromViewController:](<presentlimitedlibrarypicker(from_).md>) — Prompts the user to update their limited library selection.
