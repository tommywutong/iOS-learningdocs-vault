---
title: textLayoutManagers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentmanager/textlayoutmanagers
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/textlayoutmanagers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/textlayoutmanagers.json'
content_hash: 'sha256:1b8a6185ae8b5e47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# textLayoutManagers

<sub>Instance Property</sub>

The array of text layout managers associated with this text content manager.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textLayoutManagers: [NSTextLayoutManager] { get }
```

## Discussion

This property is KVO-compliant.

## See Also

### Working with layout managers

- [primaryTextLayoutManager](primarytextlayoutmanager.md) — The primary text layout manager for this content.
- [automaticallySynchronizesTextLayoutManagers](automaticallysynchronizestextlayoutmanagers.md) — Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [- addTextLayoutManager:](<addtextlayoutmanager(__).md>) — Adds the layout manager you provide to the list of layout managers.
- [- removeTextLayoutManager:](<removetextlayoutmanager(__).md>) — Removes the layout manager you specifiy from the list of layout managers.
- [- synchronizeTextLayoutManagers:](<synchronizetextlayoutmanagers(__).md>) — Synchronizes changes to all nonprimary text layout managers.
