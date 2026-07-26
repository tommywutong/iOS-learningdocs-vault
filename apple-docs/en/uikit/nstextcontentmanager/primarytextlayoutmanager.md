---
title: primaryTextLayoutManager
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentmanager/primarytextlayoutmanager
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/primarytextlayoutmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/primarytextlayoutmanager.json'
content_hash: 'sha256:7693145d29c48873'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# primaryTextLayoutManager

<sub>Instance Property</sub>

The primary text layout manager for this content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var primaryTextLayoutManager: NSTextLayoutManager? { get set }
```

## Discussion

Setting this property to an [NSTextLayoutManager](../nstextlayoutmanager.md) not in `textLayoutManagers` resets it to `nil`. It automatically synchronizes pending edits before switching to a new primary object. The operation is synchronous.

This property is KVO-compliant.

## See Also

### Working with layout managers

- [textLayoutManagers](textlayoutmanagers.md) — The array of text layout managers associated with this text content manager.
- [automaticallySynchronizesTextLayoutManagers](automaticallysynchronizestextlayoutmanagers.md) — Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [- addTextLayoutManager:](<addtextlayoutmanager(__).md>) — Adds the layout manager you provide to the list of layout managers.
- [- removeTextLayoutManager:](<removetextlayoutmanager(__).md>) — Removes the layout manager you specifiy from the list of layout managers.
- [- synchronizeTextLayoutManagers:](<synchronizetextlayoutmanagers(__).md>) — Synchronizes changes to all nonprimary text layout managers.
