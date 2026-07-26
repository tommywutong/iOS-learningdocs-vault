---
title: UICommandTagShare
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicommandtagshare
source_url: 'https://developer.apple.com/documentation/uikit/uicommandtagshare'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicommandtagshare.json'
content_hash: 'sha256:a2e97e4f1146a3fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICommandTagShare

<sub>Global Variable</sub>

A value that identifies a command as a Share menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
let UICommandTagShare: String
```

## Discussion

To create a Share menu, add [UICommandTagShare](uicommandtagshare.md) to the `propertyList` of a [UICommand](uicommand.md) or [UIKeyCommand](uikeycommand.md) object.

```swift
// Ensure that the builder is modifying the menu bar system.
guard builder.system == UIMenuSystem.main else { return }

let shareCommand = UICommand(title: "Share",
                             action: #selector(share(_:)),
                             propertyList: UICommandTagShare)

let shareMenu = UIMenu(title: "", options: .displayInline, children: [shareCommand])

// Insert the menu into the File menu before the Close menu.
builder.insertSibling(shareMenu, beforeMenu: .close)
```

## See Also

### Associating data

- [propertyList](uicommand/propertylist.md) — An object that contains data to associate with the command.
