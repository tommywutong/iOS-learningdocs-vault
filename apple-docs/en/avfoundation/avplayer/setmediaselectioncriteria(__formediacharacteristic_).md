---
title: 'setMediaSelectionCriteria(_:forMediaCharacteristic:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/setmediaselectioncriteria(_:formediacharacteristic:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/setmediaselectioncriteria(_:formediacharacteristic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/setmediaselectioncriteria%28_%3Aformediacharacteristic%3A%29.json'
content_hash: 'sha256:c443ad16670ee894'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# setMediaSelectionCriteria(_:forMediaCharacteristic:)

<sub>Instance Method</sub>

Applies automatic selection criteria for media that has the specified media characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria?, forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic)
```

## Parameters

- `criteria` — An instance of [AVPlayerMediaSelectionCriteria](../avplayermediaselectioncriteria.md) that specifies the selection criteria.

- `mediaCharacteristic` — The media characteristic for which the selection criteria are to be applied. Supported values include [AVMediaCharacteristicAudible](../avmediacharacteristic/audible.md), [AVMediaCharacteristicLegible](../avmediacharacteristic/legible.md), and [AVMediaCharacteristicVisual](../avmediacharacteristic/visual.md). See Media Characteristics in the `AVFoundation Constants`.

## Discussion

Criteria will be applied to an [AVPlayerItem](../avplayeritem.md) instance when:

- It is made ready to play.
- Specific media selections are made by the [AVPlayerItem](../avplayeritem.md) instance using the method [- selectMediaOption:inMediaSelectionGroup:](<../avplayeritem/select(__in_).md>) in a different group. The automatic choice in one group may be influenced by a specific selection in another group.
- Underlying system preferences change, e.g. system language, accessibility captions.

Specific selections made by the [AVPlayerItem](../avplayeritem.md) instance using the method [- selectMediaOption:inMediaSelectionGroup:](<../avplayeritem/select(__in_).md>) method within any group will override automatic selection in that group until the player item receives a [- selectMediaOptionAutomaticallyInMediaSelectionGroup:](<../avplayeritem/selectmediaoptionautomatically(in_).md>) message.

## See Also

### Configuring media selection criteria

- [appliesMediaSelectionCriteriaAutomatically](appliesmediaselectioncriteriaautomatically.md) — A Boolean value that indicates whether the receiver should apply the current selection criteria automatically to player items.
- [- mediaSelectionCriteriaForMediaCharacteristic:](<mediaselectioncriteria(formediacharacteristic_).md>) — Returns the automatic selection criteria for media items with the specified media characteristic.
