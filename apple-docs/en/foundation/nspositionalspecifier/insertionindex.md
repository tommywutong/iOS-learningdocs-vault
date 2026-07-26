---
title: insertionIndex
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspositionalspecifier/insertionindex
source_url: 'https://developer.apple.com/documentation/foundation/nspositionalspecifier/insertionindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspositionalspecifier/insertionindex.json'
content_hash: 'sha256:bd690144b665e9d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPositionalSpecifier](../nspositionalspecifier.md)

# insertionIndex

<sub>Instance Property</sub>

Returns an insertion index that indicates where the new or copied object or objects should be placed.

<sub>Mac Catalyst, macOS</sub>

```swift
var insertionIndex: Int { get }
```

## Return Value

An insertion index. Determined by evaluating the receiver.

## See Also

### Accessing information about a positional specifier

- [insertionContainer](insertioncontainer.md) — Returns the container in which the new or copied object or objects should be placed.
- [insertionKey](insertionkey.md) — Returns the key that identifies the relationship into which the new or copied object or objects should be inserted.
- [insertionReplaces](insertionreplaces.md) — Returns a Boolean value that indicates whether evaluation has been successful and the object to be inserted should actually replace the keyed, indexed object in the insertion container.
- [objectSpecifier](objectspecifier.md) — Returns the object specifier specified at initialization time.
- [position](position.md) — Returns the insertion position specified at initialization time.
- [- setInsertionClassDescription:](<setinsertionclassdescription(__).md>) — Sets the class description for the object or objects to be inserted.
