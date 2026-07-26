---
title: PHPickerCapabilities
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickercapabilities
source_url: 'https://developer.apple.com/documentation/photosui/phpickercapabilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickercapabilities.json'
content_hash: 'sha256:4acac9969059a3d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHPickerCapabilities

<sub>Structure</sub>

Options that customize the look and behavior of the photos picker.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct PHPickerCapabilities
```

## Overview

This enumeration defines the possible values for the photo picker configuration ([PHPickerConfiguration](phpickerconfiguration-swift.struct.md)) property [disabledCapabilities](phpickerconfiguration-swift.struct/disabledcapabilities.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Specifying features

- [PHPickerCapabilitiesCollectionNavigation](phpickercapabilities/collectionnavigation.md) — A capability that corresponds to a sidebar or the Albums tab.
- [PHPickerCapabilitiesSelectionActions](phpickercapabilities/selectionactions.md) — A cabability that represents the Cancel and Add buttons.
- [PHPickerCapabilitiesSearch](phpickercapabilities/search.md) — A capability that corresponds to the search bar.
- [PHPickerCapabilitiesSensitivityAnalysisIntervention](phpickercapabilities/sensitivityanalysisintervention.md) — A capability that prompts for confirmation if a person selects a photo that contains nudity.
- [PHPickerCapabilitiesStagingArea](phpickercapabilities/stagingarea.md) — A capability that corresponds to an area in which the selected photos display.

### Creating a capability

- [init(rawValue:)](<phpickercapabilities/init(rawvalue_).md>) — Creates a photo picker capability.
