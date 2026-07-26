---
title: previouslyFocusedItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusupdatecontext/previouslyfocuseditem
source_url: 'https://developer.apple.com/documentation/uikit/uifocusupdatecontext/previouslyfocuseditem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusupdatecontext/previouslyfocuseditem.json'
content_hash: 'sha256:4921ca63587a8fee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusUpdateContext](../uifocusupdatecontext.md)

# previouslyFocusedItem

<sub>Instance Property</sub>

The item that was focused before the update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var previouslyFocusedItem: (any UIFocusItem)? { get }
```

## Discussion

This property is set to `nil` when there was no previously focused item.

## See Also

### Getting related focus items

- [nextFocusedItem](nextfocuseditem.md) — The item to be focused after the update.
