---
title: PHPickerConfigurationSelection.ordered
framework: PhotosUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfigurationselection/ordered
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfigurationselection/ordered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfigurationselection/ordered.json'
content_hash: 'sha256:c8fe0765e7b52d96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerConfigurationSelection](../phpickerconfigurationselection.md)

# PHPickerConfigurationSelection.ordered

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

- [PHPickerConfigurationSelectionDefault](default.md) — An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfigurationSelectionContinuous](continuous.md) — An option that provides the app a person’s selection immediately.
- [PHPickerConfigurationSelectionContinuousAndOrdered](continuousandordered.md) — An option that provides the app a person’s selection immediately and displays selected photos with a numbered badge.
