---
title: 'actionSheet(_:didDismissWithButtonIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheetdelegate/actionsheet(_:diddismisswithbuttonindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:diddismisswithbuttonindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheetdelegate/actionsheet%28_%3Adiddismisswithbuttonindex%3A%29.json'
content_hash: 'sha256:d45699dea2209aad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheetDelegate](../uiactionsheetdelegate.md)

# actionSheet(_:didDismissWithButtonIndex:)

<sub>Instance Method</sub>

Sent to the delegate after an action sheet is dismissed from the screen.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func actionSheet(_ actionSheet: UIActionSheet, didDismissWithButtonIndex buttonIndex: Int)
```

## Parameters

- `actionSheet` — The action sheet that was dismissed.

- `buttonIndex` — The index of the button that was clicked. The button indices start at `0`. If this is the cancel button index, the action sheet is canceling. If `-1`, the cancel button index is not set.

## Discussion

This method is invoked after the animation ends and the view is hidden.

## See Also

### Customizing behavior

- [- willPresentActionSheet:](<willpresent(__).md>) — Sent to the delegate before an action sheet is presented to the user. _(deprecated)_
- [- didPresentActionSheet:](<didpresent(__).md>) — Sent to the delegate after an action sheet is presented to the user. _(deprecated)_
- [- actionSheet:willDismissWithButtonIndex:](<actionsheet(__willdismisswithbuttonindex_).md>) — Sent to the delegate before an action sheet is dismissed. _(deprecated)_
