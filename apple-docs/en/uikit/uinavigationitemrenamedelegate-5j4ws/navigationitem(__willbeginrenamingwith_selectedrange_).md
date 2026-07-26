---
title: 'navigationItem(_:willBeginRenamingWith:selectedRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:willbeginrenamingwith:selectedrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:willbeginrenamingwith:selectedrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem%28_%3Awillbeginrenamingwith%3Aselectedrange%3A%29.json'
content_hash: 'sha256:52601284061c4aaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItemRenameDelegate](../uinavigationitemrenamedelegate-5j4ws.md)

# navigationItem(_:willBeginRenamingWith:selectedRange:)

<sub>Instance Method</sub>

Tells the delegate when the rename process starts.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func navigationItem(_: UINavigationItem, willBeginRenamingWith suggestedTitle: String, selectedRange: Range<String.Index>) -> (String, Range<String.Index>)
```

## Parameters

- `_` — The navigation item with the changing title.

- `suggestedTitle` — The initial text to appear in the rename text field.

- `selectedRange` — The selected range of the initial text in the rename text field.

## Return Value

A string that contains the initial text that appears in the rename text field, and a range that determines which part of that text has selection.

## Discussion

UIKit calls this method when the rename process begins. Implement this method to customize the initial text and text selection that appears in the rename text field.

## Default Implementations

### UINavigationItemRenameDelegate Implementations

- [navigationItem(_:willBeginRenamingWith:selectedRange:)](<navigationitem(__willbeginrenamingwith_selectedrange_)-396y6.md>)

## See Also

### Handling the rename process

- [navigationItem(_:didEndRenamingWith:)](<navigationitem(__didendrenamingwith_).md>) — Tells the delegate when the rename process ends.
