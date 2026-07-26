---
title: delegate
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerviewcontroller/delegate-3zqmt
source_url: 'https://developer.apple.com/documentation/photosui/phpickerviewcontroller/delegate-3zqmt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerviewcontroller/delegate-3zqmt.json'
content_hash: 'sha256:1b0d0d0fad062b02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerViewController](../phpickerviewcontroller.md)

# delegate

<sub>Instance Property</sub>

The picker’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency weak var delegate: (any PHPickerViewControllerDelegate)? { get set }
```

## See Also

### Responding to user selection

- [PHPickerViewControllerDelegate](../phpickerviewcontrollerdelegate-5yntc.md) — A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [PHPickerResult](../phpickerresult-swift.struct.md) — Types that represent a selected asset from the user’s photo library.
