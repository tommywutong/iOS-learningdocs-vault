---
title: 'actionSheetCancel(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheetdelegate/actionsheetcancel(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheetcancel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheetdelegate/actionsheetcancel%28_%3A%29.json'
content_hash: 'sha256:37e2c38738d96089'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheetDelegate](../uiactionsheetdelegate.md)

# actionSheetCancel(_:)

<sub>Instance Method</sub>

Sent to the delegate before an action sheet is canceled.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func actionSheetCancel(_ actionSheet: UIActionSheet)
```

## Parameters

- `actionSheet` — The action sheet that will be canceled.

## Discussion

If the action sheet’s delegate does not implement this method, clicking the cancel button is simulated and the action sheet is dismissed. Implement this method if you need to perform some actions before an action sheet is canceled. An action sheet can be canceled at any time by the system—for example, when the user taps the Home button. The [- actionSheet:willDismissWithButtonIndex:](<actionsheet(__willdismisswithbuttonindex_).md>) and [- actionSheet:didDismissWithButtonIndex:](<actionsheet(__diddismisswithbuttonindex_).md>) methods are invoked after this method.
