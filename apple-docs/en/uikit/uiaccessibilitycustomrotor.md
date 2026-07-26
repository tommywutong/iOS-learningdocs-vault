---
title: UIAccessibilityCustomRotor
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycustomrotor
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomrotor.json'
content_hash: 'sha256:50331dc5cd5e0c1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityCustomRotor

<sub>Class</sub>

A context-sensitive function that helps VoiceOver users find the next instance of a related element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIAccessibilityCustomRotor
```

## Overview

You might use an instance of this class to find the next link in an article, or the next misspelled word in a document.

> [!note] Related Sessions from WWDC20
> Session 10116: [VoiceOver Efficiency with Custom Rotors](https://developer.apple.com/wwdc20/10116)

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a rotor object

- [- initWithAttributedName:itemSearchBlock:](<uiaccessibilitycustomrotor/init(attributedname_itemsearch_).md>) — Creates a rotor with the specified name and search block.
- [- initWithName:itemSearchBlock:](<uiaccessibilitycustomrotor/init(name_itemsearch_).md>) — Creates a rotor with the specified name and search block.
- [- initWithSystemType:itemSearchBlock:](<uiaccessibilitycustomrotor/init(systemtype_itemsearch_).md>) — Creates a rotor for the specified type of item.

### Navigating to the next item

- [itemSearchBlock](uiaccessibilitycustomrotor/itemsearchblock.md) — The block for retrieving the next or previous rotor.
- [Search](uiaccessibilitycustomrotor/search.md) — The block type for retrieving the next or previous rotor.
- [Direction](uiaccessibilitycustomrotor/direction.md) — Constants that indicate the search direction.

### Getting the rotor type

- [systemRotorType](uiaccessibilitycustomrotor/systemrotortype-swift.property.md) — The type of content that the rotor searches.
- [SystemRotorType](uiaccessibilitycustomrotor/systemrotortype-swift.enum.md) — Constants that indicate the type of content that the rotor represents.

### Identifying the rotor

- [name](uiaccessibilitycustomrotor/name.md) — The name of the rotor.
- [attributedName](uiaccessibilitycustomrotor/attributedname.md) — The name of the rotor as an attributed string.

### Initializers

- [init(attributedName:itemSearchBlock:)](<uiaccessibilitycustomrotor/init(attributedname_itemsearchblock_).md>)
- [init(name:itemSearchBlock:)](<uiaccessibilitycustomrotor/init(name_itemsearchblock_).md>)
- [init(systemType:itemSearchBlock:)](<uiaccessibilitycustomrotor/init(systemtype_itemsearchblock_).md>)

## See Also

### Navigation

- [UIAccessibilityCustomRotorItemResult](uiaccessibilitycustomrotoritemresult.md) — A target element that a custom rotor references.
- [UIAccessibilityCustomRotorSearchPredicate](uiaccessibilitycustomrotorsearchpredicate.md) — The search parameters that help determine the next matching custom rotor item result.
