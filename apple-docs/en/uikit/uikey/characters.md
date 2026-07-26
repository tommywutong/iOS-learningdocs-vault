---
title: characters
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, tvOS 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikey/characters
source_url: 'https://developer.apple.com/documentation/uikit/uikey/characters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikey/characters.json'
content_hash: 'sha256:75ef2404dcb7c064'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKey](../uikey.md)

# characters

<sub>Instance Property</sub>

A string that represents the text value of the key combined with any active modifier keys.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var characters: String { get }
```

## Discussion

When the user holds one or more modifier keys, this property contains the modified characters according to the rules of the particular modifier keys. For example, if the user holds Shift while pressing a letter button on a Latin keyboard, this property contains a capital letter.

## See Also

### Getting key characters

- [charactersIgnoringModifiers](charactersignoringmodifiers.md) — A string that represents the text value of the key without modifier keys.
