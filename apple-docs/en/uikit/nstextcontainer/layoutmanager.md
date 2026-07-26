---
title: layoutManager
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer/layoutmanager
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/layoutmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/layoutmanager.json'
content_hash: 'sha256:aefad36f5da9ec0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# layoutManager

<sub>Instance Property</sub>

The text container’s layout manager.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
unowned(unsafe) var layoutManager: NSLayoutManager? { get set }
```

## Discussion

Avoid assigning a layout manager directly through this property. Instead, use the [- replaceLayoutManager:](<replacelayoutmanager(__).md>) method when you want to replace the layout manager. The framework sets the value of this property automatically when you add a text container to your layout manager using the [- addTextContainer:](<../nslayoutmanager/addtextcontainer(__).md>) method.

## See Also

### Related Documentation

- [- addTextContainer:](<../nslayoutmanager/addtextcontainer(__).md>) — Appends the specified text container to the series of text containers where the layout manager arranges text.

### Managing text components

- [textLayoutManager](textlayoutmanager.md) — The [NSTextLayoutManager](../nstextlayoutmanager.md) owning the text container.
- [- replaceLayoutManager:](<replacelayoutmanager(__).md>) — Replaces the layout manager for the group of text system objects that contains the text container.
- [textView](../../appkit/nstextcontainer/textview.md) — The text container’s text view.
