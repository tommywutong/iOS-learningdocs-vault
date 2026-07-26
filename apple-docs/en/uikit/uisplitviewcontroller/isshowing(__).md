---
title: 'isShowing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontroller/isshowing(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/isshowing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/isshowing%28_%3A%29.json'
content_hash: 'sha256:40f0df24d33a099e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# isShowing(_:)

<sub>Instance Method</sub>

A Boolean value that indicates whether the split view interface is showing the specified column.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func isShowing(_ column: UISplitViewController.Column) -> Bool
```

## See Also

### Displaying the child view controllers

- [- showColumn:](<show(__).md>) — Presents the view controller in the specified column of the split view interface.
- [- hideColumn:](<hide(__).md>) — Dismisses the view controller in the specified column of the split view interface.
- [- showViewController:sender:](<show(__sender_).md>) — Presents the specified view controller as the primary view controller in the split view interface.
- [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>) — Presents the specified view controller as the secondary view controller of the split view interface.
