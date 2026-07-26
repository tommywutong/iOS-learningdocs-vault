---
title: contentInset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/contentinset
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/contentinset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/contentinset.json'
content_hash: 'sha256:49d509322e1ffaf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# contentInset

<sub>Instance Property</sub>

The custom distance that the content view is inset from the safe area or scroll view edges.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentInset: UIEdgeInsets { get set }
```

## Discussion

Use this property to extend the space between your content and the edges of the content view. The unit of size is points. The default value is [UIEdgeInsetsZero](../uiedgeinsets/zero.md).

By default, UIKit automatically adjusts the content inset to account for overlapping bars. You use this property to extend that distance even further, perhaps to accommodate your own custom content. Get the total adjustment — the safe area plus your custom insets — using the [adjustedContentInset](adjustedcontentinset.md) property. To change how the safe area is applied, modify the [contentInsetAdjustmentBehavior](contentinsetadjustmentbehavior-swift.property.md) property.

## See Also

### Managing the content inset behavior

- [adjustedContentInset](adjustedcontentinset.md) — The insets derived from the content insets and the safe area of the scroll view.
- [contentInsetAdjustmentBehavior](contentinsetadjustmentbehavior-swift.property.md) — The behavior for determining the adjusted content offsets.
- [ContentInsetAdjustmentBehavior](contentinsetadjustmentbehavior-swift.enum.md) — Constants indicating how safe area insets are added to the adjusted content inset.
- [- adjustedContentInsetDidChange](<adjustedcontentinsetdidchange().md>) — Notifies the scroll view when the adjusted content insets of the scroll view change.
