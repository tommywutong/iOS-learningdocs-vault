---
title: 'setInsertionClassDescription(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspositionalspecifier/setinsertionclassdescription(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspositionalspecifier/setinsertionclassdescription(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspositionalspecifier/setinsertionclassdescription%28_%3A%29.json'
content_hash: 'sha256:c3c71c9a780f5752'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPositionalSpecifier](../nspositionalspecifier.md)

# setInsertionClassDescription(_:)

<sub>Instance Method</sub>

Sets the class description for the object or objects to be inserted.

<sub>Mac Catalyst, macOS</sub>

```swift
func setInsertionClassDescription(_ classDescription: NSScriptClassDescription)
```

## Parameters

- `classDescription` — The class description for the object or objects to be inserted.

## Discussion

This message can be sent at any time after object initialization, but must be sent before evaluation to have any effect.

## See Also

### Accessing information about a positional specifier

- [insertionContainer](insertioncontainer.md) — Returns the container in which the new or copied object or objects should be placed.
- [insertionIndex](insertionindex.md) — Returns an insertion index that indicates where the new or copied object or objects should be placed.
- [insertionKey](insertionkey.md) — Returns the key that identifies the relationship into which the new or copied object or objects should be inserted.
- [insertionReplaces](insertionreplaces.md) — Returns a Boolean value that indicates whether evaluation has been successful and the object to be inserted should actually replace the keyed, indexed object in the insertion container.
- [objectSpecifier](objectspecifier.md) — Returns the object specifier specified at initialization time.
- [position](position.md) — Returns the insertion position specified at initialization time.
