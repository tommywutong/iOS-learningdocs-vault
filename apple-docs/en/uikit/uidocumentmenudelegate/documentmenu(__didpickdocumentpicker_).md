---
title: 'documentMenu(_:didPickDocumentPicker:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentmenudelegate/documentmenu(_:didpickdocumentpicker:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/documentmenu(_:didpickdocumentpicker:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentmenudelegate/documentmenu%28_%3Adidpickdocumentpicker%3A%29.json'
content_hash: 'sha256:91a7591311bb5a5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentMenuDelegate](../uidocumentmenudelegate.md)

# documentMenu(_:didPickDocumentPicker:)

<sub>Instance Method</sub>

Tells the delegate that the user has selected a document picker from the menu.

> [!warning] Deprecated
> For more information, see [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func documentMenu(_ documentMenu: UIDocumentMenuViewController, didPickDocumentPicker documentPicker: UIDocumentPickerViewController)
```

## Parameters

- `documentMenu` — The document menu object that called this method.

- `documentPicker` — The document picker that the user selected.

## Discussion

The document menu calls this method when the user selects a document picker. Set the document picker’s delegate, and then present it.

## See Also

### Responding to user actions

- [- documentMenuWasCancelled:](<documentmenuwascancelled(__).md>) — Tells the delegate that the user dismissed the document menu. _(deprecated)_
