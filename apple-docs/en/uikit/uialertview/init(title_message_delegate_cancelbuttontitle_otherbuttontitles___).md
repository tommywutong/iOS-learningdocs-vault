---
title: 'init(title:message:delegate:cancelButtonTitle:otherButtonTitles:_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 2.0+（9.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertview/init(title:message:delegate:cancelbuttontitle:otherbuttontitles:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/init(title:message:delegate:cancelbuttontitle:otherbuttontitles:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/init%28title%3Amessage%3Adelegate%3Acancelbuttontitle%3Aotherbuttontitles%3A_%3A%29.json'
content_hash: 'sha256:3082a839c9f28927'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# init(title:message:delegate:cancelButtonTitle:otherButtonTitles:_:)

<sub>Initializer</sub>

Creates an alert view with the specified values.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency convenience init(title: String, message: String, delegate: (any UIAlertViewDelegate)?, cancelButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...)
```

## See Also

### Creating alert views

- [- initWithTitle:message:delegate:cancelButtonTitle:otherButtonTitles:](<init(title_message_delegate_cancelbuttontitle_).md>) — Convenience method for initializing an alert view. _(deprecated)_
- [- initWithFrame:](<init(frame_).md>) — Creates an alert view with the specified frame. _(deprecated)_
- [- initWithCoder:](<init(coder_).md>) — Creates an alert view from data in an unarchiver. _(deprecated)_
