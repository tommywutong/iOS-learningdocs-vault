---
title: 'navigationItem(_:didEndRenamingWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:didendrenamingwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:didendrenamingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem%28_%3Adidendrenamingwith%3A%29.json'
content_hash: 'sha256:7aa1ad9ef5079306'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItemRenameDelegate](../uinavigationitemrenamedelegate-5j4ws.md)

# navigationItem(_:didEndRenamingWith:)

<sub>Instance Method</sub>

Tells the delegate when the rename process ends.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func navigationItem(_: UINavigationItem, didEndRenamingWith title: String)
```

## Parameters

- `_` — The navigation item with the changing title.

- `title` — The new title of the navigation item.

## Discussion

UIKit calls this method after a person finishes renaming the navigation item. Implement this method to update your data model with the new title as needed.

UIKit updates the navigation item’s title automatically. However, if you want to modify the final title that the system passes in to this method, you must update the navigation item’s title manually.

## See Also

### Handling the rename process

- [navigationItem(_:willBeginRenamingWith:selectedRange:)](<navigationitem(__willbeginrenamingwith_selectedrange_).md>) — Tells the delegate when the rename process starts.
