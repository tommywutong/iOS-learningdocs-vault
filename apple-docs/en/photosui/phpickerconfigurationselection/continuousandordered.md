---
title: PHPickerConfigurationSelection.continuousAndOrdered
framework: PhotosUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfigurationselection/continuousandordered
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfigurationselection/continuousandordered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfigurationselection/continuousandordered.json'
content_hash: 'sha256:fbcb5496533f3ad7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerConfigurationSelection](../phpickerconfigurationselection.md)

# PHPickerConfigurationSelection.continuousAndOrdered

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

- [PHPickerConfigurationSelectionDefault](default.md) — An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfigurationSelectionOrdered](ordered.md) — An option that provides selected photos to the app in the chosen order after the user confirms the selection.
- [PHPickerConfigurationSelectionContinuous](continuous.md) — An option that provides the app a person’s selection immediately.
