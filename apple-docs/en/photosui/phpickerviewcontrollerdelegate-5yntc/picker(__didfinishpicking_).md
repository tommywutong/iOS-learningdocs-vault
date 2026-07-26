---
title: 'picker(_:didFinishPicking:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phpickerviewcontrollerdelegate-5yntc/picker(_:didfinishpicking:)'
source_url: 'https://developer.apple.com/documentation/photosui/phpickerviewcontrollerdelegate-5yntc/picker(_:didfinishpicking:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerviewcontrollerdelegate-5yntc/picker%28_%3Adidfinishpicking%3A%29.json'
content_hash: 'sha256:6c59e86b14caf9b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerViewControllerDelegate](../phpickerviewcontrollerdelegate-5yntc.md)

# picker(_:didFinishPicking:)

<sub>Instance Method</sub>

Called when the user completes a selection or dismisses `PHPickerViewController` using the cancel button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult])
```

## Discussion

The picker won’t be automatically dismissed when this method is called.
