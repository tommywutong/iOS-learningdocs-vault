---
title: PHPickerConfiguration.Selection
framework: PhotosUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfiguration-swift.struct/selection-swift.enum.json'
content_hash: 'sha256:7a4e584cc76257f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerConfiguration](../phpickerconfiguration-swift.struct.md)

# PHPickerConfiguration.Selection

<sub>Enumeration</sub>

Options that represent differing selection behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum Selection
```

## Overview

This enumeration defines the possible values of the photo picker configuration ([PHPickerConfiguration](../phpickerconfiguration-swift.struct.md)) property [selection](selection-swift.property.md).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Selection methods

- [PHPickerConfiguration.Selection.default](selection-swift.enum/default.md) — An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfiguration.Selection.ordered](selection-swift.enum/ordered.md) — An option that provides selected photos to the app in the chosen order after the user confirms the selection.
- [PHPickerConfiguration.Selection.continuous](selection-swift.enum/continuous.md) — An option that provides the app a person’s selection immediately.
- [PHPickerConfiguration.Selection.continuousAndOrdered](selection-swift.enum/continuousandordered.md) — An option that provides the app a person’s selection immediately and displays selected photos with a numbered badge.

## See Also

### Setting the selection limit

- [selectionLimit](selectionlimit.md) — The maximum number of selections the user can make.
- [selection](selection-swift.property.md) — The selection behavior for the picker.
- [PHPickerConfigurationSelection](../phpickerconfigurationselection.md) — Options that represent differing selection behavior.
