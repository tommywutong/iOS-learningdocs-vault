---
title: 'actionSheet(_:clickedButtonAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheetdelegate/actionsheet(_:clickedbuttonat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:clickedbuttonat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheetdelegate/actionsheet%28_%3Aclickedbuttonat%3A%29.json'
content_hash: 'sha256:4c5ae20ab91021f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheetDelegate](../uiactionsheetdelegate.md)

# actionSheet(_:clickedButtonAt:)

<sub>Instance Method</sub>

Sent to the delegate when the user clicks a button on an action sheet.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func actionSheet(_ actionSheet: UIActionSheet, clickedButtonAt buttonIndex: Int)
```

## Parameters

- `actionSheet` — The action sheet containing the button.

- `buttonIndex` — The position of the clicked button. The button indices start at `0`.

## Discussion

The receiver is automatically dismissed after this method is invoked.
