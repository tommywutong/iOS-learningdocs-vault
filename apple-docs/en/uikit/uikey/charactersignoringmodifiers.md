---
title: charactersIgnoringModifiers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, tvOS 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikey/charactersignoringmodifiers
source_url: 'https://developer.apple.com/documentation/uikit/uikey/charactersignoringmodifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikey/charactersignoringmodifiers.json'
content_hash: 'sha256:dc5793cebec695f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKey](../uikey.md)

# charactersIgnoringModifiers

<sub>Instance Property</sub>

A string that represents the text value of the key without modifier keys.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var charactersIgnoringModifiers: String { get }
```

## Discussion

For Latin-based languages, always expect a lowercase property value. If the user is pressing only a modifier key, the property value is an empty string.

To check for special keys, compare [charactersIgnoringModifiers](charactersignoringmodifiers.md) to constants listed in [Input strings for special keys](../input-strings-for-special-keys.md).

## See Also

### Getting key characters

- [characters](characters.md) — A string that represents the text value of the key combined with any active modifier keys.
