---
title: automaticallySynchronizesTextLayoutManagers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentmanager/automaticallysynchronizestextlayoutmanagers
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/automaticallysynchronizestextlayoutmanagers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/automaticallysynchronizestextlayoutmanagers.json'
content_hash: 'sha256:63bcc0f97bcb664d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# automaticallySynchronizesTextLayoutManagers

<sub>Instance Property</sub>

Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallySynchronizesTextLayoutManagers: Bool { get set }
```

## See Also

### Working with layout managers

- [primaryTextLayoutManager](primarytextlayoutmanager.md) — The primary text layout manager for this content.
- [textLayoutManagers](textlayoutmanagers.md) — The array of text layout managers associated with this text content manager.
- [- addTextLayoutManager:](<addtextlayoutmanager(__).md>) — Adds the layout manager you provide to the list of layout managers.
- [- removeTextLayoutManager:](<removetextlayoutmanager(__).md>) — Removes the layout manager you specifiy from the list of layout managers.
- [- synchronizeTextLayoutManagers:](<synchronizetextlayoutmanagers(__).md>) — Synchronizes changes to all nonprimary text layout managers.
