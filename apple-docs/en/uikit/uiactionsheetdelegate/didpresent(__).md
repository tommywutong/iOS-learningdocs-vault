---
title: 'didPresent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheetdelegate/didpresent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/didpresent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheetdelegate/didpresent%28_%3A%29.json'
content_hash: 'sha256:0660ab7bbffc8b37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheetDelegate](../uiactionsheetdelegate.md)

# didPresent(_:)

<sub>Instance Method</sub>

Sent to the delegate after an action sheet is presented to the user.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func didPresent(_ actionSheet: UIActionSheet)
```

## Parameters

- `actionSheet` — The action sheet that was displayed.

## See Also

### Customizing behavior

- [- willPresentActionSheet:](<willpresent(__).md>) — Sent to the delegate before an action sheet is presented to the user. _(deprecated)_
- [- actionSheet:willDismissWithButtonIndex:](<actionsheet(__willdismisswithbuttonindex_).md>) — Sent to the delegate before an action sheet is dismissed. _(deprecated)_
- [- actionSheet:didDismissWithButtonIndex:](<actionsheet(__diddismisswithbuttonindex_).md>) — Sent to the delegate after an action sheet is dismissed from the screen. _(deprecated)_
