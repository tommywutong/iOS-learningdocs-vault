---
title: appliesMediaSelectionCriteriaAutomatically
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/appliesmediaselectioncriteriaautomatically
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/appliesmediaselectioncriteriaautomatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/appliesmediaselectioncriteriaautomatically.json'
content_hash: 'sha256:e8e6dbc535b347df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# appliesMediaSelectionCriteriaAutomatically

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver should apply the current selection criteria automatically to player items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var appliesMediaSelectionCriteriaAutomatically: Bool { get set }
```

## Discussion

By default, the `AVPlayer` instance applies selection criteria based on system accessibility preferences. To override the default criteria for any media selection group, use [- setMediaSelectionCriteria:forMediaCharacteristic:](<setmediaselectioncriteria(__formediacharacteristic_).md>).

> [!note] Note
> For clients linked against the iOS 7.0 and later or against the macOS 10.9 and later, the default is [true](../../swift/true.md). For all others, the default is [false](../../swift/false.md).

## See Also

### Configuring media selection criteria

- [- mediaSelectionCriteriaForMediaCharacteristic:](<mediaselectioncriteria(formediacharacteristic_).md>) — Returns the automatic selection criteria for media items with the specified media characteristic.
- [- setMediaSelectionCriteria:forMediaCharacteristic:](<setmediaselectioncriteria(__formediacharacteristic_).md>) — Applies automatic selection criteria for media that has the specified media characteristic.
