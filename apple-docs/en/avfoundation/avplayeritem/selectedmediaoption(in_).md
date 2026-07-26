---
title: 'selectedMediaOption(in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（11.0 起废弃）, iPadOS 5.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.8+（10.13 起废弃）, tvOS 9.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avplayeritem/selectedmediaoption(in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/selectedmediaoption(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/selectedmediaoption%28in%3A%29.json'
content_hash: 'sha256:08b14262cd6ee648'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# selectedMediaOption(in:)

<sub>Instance Method</sub>

Returns the media selection option that’s currently selected from the specified group.

> [!warning] Deprecated
> Use [currentMediaSelection](currentmediaselection.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func selectedMediaOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?
```

## Parameters

- `mediaSelectionGroup` — A media selection group obtained from the player item’s asset.

## Return Value

An instance of [AVMediaSelectionOption](../avmediaselectionoption.md) that describes the currently selected option in the group.

## Discussion

If the value of the [allowsEmptySelection](../avmediaselectiongroup/allowsemptyselection.md) property of `mediaSelectionGroup` is [true](../../swift/true.md), the currently selected option in the group may be `nil`.
