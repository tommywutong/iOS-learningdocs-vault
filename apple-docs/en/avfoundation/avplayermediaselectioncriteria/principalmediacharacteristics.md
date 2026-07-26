---
title: principalMediaCharacteristics
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayermediaselectioncriteria/principalmediacharacteristics
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/principalmediacharacteristics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayermediaselectioncriteria/principalmediacharacteristics.json'
content_hash: 'sha256:88645f079be09c54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerMediaSelectionCriteria](../avplayermediaselectioncriteria.md)

# principalMediaCharacteristics

<sub>Instance Property</sub>

An array of media characteristics that are essential to select when choosing media with a particular characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var principalMediaCharacteristics: [AVMediaCharacteristic]? { get }
```

## Discussion

If no option matches the principal media characteristics, the system chooses the default option in the group as the best match.

When making automatic selections, a player item treats principal media characteristics as criteria that supersede language preferences and preferred media characteristics.

> [!important] Important
> Use principal media characteristics with caution. It’s typical to support accessibility features using a combination of language preferences and preferred characteristics, and not using principal media characteristics.

## See Also

### Retrieving selection criteria settings

- [preferredLanguages](preferredlanguages.md) — An array of language identifiers in preferred order.
- [preferredMediaCharacteristics](preferredmediacharacteristics.md) — An array of media characteristics in preferred order.
