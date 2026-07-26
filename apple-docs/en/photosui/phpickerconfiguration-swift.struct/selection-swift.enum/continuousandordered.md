---
title: PHPickerConfiguration.Selection.continuousAndOrdered
framework: PhotosUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum/continuousandordered
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum/continuousandordered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum/continuousandordered.json'
content_hash: 'sha256:8c62fc698cfecf7c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [PhotosUI](../../../photosui.md) · [PHPickerConfiguration](../../phpickerconfiguration-swift.struct.md) · [Selection](../selection-swift.enum.md)

# PHPickerConfiguration.Selection.continuousAndOrdered

<sub>Case</sub>

An option that provides the app a person’s selection immediately and displays selected photos with a numbered badge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case continuousAndOrdered
```

## Discussion

This option notifies the app of photo selections dynamically, as someone taps the photo picker.

In addition, selected photos display a numbered badge that represents the order in which someone taps the photo.

## See Also

### Selection methods

- [PHPickerConfiguration.Selection.default](default.md) — An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfiguration.Selection.ordered](ordered.md) — An option that provides selected photos to the app in the chosen order after the user confirms the selection.
- [PHPickerConfiguration.Selection.continuous](continuous.md) — An option that provides the app a person’s selection immediately.
