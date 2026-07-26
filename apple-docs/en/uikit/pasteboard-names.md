---
title: Pasteboard Names
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/pasteboard-names
source_url: 'https://developer.apple.com/documentation/uikit/pasteboard-names'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/pasteboard-names.json'
content_hash: 'sha256:b4dbbdc0862f5ef5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Documents, data, and pasteboard](documents-data-and-pasteboard.md) · [UIPasteboard](uipasteboard.md)

# Pasteboard Names

<sub>API Collection</sub>

Names identifying the system pasteboards.

## Overview

You can access the general system pasteboard by calling the class method [+ pasteboardWithName:create:](<uipasteboard/init(name_create_).md>), specifying the `UIPasteboardNameGeneral` constant as the first argument. You can alternatively access the general pasteboard by calling the [generalPasteboard](uipasteboard/general.md) class method. The general system pasteboard is persistent across device restarts, app uninstalls, and app restores.

## Topics

### Constants

- [UIPasteboardNameGeneral](uipasteboard/name-swift.struct/general.md) — The name identifying the general pasteboard, which you use for general copy-cut-paste operations.
- [UIPasteboardNameFind](uipasteboardnamefind.md) — A name that identifies the Find pasteboard. _(deprecated)_

## See Also

### Constants

- [Name](uipasteboard/name-swift.struct.md) — Constants that identify the name of a pasteboard.
- [OptionsKey](uipasteboard/optionskey.md) — Options for describing pasteboard privacy.
- [Pasteboard Data Type Representations](pasteboard-data-type-representations.md) — Pasteboard-item representation types, as for a given object value.
- [UserInfo Dictionary Keys](userinfo-dictionary-keys.md) — Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.
