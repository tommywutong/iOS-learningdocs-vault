---
title: PHPickerViewControllerDelegate
framework: PhotosUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerviewcontrollerdelegate-5yntc
source_url: 'https://developer.apple.com/documentation/photosui/phpickerviewcontrollerdelegate-5yntc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerviewcontrollerdelegate-5yntc.json'
content_hash: 'sha256:05a9c3b7e2c206e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHPickerViewControllerDelegate

<sub>Protocol</sub>

A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol PHPickerViewControllerDelegate : AnyObject
```

## Topics

### Instance Methods

- [picker(_:didFinishPicking:)](<phpickerviewcontrollerdelegate-5yntc/picker(__didfinishpicking_).md>) — Called when the user completes a selection or dismisses `PHPickerViewController` using the cancel button.

## See Also

### Photos picker for UIKit, AppKit

- [Selecting Photos and Videos in iOS](../photokit/selecting-photos-and-videos-in-ios.md) — Improve the user experience of finding and selecting assets by using the Photos picker.
- [PHPickerViewController](phpickerviewcontroller.md) — A view controller that provides the user interface for choosing assets from the photo library.
- [PHPickerConfiguration](phpickerconfiguration-swift.struct.md) — An object that contains information about how to configure a picker view controller.
- [PHPickerFilter](phpickerfilter-swift.struct.md) — A type that defines the filter to apply to the photo library.
- [PHPickerResult](phpickerresult-swift.struct.md) — Types that represent a selected asset from the user’s photo library.
