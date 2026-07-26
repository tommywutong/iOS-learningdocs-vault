---
title: 'init(systemType:itemSearch:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilitycustomrotor/init(systemtype:itemsearch:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/init(systemtype:itemsearch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomrotor/init%28systemtype%3Aitemsearch%3A%29.json'
content_hash: 'sha256:e9c779830f3d0917'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomRotor](../uiaccessibilitycustomrotor.md)

# init(systemType:itemSearch:)

<sub>Initializer</sub>

Creates a rotor for the specified type of item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(systemType type: UIAccessibilityCustomRotor.SystemRotorType, itemSearch itemSearchBlock: @escaping UIAccessibilityCustomRotor.Search)
```

## Parameters

- `type` — The type of content navigated by the rotor. For a list of possible values, see [SystemRotorType](systemrotortype-swift.enum.md).

- `itemSearchBlock` — The block that provides the next or previous rotor for the given type.

## Return Value

An initialized rotor object.

## See Also

### Creating a rotor object

- [- initWithAttributedName:itemSearchBlock:](<init(attributedname_itemsearch_).md>) — Creates a rotor with the specified name and search block.
- [- initWithName:itemSearchBlock:](<init(name_itemsearch_).md>) — Creates a rotor with the specified name and search block.
