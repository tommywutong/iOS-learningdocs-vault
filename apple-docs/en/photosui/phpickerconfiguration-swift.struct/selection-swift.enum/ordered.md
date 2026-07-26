---
title: PHPickerConfiguration.Selection.ordered
framework: PhotosUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum/ordered
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum/ordered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum/ordered.json'
content_hash: 'sha256:8dc90ec7c5f7c3ab'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [PhotosUI](../../../photosui.md) · [PHPickerConfiguration](../../phpickerconfiguration-swift.struct.md) · [Selection](../selection-swift.enum.md)

# PHPickerConfiguration.Selection.ordered

<sub>Case</sub>

An option that provides selected photos to the app in the chosen order after the user confirms the selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case ordered
```

## Discussion

This option notifies the app of photo selections when a person taps the Add button.

In addition, selected photos display a numbered badge that represents the order in which someone taps the photo.

## See Also

### Selection methods

- [PHPickerConfiguration.Selection.default](default.md) — An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfiguration.Selection.continuous](continuous.md) — An option that provides the app a person’s selection immediately.
- [PHPickerConfiguration.Selection.continuousAndOrdered](continuousandordered.md) — An option that provides the app a person’s selection immediately and displays selected photos with a numbered badge.
