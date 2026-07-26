---
title: 'mediaSelectionCriteriaCanBeAppliedAutomatically(to:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediaselection/mediaselectioncriteriacanbeappliedautomatically(to:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselection/mediaselectioncriteriacanbeappliedautomatically(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselection/mediaselectioncriteriacanbeappliedautomatically%28to%3A%29.json'
content_hash: 'sha256:2f7ad4aa63b38ce7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelection](../avmediaselection.md)

# mediaSelectionCriteriaCanBeAppliedAutomatically(to:)

<sub>Instance Method</sub>

Indicates whether the specified media selection group is subject to automatic media selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mediaSelectionCriteriaCanBeAppliedAutomatically(to mediaSelectionGroup: AVMediaSelectionGroup) -> Bool
```

## Parameters

- `mediaSelectionGroup` — A media selection group obtained from the associated asset.

## Return Value

A Boolean value indicating whether the group is subject to automatic media selection.

## Discussion

The automatic application of media selection criteria is suspended in any group in which a specific selection has been made by calling [- selectMediaOption:inMediaSelectionGroup:](<../avplayeritem/select(__in_).md>) on the current [AVPlayerItem](../avplayeritem.md).

## See Also

### Inspecting the media selection

- [- selectedMediaOptionInMediaSelectionGroup:](<selectedmediaoption(in_).md>) — Returns the media selection option that’s currently selected in the specified group.
