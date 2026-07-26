---
title: UIScrollView.ContentInsetAdjustmentBehavior
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum.json'
content_hash: 'sha256:bcb3dd8dce0193b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# UIScrollView.ContentInsetAdjustmentBehavior

<sub>Enumeration</sub>

Constants indicating how safe area insets are added to the adjusted content inset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ContentInsetAdjustmentBehavior
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UIScrollViewContentInsetAdjustmentAlways](contentinsetadjustmentbehavior-swift.enum/always.md) — Always include the safe area insets in the content adjustment.
- [UIScrollViewContentInsetAdjustmentAutomatic](contentinsetadjustmentbehavior-swift.enum/automatic.md) — Automatically adjust the scroll view insets.
- [UIScrollViewContentInsetAdjustmentNever](contentinsetadjustmentbehavior-swift.enum/never.md) — Do not adjust the scroll view insets.
- [UIScrollViewContentInsetAdjustmentScrollableAxes](contentinsetadjustmentbehavior-swift.enum/scrollableaxes.md) — Adjust the insets only in the scrollable directions.

### Initializers

- [init(rawValue:)](<contentinsetadjustmentbehavior-swift.enum/init(rawvalue_).md>)

## See Also

### Managing the content inset behavior

- [adjustedContentInset](adjustedcontentinset.md) — The insets derived from the content insets and the safe area of the scroll view.
- [contentInset](contentinset.md) — The custom distance that the content view is inset from the safe area or scroll view edges.
- [contentInsetAdjustmentBehavior](contentinsetadjustmentbehavior-swift.property.md) — The behavior for determining the adjusted content offsets.
- [- adjustedContentInsetDidChange](<adjustedcontentinsetdidchange().md>) — Notifies the scroll view when the adjusted content insets of the scroll view change.
