---
title: UserInfo Dictionary Keys
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/userinfo-dictionary-keys
source_url: 'https://developer.apple.com/documentation/uikit/userinfo-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/userinfo-dictionary-keys.json'
content_hash: 'sha256:a60091ebbff92a42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Documents, data, and pasteboard](documents-data-and-pasteboard.md) · [UIPasteboard](uipasteboard.md)

# UserInfo Dictionary Keys

<sub>API Collection</sub>

Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.

## Topics

### Constants

- [UIPasteboardChangedTypesAddedKey](uipasteboard/changedtypesaddeduserinfokey.md) — With the notification named [UIPasteboardChangedNotification](uipasteboard/changednotification.md), use this key to access the added representation types. These types are stored as an array in the notification’s `userInfo` dictionary.
- [UIPasteboardChangedTypesRemovedKey](uipasteboard/changedtypesremoveduserinfokey.md) — With the notification named [UIPasteboardChangedNotification](uipasteboard/changednotification.md), use this key to access the removed representation types. These types are stored as an array in the notification’s `userInfo` dictionary.

## See Also

### Constants

- [Name](uipasteboard/name-swift.struct.md) — Constants that identify the name of a pasteboard.
- [Pasteboard Names](pasteboard-names.md) — Names identifying the system pasteboards.
- [OptionsKey](uipasteboard/optionskey.md) — Options for describing pasteboard privacy.
- [Pasteboard Data Type Representations](pasteboard-data-type-representations.md) — Pasteboard-item representation types, as for a given object value.
