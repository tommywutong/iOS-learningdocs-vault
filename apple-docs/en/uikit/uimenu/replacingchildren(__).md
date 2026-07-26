---
title: 'replacingChildren(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenu/replacingchildren(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenu/replacingchildren(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenu/replacingchildren%28_%3A%29.json'
content_hash: 'sha256:6cf04930b51bce7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenu](../uimenu.md)

# replacingChildren(_:)

<sub>Instance Method</sub>

Creates a new menu with the same configuration as the current menu, but with a new set of child elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func replacingChildren(_ newChildren: [UIMenuElement]) -> UIMenu
```

## Parameters

- `newChildren` — The child elements to include in the new menu.

## Return Value

A new menu object containing the specified children.

## Discussion

The new menu contains the same title, image, identifier, and options as the current menu. The new menu contains only the children in the `newChildren` parameter. It doesn’t contain any child elements from the current menu.

## See Also

### Accessing child elements

- [children](children.md) — The contents of the menu.
