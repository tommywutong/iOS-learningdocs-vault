---
title: 'mediaSelectionGroup(forMediaCharacteristic:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcomposition/mediaselectiongroup(formediacharacteristic:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/mediaselectiongroup(formediacharacteristic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/mediaselectiongroup%28formediacharacteristic%3A%29.json'
content_hash: 'sha256:bddc3062e90fc5d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# mediaSelectionGroup(forMediaCharacteristic:)

<sub>Instance Method</sub>

Returns a media selection group that contains one or more options with the specified media characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> AVMediaSelectionGroup?
```

## Parameters

- `mediaCharacteristic` — A media characteristic for which to obtain the available media selection options. Only [AVMediaCharacteristicAudible](../avmediacharacteristic/audible.md), [AVMediaCharacteristicVisual](../avmediacharacteristic/visual.md), and [AVMediaCharacteristicLegible](../avmediacharacteristic/legible.md) are currently supported. - Pass [AVMediaCharacteristicAudible](../avmediacharacteristic/audible.md) to return the group of available options for audio media in various languages and for various purposes, such as descriptive audio. - Pass [AVMediaCharacteristicLegible](../avmediacharacteristic/legible.md) to return the group of available options for subtitles in various languages and for various purposes. - Pass [AVMediaCharacteristicVisual](../avmediacharacteristic/visual.md) to return the group of available options for video media.

## Return Value

An [AVMediaSelectionGroup](../avmediaselectiongroup.md) that contains one or more options with the specified media characteristic, or `nil` if none could be found.

## Discussion

Use the filtering methods [AVMediaSelectionGroup](../avmediaselectiongroup.md) defines to filter the group’s options according to playability, locale, and additional media characteristics.

You can call this method without blocking the current thread after you’ve asynchronously loaded the [availableMediaCharacteristicsWithMediaSelectionOptions](../avasset/availablemediacharacteristicswithmediaselectionoptions.md) property.

## See Also

### Accessing media selections

- [allMediaSelections](allmediaselections.md) — The array of available media selections for this asset.
- [availableMediaCharacteristicsWithMediaSelectionOptions](availablemediacharacteristicswithmediaselectionoptions.md) — An array of media characteristics for which a media selection option is available.
