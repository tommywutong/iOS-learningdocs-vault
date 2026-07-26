---
title: textLayoutManager
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer/textlayoutmanager
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/textlayoutmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/textlayoutmanager.json'
content_hash: 'sha256:b8a6e5b4c7b2221f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# textLayoutManager

<sub>Instance Property</sub>

The [NSTextLayoutManager](../nstextlayoutmanager.md) owning the text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var textLayoutManager: NSTextLayoutManager? { get }
```

## Discussion

When non-nil, the legacy `layoutManager` should be `nil`.

## See Also

### Managing text components

- [layoutManager](layoutmanager.md) — The text container’s layout manager.
- [- replaceLayoutManager:](<replacelayoutmanager(__).md>) — Replaces the layout manager for the group of text system objects that contains the text container.
- [textView](../../appkit/nstextcontainer/textview.md) — The text container’s text view.
