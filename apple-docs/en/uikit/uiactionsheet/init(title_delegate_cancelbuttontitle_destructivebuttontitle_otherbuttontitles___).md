---
title: 'init(title:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 2.0+（8.3 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheet/init(title:delegate:cancelbuttontitle:destructivebuttontitle:otherbuttontitles:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/init(title:delegate:cancelbuttontitle:destructivebuttontitle:otherbuttontitles:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/init%28title%3Adelegate%3Acancelbuttontitle%3Adestructivebuttontitle%3Aotherbuttontitles%3A_%3A%29.json'
content_hash: 'sha256:44ffdf0d7d7a6598'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# init(title:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:_:)

<sub>Initializer</sub>

Creates an action sheet with the specified values.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency convenience init(title: String?, delegate: (any UIActionSheetDelegate)?, cancelButtonTitle: String?, destructiveButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...)
```

## See Also

### Creating action sheets

- [- initWithTitle:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:](<init(title_delegate_cancelbuttontitle_destructivebuttontitle_).md>) — Initializes the action sheet using the specified starting parameters. _(deprecated)_
