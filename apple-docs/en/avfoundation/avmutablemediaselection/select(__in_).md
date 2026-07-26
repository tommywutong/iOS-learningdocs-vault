---
title: 'select(_:in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemediaselection/select(_:in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemediaselection/select(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemediaselection/select%28_%3Ain%3A%29.json'
content_hash: 'sha256:b0ce8c525898548e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMediaSelection](../avmutablemediaselection.md)

# select(_:in:)

<sub>Instance Method</sub>

Selects the media option in the specified media selection group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func select(_ mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup)
```

## Parameters

- `mediaSelectionOption` — The media selection option to select.

- `mediaSelectionGroup` — The media selection group containing the specified media selection option.

## Discussion

This method selects the [AVMediaSelectionOption](../avmediaselectionoption.md) in the specified [AVMediaSelectionGroup](../avmediaselectiongroup.md) and deselects all other options in that group. If the specified media selection option isn’t a member of the specified media selection group, no change in state will be made. If the media selection group’s [allowsEmptySelection](../avmediaselectiongroup/allowsemptyselection.md) property is set to [true](../../swift/true.md), you can pass `nil` for `mediaSelectionOption` argument to deselect all media selection options in the group.
