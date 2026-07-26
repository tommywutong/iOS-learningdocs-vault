---
title: UINavigationItemRenameDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitemrenamedelegate-5j4ws
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-5j4ws.json'
content_hash: 'sha256:40089d7569459576'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UINavigationItemRenameDelegate

<sub>Protocol</sub>

Methods an object implements to rename a navigation item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency protocol UINavigationItemRenameDelegate : AnyObject
```

## Overview

A navigation item ([UINavigationItem](uinavigationitem.md)) uses this delegate to determine whether a person can change the navigation item’s title and to handle the rename process.

> [!note] Related Sessions from WWDC22
> Session 10069: [Meet desktop-class iPad](https://developer.apple.com/wwdc22/10069)
>
> Session 10070: [Build a desktop-class iPad app](https://developer.apple.com/wwdc22/10070)

## Topics

### Determining rename support

- [navigationItemShouldBeginRenaming(_:)](<uinavigationitemrenamedelegate-5j4ws/navigationitemshouldbeginrenaming(__).md>) — Asks the delegate whether the navigation item supports renaming.
- [navigationItem(_:shouldEndRenamingWith:)](<uinavigationitemrenamedelegate-5j4ws/navigationitem(__shouldendrenamingwith_).md>) — Asks the delegate whether to continue or abandon the rename process.

### Handling the rename process

- [navigationItem(_:willBeginRenamingWith:selectedRange:)](<uinavigationitemrenamedelegate-5j4ws/navigationitem(__willbeginrenamingwith_selectedrange_).md>) — Tells the delegate when the rename process starts.
- [navigationItem(_:didEndRenamingWith:)](<uinavigationitemrenamedelegate-5j4ws/navigationitem(__didendrenamingwith_).md>) — Tells the delegate when the rename process ends.

## See Also

### Renaming documents

- [renameDelegate](uinavigationitem/renamedelegate-8jiuf.md) — The delegate for renaming the navigation item.
