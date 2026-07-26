---
title: contentInsetAdjustmentBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.property.json'
content_hash: 'sha256:788ab842d17186ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# contentInsetAdjustmentBehavior

<sub>Instance Property</sub>

The behavior for determining the adjusted content offsets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior { get set }
```

## Discussion

This property specifies how the safe area insets are used to modify the content area of the scroll view. The default value of this property is [UIScrollViewContentInsetAdjustmentAutomatic](contentinsetadjustmentbehavior-swift.enum/automatic.md).

## See Also

### Managing the content inset behavior

- [adjustedContentInset](adjustedcontentinset.md) — The insets derived from the content insets and the safe area of the scroll view.
- [contentInset](contentinset.md) — The custom distance that the content view is inset from the safe area or scroll view edges.
- [ContentInsetAdjustmentBehavior](contentinsetadjustmentbehavior-swift.enum.md) — Constants indicating how safe area insets are added to the adjusted content inset.
- [- adjustedContentInsetDidChange](<adjustedcontentinsetdidchange().md>) — Notifies the scroll view when the adjusted content insets of the scroll view change.
