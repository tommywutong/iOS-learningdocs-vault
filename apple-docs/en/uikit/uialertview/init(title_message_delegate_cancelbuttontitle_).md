---
title: 'init(title:message:delegate:cancelButtonTitle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertview/init(title:message:delegate:cancelbuttontitle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/init(title:message:delegate:cancelbuttontitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/init%28title%3Amessage%3Adelegate%3Acancelbuttontitle%3A%29.json'
content_hash: 'sha256:e068fcde8a3a82b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# init(title:message:delegate:cancelButtonTitle:)

<sub>Initializer</sub>

Convenience method for initializing an alert view.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
convenience init(title: String?, message: String?, delegate: Any?, cancelButtonTitle: String?)
```

## Parameters

- `title` — The string that appears in the receiver’s title bar.

- `message` — Descriptive text that provides more details than the title.

- `delegate` — The receiver’s delegate or `nil` if it doesn’t have a delegate.

- `cancelButtonTitle` — The title of the cancel button or `nil` if there’s no cancel button. Using this argument is equivalent to setting the cancel button index to the value returned by invoking [- addButtonWithTitle:](<addbutton(withtitle_).md>) specifying this title.

## Return Value

Newly initialized alert view.

## See Also

### Creating alert views

- [init(title:message:delegate:cancelButtonTitle:otherButtonTitles:_:)](<init(title_message_delegate_cancelbuttontitle_otherbuttontitles___).md>) — Creates an alert view with the specified values. _(deprecated)_
- [- initWithFrame:](<init(frame_).md>) — Creates an alert view with the specified frame. _(deprecated)_
- [- initWithCoder:](<init(coder_).md>) — Creates an alert view from data in an unarchiver. _(deprecated)_
