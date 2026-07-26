---
title: 'willPresent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheetdelegate/willpresent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/willpresent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheetdelegate/willpresent%28_%3A%29.json'
content_hash: 'sha256:1fd46b00e7595a81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheetDelegate](../uiactionsheetdelegate.md)

# willPresent(_:)

<sub>Instance Method</sub>

Sent to the delegate before an action sheet is presented to the user.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func willPresent(_ actionSheet: UIActionSheet)
```

## Parameters

- `actionSheet` — The action sheet that is about to be displayed.

## See Also

### Customizing behavior

- [- didPresentActionSheet:](<didpresent(__).md>) — Sent to the delegate after an action sheet is presented to the user. _(deprecated)_
- [- actionSheet:willDismissWithButtonIndex:](<actionsheet(__willdismisswithbuttonindex_).md>) — Sent to the delegate before an action sheet is dismissed. _(deprecated)_
- [- actionSheet:didDismissWithButtonIndex:](<actionsheet(__diddismisswithbuttonindex_).md>) — Sent to the delegate after an action sheet is dismissed from the screen. _(deprecated)_
