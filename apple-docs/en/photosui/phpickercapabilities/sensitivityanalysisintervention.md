---
title: sensitivityAnalysisIntervention
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickercapabilities/sensitivityanalysisintervention
source_url: 'https://developer.apple.com/documentation/photosui/phpickercapabilities/sensitivityanalysisintervention'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickercapabilities/sensitivityanalysisintervention.json'
content_hash: 'sha256:840337d1321a19de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerCapabilities](../phpickercapabilities.md)

# sensitivityAnalysisIntervention

<sub>Type Property</sub>

A capability that prompts for confirmation if a person selects a photo that contains nudity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var sensitivityAnalysisIntervention: PHPickerCapabilities { get }
```

## Discussion

When either the Sensitive Content Warning setting or Communication Safety parental control in Screen Time are active in iOS 17 or later, the photos picker checks whether a selected asset contains nudity. If so, the photo picker presents a model view that warns the person before giving the app access to the photo. The intervention UI requires a person to confirm that they really intend to interact with the sensitive asset in the photo library before proceeding. For more information on nudity detection in iOS 17 and later, see [Sensitive Content Analysis](../../sensitivecontentanalysis.md).

## See Also

### Specifying features

- [PHPickerCapabilitiesCollectionNavigation](collectionnavigation.md) — A capability that corresponds to a sidebar or the Albums tab.
- [PHPickerCapabilitiesSelectionActions](selectionactions.md) — A cabability that represents the Cancel and Add buttons.
- [PHPickerCapabilitiesSearch](search.md) — A capability that corresponds to the search bar.
- [PHPickerCapabilitiesStagingArea](stagingarea.md) — A capability that corresponds to an area in which the selected photos display.
