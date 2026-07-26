---
title: 'mediaSelectionCriteria(forMediaCharacteristic:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/mediaselectioncriteria(formediacharacteristic:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/mediaselectioncriteria(formediacharacteristic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/mediaselectioncriteria%28formediacharacteristic%3A%29.json'
content_hash: 'sha256:b1b2751d17730ec5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# mediaSelectionCriteria(forMediaCharacteristic:)

<sub>Instance Method</sub>

Returns the automatic selection criteria for media items with the specified media characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func mediaSelectionCriteria(forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> AVPlayerMediaSelectionCriteria?
```

## Parameters

- `mediaCharacteristic` — The media characteristic for which the selection criteria is to be returned. Supported values include [AVMediaCharacteristicAudible](../avmediacharacteristic/audible.md), [AVMediaCharacteristicLegible](../avmediacharacteristic/legible.md), and [AVMediaCharacteristicVisual](../avmediacharacteristic/visual.md).

## Return Value

The [AVPlayerMediaSelectionCriteria](../avplayermediaselectioncriteria.md) for `mediaCharacteristic`.

## See Also

### Configuring media selection criteria

- [appliesMediaSelectionCriteriaAutomatically](appliesmediaselectioncriteriaautomatically.md) — A Boolean value that indicates whether the receiver should apply the current selection criteria automatically to player items.
- [- setMediaSelectionCriteria:forMediaCharacteristic:](<setmediaselectioncriteria(__formediacharacteristic_).md>) — Applies automatic selection criteria for media that has the specified media characteristic.
