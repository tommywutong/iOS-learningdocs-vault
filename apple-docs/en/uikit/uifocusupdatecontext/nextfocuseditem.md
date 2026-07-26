---
title: nextFocusedItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusupdatecontext/nextfocuseditem
source_url: 'https://developer.apple.com/documentation/uikit/uifocusupdatecontext/nextfocuseditem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusupdatecontext/nextfocuseditem.json'
content_hash: 'sha256:4aeb7b28cf8d1a56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusUpdateContext](../uifocusupdatecontext.md)

# nextFocusedItem

<sub>Instance Property</sub>

The item to be focused after the update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var nextFocusedItem: (any UIFocusItem)? { get }
```

## Discussion

This property is set to `nil` if no item is receiving the focus.

## See Also

### Getting related focus items

- [previouslyFocusedItem](previouslyfocuseditem.md) — The item that was focused before the update.
