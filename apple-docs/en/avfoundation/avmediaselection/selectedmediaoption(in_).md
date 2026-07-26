---
title: 'selectedMediaOption(in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediaselection/selectedmediaoption(in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselection/selectedmediaoption(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselection/selectedmediaoption%28in%3A%29.json'
content_hash: 'sha256:648ecd4f0fec02a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelection](../avmediaselection.md)

# selectedMediaOption(in:)

<sub>Instance Method</sub>

Returns the media selection option that’s currently selected in the specified group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func selectedMediaOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?
```

## Parameters

- `mediaSelectionGroup` — A media selection group obtained from the associated asset.

## Return Value

The currently selected [AVMediaSelectionOption](../avmediaselectionoption.md). The return value may be `nil`.

## Discussion

This method returns the currently selected [AVMediaSelectionOption](../avmediaselectionoption.md) in the specified [AVMediaSelectionGroup](../avmediaselectiongroup.md), but may return `nil` if media selection group’s [allowsEmptySelection](../avmediaselectiongroup/allowsemptyselection.md) is set to [true](../../swift/true.md).

## See Also

### Inspecting the media selection

- [- mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup:](<mediaselectioncriteriacanbeappliedautomatically(to_).md>) — Indicates whether the specified media selection group is subject to automatic media selection.
