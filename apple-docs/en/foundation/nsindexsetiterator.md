---
title: NSIndexSetIterator
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsindexsetiterator
source_url: 'https://developer.apple.com/documentation/foundation/nsindexsetiterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexsetiterator.json'
content_hash: 'sha256:dfd2cbc95076a1fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIndexSetIterator

<sub>Structure</sub>

An iterator suitable for enumerating the elements of an index set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSIndexSetIterator
```

## Overview

You typically obtain an index set iterator by calling the [makeIterator()](<nsindexset/makeiterator().md>) function of an [NSIndexSet](nsindexset.md) instance.

## Relationships

- **Conforms To**: [IteratorProtocol](../swift/iteratorprotocol.md)

## See Also

### Iteration

- [NSEnumerator](nsenumerator.md) — An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.
- [NSFastEnumeration](nsfastenumeration.md) — A protocol that objects adopt to support fast enumeration.
- [NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [NSEnumerationOptions](nsenumerationoptions.md) — Options for block enumeration operations.
- [NSSortOptions](nssortoptions.md) — Options for block sorting operations.
