---
title: objectSpecifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspositionalspecifier/objectspecifier
source_url: 'https://developer.apple.com/documentation/foundation/nspositionalspecifier/objectspecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspositionalspecifier/objectspecifier.json'
content_hash: 'sha256:7c4864170803bc17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPositionalSpecifier](../nspositionalspecifier.md)

# objectSpecifier

<sub>Instance Property</sub>

Returns the object specifier specified at initialization time.

<sub>macOS</sub>

```swift
var objectSpecifier: NSScriptObjectSpecifier { get }
```

## Return Value

An object specifier for a container.

## See Also

### Accessing information about a positional specifier

- [insertionContainer](insertioncontainer.md) — Returns the container in which the new or copied object or objects should be placed.
- [insertionIndex](insertionindex.md) — Returns an insertion index that indicates where the new or copied object or objects should be placed.
- [insertionKey](insertionkey.md) — Returns the key that identifies the relationship into which the new or copied object or objects should be inserted.
- [insertionReplaces](insertionreplaces.md) — Returns a Boolean value that indicates whether evaluation has been successful and the object to be inserted should actually replace the keyed, indexed object in the insertion container.
- [position](position.md) — Returns the insertion position specified at initialization time.
- [- setInsertionClassDescription:](<setinsertionclassdescription(__).md>) — Sets the class description for the object or objects to be inserted.
