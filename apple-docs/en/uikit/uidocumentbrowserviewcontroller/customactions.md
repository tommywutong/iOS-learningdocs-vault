---
title: customActions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/customactions
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/customactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/customactions.json'
content_hash: 'sha256:92755ec4ebaf4756'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# customActions

<sub>Instance Property</sub>

Custom document browser actions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var customActions: [UIDocumentBrowserAction] { get set }
```

## Discussion

By default, this property contains an empty array. Assign an array of [UIDocumentBrowserAction](../uidocumentbrowseraction.md) objects to add custom document browser actions.

Document browser actions can be accessed in two ways:

- _Navigation bar_ actions appear in the Navigation bar when the user places the browser into the Select mode.
- _Menu_ actions appear when the user long presses on a document or folder.

When triggered, these actions are passed the URLs of the currently selected items.

## See Also

### Adding custom actions

- [UIDocumentBrowserAction](../uidocumentbrowseraction.md) — A custom action that you can create and add to a document browser’s Edit menu or navigation bar.
