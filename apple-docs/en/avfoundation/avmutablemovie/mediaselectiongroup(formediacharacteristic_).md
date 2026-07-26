---
title: 'mediaSelectionGroup(forMediaCharacteristic:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovie/mediaselectiongroup(formediacharacteristic:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/mediaselectiongroup(formediacharacteristic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/mediaselectiongroup%28formediacharacteristic%3A%29.json'
content_hash: 'sha256:dc6aeb339d279852'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# mediaSelectionGroup(forMediaCharacteristic:)

<sub>Instance Method</sub>

Returns a media selection group that contains one or more options with the specified media characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

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
