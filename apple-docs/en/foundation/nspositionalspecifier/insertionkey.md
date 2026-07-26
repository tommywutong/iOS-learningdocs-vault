---
title: insertionKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspositionalspecifier/insertionkey
source_url: 'https://developer.apple.com/documentation/foundation/nspositionalspecifier/insertionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspositionalspecifier/insertionkey.json'
content_hash: 'sha256:9d7ea62f8335c0dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPositionalSpecifier](../nspositionalspecifier.md)

# insertionKey

<sub>Instance Property</sub>

Returns the key that identifies the relationship into which the new or copied object or objects should be inserted.

<sub>Mac Catalyst, macOS</sub>

```swift
var insertionKey: String? { get }
```

## Return Value

A key. Determined by evaluating the receiver.

## See Also

### Accessing information about a positional specifier

- [insertionContainer](insertioncontainer.md) — Returns the container in which the new or copied object or objects should be placed.
- [insertionIndex](insertionindex.md) — Returns an insertion index that indicates where the new or copied object or objects should be placed.
- [insertionReplaces](insertionreplaces.md) — Returns a Boolean value that indicates whether evaluation has been successful and the object to be inserted should actually replace the keyed, indexed object in the insertion container.
- [objectSpecifier](objectspecifier.md) — Returns the object specifier specified at initialization time.
- [position](position.md) — Returns the insertion position specified at initialization time.
- [- setInsertionClassDescription:](<setinsertionclassdescription(__).md>) — Sets the class description for the object or objects to be inserted.
