---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（11.0 起废弃）, iPadOS 8.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentmenuviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentmenuviewcontroller/delegate.json'
content_hash: 'sha256:dd639ea00b206be0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md)

# delegate

<sub>Instance Property</sub>

The document menu’s delegate.

> [!warning] Deprecated
> For more information, see [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
weak var delegate: (any UIDocumentMenuDelegate)? { get set }
```

## Discussion

The delegate must adopt the [UIDocumentMenuDelegate](../uidocumentmenudelegate.md) protocol.

## See Also

### Getting the user-selected document picker

- [UIDocumentMenuDelegate](../uidocumentmenudelegate.md) — A set of methods that you must implement to track user interactions with a document menu view controller. _(deprecated)_
