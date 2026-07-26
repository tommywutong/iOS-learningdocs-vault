---
title: PHPickerConfigurationSelection
framework: PhotosUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfigurationselection
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfigurationselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfigurationselection.json'
content_hash: 'sha256:022fd35c93a9db70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHPickerConfigurationSelection

<sub>Enumeration</sub>

Options that represent differing selection behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum PHPickerConfigurationSelection
```

## Overview

This enumeration defines the possible values of the photo picker configuration ([PHPickerConfiguration](phpickerconfiguration-swift.struct.md)) property [selection](phpickerconfiguration-swift.struct/selection-swift.property.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Selection methods

- [PHPickerConfigurationSelectionDefault](phpickerconfigurationselection/default.md) — An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfigurationSelectionOrdered](phpickerconfigurationselection/ordered.md) — An option that provides selected photos to the app in the chosen order after the user confirms the selection.
- [PHPickerConfigurationSelectionContinuous](phpickerconfigurationselection/continuous.md) — An option that provides the app a person’s selection immediately.
- [PHPickerConfigurationSelectionContinuousAndOrdered](phpickerconfigurationselection/continuousandordered.md) — An option that provides the app a person’s selection immediately and displays selected photos with a numbered badge.

### Initializers

- [init(rawValue:)](<phpickerconfigurationselection/init(rawvalue_).md>)
