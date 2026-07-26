---
title: 'mediaSelectionGroup(forMediaCharacteristic:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（16.0 起废弃）, iPadOS 5.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasset/mediaselectiongroup(formediacharacteristic:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/mediaselectiongroup(formediacharacteristic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/mediaselectiongroup%28formediacharacteristic%3A%29.json'
content_hash: 'sha256:259e5dbc73d66d1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# mediaSelectionGroup(forMediaCharacteristic:)

<sub>Instance Method</sub>

Returns a media selection group that contains one or more options with the specified media characteristic.

> [!warning] Deprecated
> Use [- loadMediaSelectionGroupForMediaCharacteristic:completionHandler:](<loadmediaselectiongroup(for_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> AVMediaSelectionGroup?
```

## Parameters

- `mediaCharacteristic` — A media characteristic for which to obtain the available media selection options. Only [AVMediaCharacteristicAudible](../avmediacharacteristic/audible.md), [AVMediaCharacteristicVisual](../avmediacharacteristic/visual.md), and [AVMediaCharacteristicLegible](../avmediacharacteristic/legible.md) are currently supported. - Pass [AVMediaCharacteristicAudible](../avmediacharacteristic/audible.md) to return the group of available options for audio media in various languages and for various purposes, such as descriptive audio. - Pass [AVMediaCharacteristicLegible](../avmediacharacteristic/legible.md) to return the group of available options for subtitles in various languages and for various purposes. - Pass [AVMediaCharacteristicVisual](../avmediacharacteristic/visual.md) to return the group of available options for video media.

## Return Value

An [AVMediaSelectionGroup](../avmediaselectiongroup.md) that contains one or more options with the specified media characteristic, or `nil` if none could be found.

## Discussion

Use the filtering methods [AVMediaSelectionGroup](../avmediaselectiongroup.md) defines to filter the group’s options according to playability, locale, and additional media characteristics.

You can call this method without blocking the current thread after you’ve asynchronously loaded the [availableMediaCharacteristicsWithMediaSelectionOptions](availablemediacharacteristicswithmediaselectionoptions.md) property.
