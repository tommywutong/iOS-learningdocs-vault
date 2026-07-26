---
title: UIPasteboard.OptionsKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/optionskey
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/optionskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/optionskey.json'
content_hash: 'sha256:400e56e7a0cde49a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# UIPasteboard.OptionsKey

<sub>Structure</sub>

Options for describing pasteboard privacy.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct OptionsKey
```

## Overview

Use these options with the [- setItems:options:](<setitems(__options_).md>) method. Options that you set apply to all the items on a pasteboard.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIPasteboardOptionExpirationDate](optionskey/expirationdate.md) — The time and date that you want the system to remove the pasteboard items from the pasteboard.
- [UIPasteboardOptionLocalOnly](optionskey/localonly.md) — A Boolean value that specifies that the pasteboard items should not be available to other devices through the Handoff feature.

### Initializers

- [init(rawValue:)](<optionskey/init(rawvalue_).md>)

## See Also

### Constants

- [Name](name-swift.struct.md) — Constants that identify the name of a pasteboard.
- [Pasteboard Names](../pasteboard-names.md) — Names identifying the system pasteboards.
- [Pasteboard Data Type Representations](../pasteboard-data-type-representations.md) — Pasteboard-item representation types, as for a given object value.
- [UserInfo Dictionary Keys](../userinfo-dictionary-keys.md) — Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.
