---
title: 'init(title:delegate:cancelButtonTitle:destructiveButtonTitle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheet/init(title:delegate:cancelbuttontitle:destructivebuttontitle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/init(title:delegate:cancelbuttontitle:destructivebuttontitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/init%28title%3Adelegate%3Acancelbuttontitle%3Adestructivebuttontitle%3A%29.json'
content_hash: 'sha256:60b367242b0339b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# init(title:delegate:cancelButtonTitle:destructiveButtonTitle:)

<sub>Initializer</sub>

Initializes the action sheet using the specified starting parameters.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(title: String?, delegate: (any UIActionSheetDelegate)?, cancelButtonTitle: String?, destructiveButtonTitle: String?)
```

## Parameters

- `title` — A string to display in the title area of the action sheet. Pass `nil` if you don’t want to display any text in the title area.

- `delegate` — The receiver’s delegate object. Although this parameter may be `nil`, the delegate is used to respond to taps in the action sheet and should usually be provided.

- `cancelButtonTitle` — The title of the cancel button. This button is added to the action sheet automatically and assigned an appropriate index, which is available from the [cancelButtonIndex](cancelbuttonindex.md) property. This button is displayed in black to indicate that it represents the cancel action. Specify `nil` if you don’t want a cancel button or are presenting the action sheet on an iPad.

- `destructiveButtonTitle` — The title of the destructive button. This button is added to the action sheet automatically and assigned an appropriate index, which is available from the [destructiveButtonIndex](destructivebuttonindex.md) property. This button is displayed in red to indicate that it represents a destructive behavior. Specify `nil` if you don’t want a destructive button.

## Return Value

A newly initialized action sheet.

## Discussion

The action sheet automatically sets the appearance of the destructive and cancel buttons. If the action sheet contains only one button, it doesn’t apply the custom colors associated with the destructive and cancel buttons.

## See Also

### Creating action sheets

- [init(title:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:_:)](<init(title_delegate_cancelbuttontitle_destructivebuttontitle_otherbuttontitles___).md>) — Creates an action sheet with the specified values. _(deprecated)_
