---
title: UINavigationItemRenameDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitemrenamedelegate-96g5t
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-96g5t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-96g5t.json'
content_hash: 'sha256:b35a47d660b3ec04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UINavigationItemRenameDelegate

<sub>Protocol</sub>

Methods an object implements to rename a navigation item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UINavigationItemRenameDelegate <NSObject>
```

## Overview

A navigation item ([UINavigationItem](uinavigationitem.md)) uses this delegate to determine whether a person can change the navigation item’s title and to handle the rename process.

> [!note] Related Sessions from WWDC22
> Session 10069: [Meet desktop-class iPad](https://developer.apple.com/wwdc22/10069)
>
> Session 10070: [Build a desktop-class iPad app](https://developer.apple.com/wwdc22/10070)

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIDocument](uidocument.md)

## Topics

### Determining rename support

- [navigationItemShouldBeginRenaming:](uinavigationitemrenamedelegate-96g5t/navigationitemshouldbeginrenaming_.md) — Asks the delegate whether the navigation item supports renaming.
- [navigationItem:shouldEndRenamingWithTitle:](uinavigationitemrenamedelegate-96g5t/navigationitem_shouldendrenamingwithtitle_.md) — Asks the delegate whether to continue or abandon the rename process.

### Handling the rename process

- [navigationItem:willBeginRenamingWithSuggestedTitle:selectedRange:](uinavigationitemrenamedelegate-96g5t/navigationitem_willbeginrenamingwithsuggestedtitle_selectedrange_.md) — Tells the delegate when the rename process starts.
- [navigationItem:didEndRenamingWithTitle:](uinavigationitemrenamedelegate-96g5t/navigationitem_didendrenamingwithtitle_.md) — Tells the delegate when the rename process ends.

## See Also

### Renaming documents

- [renameDelegate](uinavigationitem/renamedelegate-o32h.md) — The delegate for renaming the navigation item.
