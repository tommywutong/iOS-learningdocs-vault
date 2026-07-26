---
title: UINavigationItem.LargeTitleDisplayMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/largetitledisplaymode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/largetitledisplaymode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/largetitledisplaymode-swift.enum.json'
content_hash: 'sha256:65def040c5a20114'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# UINavigationItem.LargeTitleDisplayMode

<sub>Enumeration</sub>

Constants that indicate how to size the title of this item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum LargeTitleDisplayMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UINavigationItemLargeTitleDisplayModeAutomatic](largetitledisplaymode-swift.enum/automatic.md) — Inherit the display mode from the previous navigation item.
- [UINavigationItemLargeTitleDisplayModeAlways](largetitledisplaymode-swift.enum/always.md) — Always display a large title.
- [UINavigationItemLargeTitleDisplayModeNever](largetitledisplaymode-swift.enum/never.md) — Never display a large title.

### Enumeration Cases

- [UINavigationItemLargeTitleDisplayModeInline](largetitledisplaymode-swift.enum/inline.md) — Always use a large title when this item is topmost. If there is a back button present, this will revert to `Always`. Leading & center items will move to the overflow menu if present.

### Initializers

- [init(rawValue:)](<largetitledisplaymode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring the title

- [title](title.md) — The navigation item’s title that displays in the navigation bar.
- [attributedTitle](attributedtitle-25fxb.md)
- [largeTitle](largetitle.md) — String to be used as the large title.
- [largeTitleDisplayMode](largetitledisplaymode-swift.property.md) — The mode for displaying the title of the navigation bar.
