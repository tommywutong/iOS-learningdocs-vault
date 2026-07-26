---
title: adjustedContentInset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/adjustedcontentinset
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/adjustedcontentinset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/adjustedcontentinset.json'
content_hash: 'sha256:68d54b365dad880c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# adjustedContentInset

<sub>Instance Property</sub>

The insets derived from the content insets and the safe area of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var adjustedContentInset: UIEdgeInsets { get }
```

## Discussion

Use this property to obtain the adjusted area in which to draw content. The [contentInsetAdjustmentBehavior](contentinsetadjustmentbehavior-swift.property.md) property determines whether the safe area insets are included in the adjustment. The safe area insets are then added to the values in the [contentInset](contentinset.md) property to obtain the final value of this property.

## See Also

### Managing the content inset behavior

- [contentInset](contentinset.md) — The custom distance that the content view is inset from the safe area or scroll view edges.
- [contentInsetAdjustmentBehavior](contentinsetadjustmentbehavior-swift.property.md) — The behavior for determining the adjusted content offsets.
- [ContentInsetAdjustmentBehavior](contentinsetadjustmentbehavior-swift.enum.md) — Constants indicating how safe area insets are added to the adjusted content inset.
- [- adjustedContentInsetDidChange](<adjustedcontentinsetdidchange().md>) — Notifies the scroll view when the adjusted content insets of the scroll view change.
