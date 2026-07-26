---
title: 'addTextLayoutManager(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentmanager/addtextlayoutmanager(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/addtextlayoutmanager(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/addtextlayoutmanager%28_%3A%29.json'
content_hash: 'sha256:c272dd7af76b22ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# addTextLayoutManager(_:)

<sub>Instance Method</sub>

Adds the layout manager you provide to the list of layout managers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addTextLayoutManager(_ textLayoutManager: NSTextLayoutManager)
```

## Parameters

- `textLayoutManager` — The layout manager to add.

## See Also

### Working with layout managers

- [primaryTextLayoutManager](primarytextlayoutmanager.md) — The primary text layout manager for this content.
- [textLayoutManagers](textlayoutmanagers.md) — The array of text layout managers associated with this text content manager.
- [automaticallySynchronizesTextLayoutManagers](automaticallysynchronizestextlayoutmanagers.md) — Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [- removeTextLayoutManager:](<removetextlayoutmanager(__).md>) — Removes the layout manager you specifiy from the list of layout managers.
- [- synchronizeTextLayoutManagers:](<synchronizetextlayoutmanagers(__).md>) — Synchronizes changes to all nonprimary text layout managers.
