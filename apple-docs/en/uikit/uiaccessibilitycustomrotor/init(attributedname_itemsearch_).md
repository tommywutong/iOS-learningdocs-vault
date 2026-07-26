---
title: 'init(attributedName:itemSearch:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilitycustomrotor/init(attributedname:itemsearch:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/init(attributedname:itemsearch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomrotor/init%28attributedname%3Aitemsearch%3A%29.json'
content_hash: 'sha256:741deb68732d86fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomRotor](../uiaccessibilitycustomrotor.md)

# init(attributedName:itemSearch:)

<sub>Initializer</sub>

Creates a rotor with the specified name and search block.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(attributedName: NSAttributedString, itemSearch itemSearchBlock: @escaping UIAccessibilityCustomRotor.Search)
```

## Parameters

- `attributedName` — The name of the rotor.

- `itemSearchBlock` — The block that provides the next or previous rotor.

## Return Value

An initialized rotor object.

## See Also

### Creating a rotor object

- [- initWithName:itemSearchBlock:](<init(name_itemsearch_).md>) — Creates a rotor with the specified name and search block.
- [- initWithSystemType:itemSearchBlock:](<init(systemtype_itemsearch_).md>) — Creates a rotor for the specified type of item.
