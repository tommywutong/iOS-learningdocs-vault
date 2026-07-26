---
title: 'replaceLayoutManager(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontainer/replacelayoutmanager(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/replacelayoutmanager(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/replacelayoutmanager%28_%3A%29.json'
content_hash: 'sha256:f42fca95137a6331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# replaceLayoutManager(_:)

<sub>Instance Method</sub>

Replaces the layout manager for the group of text system objects that contains the text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func replaceLayoutManager(_ newLayoutManager: NSLayoutManager)
```

## Parameters

- `newLayoutManager` — The new layout manager.

## Discussion

The framework reassigns all text containers and text views attached to the old layout manager to the new layout manager. Unlike setting the [layoutManager](layoutmanager.md) property directly, this method makes all the adjustments necessary to keep the text object relationships intact.

## See Also

### Managing text components

- [layoutManager](layoutmanager.md) — The text container’s layout manager.
- [textLayoutManager](textlayoutmanager.md) — The [NSTextLayoutManager](../nstextlayoutmanager.md) owning the text container.
- [textView](../../appkit/nstextcontainer/textview.md) — The text container’s text view.
