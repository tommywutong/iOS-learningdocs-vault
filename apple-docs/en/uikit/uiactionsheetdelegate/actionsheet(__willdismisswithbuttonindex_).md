---
title: 'actionSheet(_:willDismissWithButtonIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheetdelegate/actionsheet(_:willdismisswithbuttonindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:willdismisswithbuttonindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheetdelegate/actionsheet%28_%3Awilldismisswithbuttonindex%3A%29.json'
content_hash: 'sha256:b9a8761100215387'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheetDelegate](../uiactionsheetdelegate.md)

# actionSheet(_:willDismissWithButtonIndex:)

<sub>Instance Method</sub>

Sent to the delegate before an action sheet is dismissed.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func actionSheet(_ actionSheet: UIActionSheet, willDismissWithButtonIndex buttonIndex: Int)
```

## Parameters

- `actionSheet` — The action sheet that is about to be dismissed.

- `buttonIndex` — The index of the button that was clicked. If this is the cancel button index, the action sheet is canceling. If `-1`, the cancel button index is not set.

## Discussion

This method is invoked before the animation begins and the view is hidden.

## See Also

### Customizing behavior

- [- willPresentActionSheet:](<willpresent(__).md>) — Sent to the delegate before an action sheet is presented to the user. _(deprecated)_
- [- didPresentActionSheet:](<didpresent(__).md>) — Sent to the delegate after an action sheet is presented to the user. _(deprecated)_
- [- actionSheet:didDismissWithButtonIndex:](<actionsheet(__diddismisswithbuttonindex_).md>) — Sent to the delegate after an action sheet is dismissed from the screen. _(deprecated)_
