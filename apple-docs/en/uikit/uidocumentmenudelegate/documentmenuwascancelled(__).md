---
title: 'documentMenuWasCancelled(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentmenudelegate/documentmenuwascancelled(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/documentmenuwascancelled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentmenudelegate/documentmenuwascancelled%28_%3A%29.json'
content_hash: 'sha256:a94105ea3dcc024e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentMenuDelegate](../uidocumentmenudelegate.md)

# documentMenuWasCancelled(_:)

<sub>Instance Method</sub>

Tells the delegate that the user dismissed the document menu.

> [!warning] Deprecated
> For more information, see [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func documentMenuWasCancelled(_ documentMenu: UIDocumentMenuViewController)
```

## Parameters

- `documentMenu` — The document menu object that called this method.

## See Also

### Responding to user actions

- [- documentMenu:didPickDocumentPicker:](<documentmenu(__didpickdocumentpicker_).md>) — Tells the delegate that the user has selected a document picker from the menu. _(deprecated)_
