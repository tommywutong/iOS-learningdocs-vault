---
title: NSCollectionLayoutGroupCustomItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutgroupcustomitem
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutgroupcustomitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutgroupcustomitem.json'
content_hash: 'sha256:55cfe28fbe4e4186'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutGroupCustomItem

<sub>Class</sub>

An item used in a group with a custom layout arrangement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSCollectionLayoutGroupCustomItem
```

## Overview

You use a custom item if you want to specify a layout with a custom arrangement, like a radial or diagonal layout. You use custom items within a group that’s created with [+ customGroupWithLayoutSize:itemProvider:](<nscollectionlayoutgroup/custom(layoutsize_itemprovider_).md>).

Instead of providing a layout size for the custom item, like you do when you create an [NSCollectionLayoutItem](nscollectionlayoutitem.md), you provide a frame instead.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a custom item

- [+ customItemWithFrame:](<nscollectionlayoutgroupcustomitem/init(frame_).md>) — Creates a custom item with the specified frame.
- [+ customItemWithFrame:zIndex:](<nscollectionlayoutgroupcustomitem/init(frame_zindex_).md>) — Creates a custom item with the specified frame and vertical stacking order in relation to other items in the group.

### Getting the frame

- [frame](nscollectionlayoutgroupcustomitem/frame.md) — The frame of the custom item.

### Specifying stacking order

- [zIndex](nscollectionlayoutgroupcustomitem/zindex.md) — The vertical stacking order of the custom item in relation to other items in the group.

## See Also

### Advanced layouts

- [NSCollectionLayoutGroupCustomItemProvider](nscollectionlayoutgroupcustomitemprovider.md) — A closure that creates and returns each of the custom group’s items.
